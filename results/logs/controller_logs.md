# starting up controller

```bash
seed@seedvm2006:~/Documents/mininet$ ryu-manager controller/static_routing_controller.py 
loading app controller/static_routing_controller.py
loading app ryu.controller.ofp_handler
instantiating app controller/static_routing_controller.py of StaticRoutingController
instantiating app ryu.controller.ofp_handler of OFPHandler
```

# after starting up topology using mininet

```bash
Switch connected: dpid=1
Switch connected: dpid=3
Switch connected: dpid=2
packet_in dpid=1 eth_src=0e:80:51:b1:39:80 eth_dst=33:33:00:00:00:02
packet_in dpid=3 eth_src=ce:3a:51:02:4e:36 eth_dst=33:33:00:00:00:fb
packet_in dpid=1 eth_src=ae:14:17:6c:8d:45 eth_dst=33:33:00:00:00:fb
packet_in dpid=1 eth_src=0e:80:51:b1:39:80 eth_dst=33:33:00:00:00:fb
packet_in dpid=2 eth_src=fa:3d:bf:b0:3d:af eth_dst=33:33:00:00:00:fb
packet_in dpid=1 eth_src=9e:bb:ca:f3:df:28 eth_dst=33:33:00:00:00:02
packet_in dpid=3 eth_src=ce:3a:51:02:4e:36 eth_dst=33:33:00:00:00:02
packet_in dpid=3 eth_src=2a:97:a3:7f:0e:d4 eth_dst=33:33:00:00:00:02
packet_in dpid=2 eth_src=fa:3d:bf:b0:3d:af eth_dst=33:33:00:00:00:02
packet_in dpid=1 eth_src=ea:13:aa:a3:86:2e eth_dst=33:33:00:00:00:02
packet_in dpid=1 eth_src=ae:14:17:6c:8d:45 eth_dst=33:33:00:00:00:02
packet_in dpid=2 eth_src=32:51:a5:e0:46:fc eth_dst=33:33:00:00:00:02
```
