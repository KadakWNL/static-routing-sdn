from mininet.topo import Topo

class OrangeTopo(Topo):
    def build(self):
        # add hosts with their ip
        h1 = self.addHost("h1", ip="10.0.0.1/24")
        h2 = self.addHost("h2", ip="10.0.0.2/24")
        h3 = self.addHost("h3", ip="10.0.0.3/24")
        h4 = self.addHost("h4", ip="10.0.0.4/24")

        # add switches
        s1 = self.addSwitch("s1", protocols="OpenFlow13")
        s2 = self.addSwitch("s2", protocols="OpenFlow13")
        s3 = self.addSwitch("s3", protocols="OpenFlow13")

        # build the links bw hosts and switches
        self.addLink(h1, s1, port2=1)
        self.addLink(h2, s1, port2=2)
        self.addLink(h3, s2, port2=1)
        self.addLink(h4, s3, port2=1)

        self.addLink(s1, s2, port1=3, port2=3)
        self.addLink(s1, s3, port1=4, port2=3)

topos = {"orange": (lambda: OrangeTopo())}