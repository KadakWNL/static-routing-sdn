from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet, ipv4

# Main controller class (control plane logic)
class StaticRoutingController(app_manager.RyuApp):
    # Use OpenFlow 1.3 protocol
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    # Function to install a flow rule into a switch
    def add_flow(self, datapath, priority, match, actions, idle=0, hard=0):
        ofp = datapath.ofproto              # datapath -> switch, get current openflow protocols of the switch
        parser = datapath.ofproto_parser    # used to build OpenFlow messages

        # Wrap actions into an instruction (required by OpenFlow)
        inst = [parser.OFPInstructionActions(ofp.OFPIT_APPLY_ACTIONS, actions)]

        # Create a FlowMod message (this is the actual rule)
        mod = parser.OFPFlowMod(
            datapath=datapath,              # Target switch
            priority=priority,              # Rule priority
            match=match,                    # Matching condition
            instructions=inst,              # Actions wrapped as instructions
            idle_timeout=idle,              # Remove if idle for this time
            hard_timeout=hard               # Remove after fixed time
        )

        # Send the rule to the switch
        datapath.send_msg(mod)

    # Install all static routing rules into a switch
    def install_static_rules(self, datapath):
        dpid = datapath.id                 # Switch ID
        parser = datapath.ofproto_parser
        ofp = datapath.ofproto

        # Default rule (lowest priority)
        # If no other rule matches → send packet to controller
        self.add_flow(
            datapath,
            0,
            parser.OFPMatch(),  # Match everything
            [parser.OFPActionOutput(ofp.OFPP_CONTROLLER, ofp.OFPCML_NO_BUFFER)]
        )

        # ARP rule
        # Flood ARP packets so hosts can discover each other
        self.add_flow(
            datapath,
            10,
            parser.OFPMatch(eth_type=0x0806),  # ARP packets
            [parser.OFPActionOutput(ofp.OFPP_FLOOD)]
        )

        # Static routing table (per switch)
        # Maps destination IP → output port
        routes = {
            1: {"10.0.0.1": 1, "10.0.0.2": 2, "10.0.0.3": 3, "10.0.0.4": 4},
            2: {"10.0.0.1": 3, "10.0.0.2": 3, "10.0.0.3": 1, "10.0.0.4": 3},
            3: {"10.0.0.1": 3, "10.0.0.2": 3, "10.0.0.3": 3, "10.0.0.4": 1},
        }

        # Install rules only if this switch has entries
        if dpid in routes:
            for dst_ip, out_port in routes[dpid].items():
                # Match IPv4 packets going to a specific destination IP
                match = parser.OFPMatch(eth_type=0x0800, ipv4_dst=dst_ip)

                # Action: forward packet to the correct port
                actions = [parser.OFPActionOutput(out_port)]

                # Install high-priority rule for routing
                self.add_flow(datapath, 100, match, actions)

    # Triggered when a switch connects to the controller
    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        self.logger.info("Switch connected: dpid=%s", datapath.id)

        # Install all predefined rules into this switch
        self.install_static_rules(datapath)

    # Triggered when a packet is sent to controller (no matching rule)
    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        msg = ev.msg
        datapath = msg.datapath

        # Parse the incoming packet
        pkt = packet.Packet(msg.data)
        eth = pkt.get_protocol(ethernet.ethernet)
        ip = pkt.get_protocol(ipv4.ipv4)

        # If it's an IP packet → log source and destination IP
        if ip:
            self.logger.info("packet_in dpid=%s src=%s dst=%s",
                             datapath.id, ip.src, ip.dst)

        # Otherwise log Ethernet info
        elif eth:
            self.logger.info("packet_in dpid=%s eth_src=%s eth_dst=%s",
                             datapath.id, eth.src, eth.dst)