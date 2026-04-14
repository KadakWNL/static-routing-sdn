# initial dumpflows

```bash
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s1
[sudo] password for seed: 
 cookie=0x0, duration=214.256s, table=0, n_packets=114793, n_bytes=7577122, priority=100,ip,nw_dst=10.0.0.1 actions=output:"s1-eth1"
 cookie=0x0, duration=214.256s, table=0, n_packets=11, n_bytes=1078, priority=100,ip,nw_dst=10.0.0.2 actions=output:"s1-eth2"
 cookie=0x0, duration=214.256s, table=0, n_packets=266775, n_bytes=12249908794, priority=100,ip,nw_dst=10.0.0.3 actions=output:"s1-eth3"
 cookie=0x0, duration=214.256s, table=0, n_packets=11, n_bytes=1078, priority=100,ip,nw_dst=10.0.0.4 actions=output:"s1-eth4"
 cookie=0x0, duration=214.256s, table=0, n_packets=26, n_bytes=1092, priority=10,arp actions=FLOOD
 cookie=0x0, duration=214.256s, table=0, n_packets=64, n_bytes=7032, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s2
 cookie=0x0, duration=216.394s, table=0, n_packets=114789, n_bytes=7576730, priority=100,ip,nw_dst=10.0.0.1 actions=output:"s2-eth3"
 cookie=0x0, duration=216.394s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.2 actions=output:"s2-eth3"
 cookie=0x0, duration=216.394s, table=0, n_packets=266775, n_bytes=12249908794, priority=100,ip,nw_dst=10.0.0.3 actions=output:"s2-eth1"
 cookie=0x0, duration=216.394s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.4 actions=output:"s2-eth3"
 cookie=0x0, duration=216.394s, table=0, n_packets=26, n_bytes=1092, priority=10,arp actions=FLOOD
 cookie=0x0, duration=216.394s, table=0, n_packets=32, n_bytes=3516, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s3
 cookie=0x0, duration=218.130s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.1 actions=output:"s3-eth3"
 cookie=0x0, duration=218.130s, table=0, n_packets=7, n_bytes=686, priority=100,ip,nw_dst=10.0.0.2 actions=output:"s3-eth3"
 cookie=0x0, duration=218.130s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.3 actions=output:"s3-eth3"
 cookie=0x0, duration=218.130s, table=0, n_packets=11, n_bytes=1078, priority=100,ip,nw_dst=10.0.0.4 actions=output:"s3-eth1"
 cookie=0x0, duration=218.130s, table=0, n_packets=26, n_bytes=1092, priority=10,arp actions=FLOOD
 cookie=0x0, duration=218.130s, table=0, n_packets=33, n_bytes=3606, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ 

```

# deleting flows recovered flows after flow dump

```bash
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 del-flows s1 "ip"
sudo ovs-ofctl -O OpenFlow13 del-flows s2 "ip"
sudo ovs-ofctl -O OpenFlow13 del-flows s3 "ip"
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x0, duration=364.797s, table=0, n_packets=30, n_bytes=1260, priority=10,arp actions=FLOOD
 cookie=0x0, duration=364.797s, table=0, n_packets=73, n_bytes=7820, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s2
 cookie=0x0, duration=382.014s, table=0, n_packets=34, n_bytes=1428, priority=10,arp actions=FLOOD
 cookie=0x0, duration=382.014s, table=0, n_packets=35, n_bytes=3763, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s3
 cookie=0x0, duration=383.734s, table=0, n_packets=34, n_bytes=1428, priority=10,arp actions=FLOOD
 cookie=0x0, duration=383.734s, table=0, n_packets=36, n_bytes=3853, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s1
 cookie=0x0, duration=123.677s, table=0, n_packets=6, n_bytes=588, priority=100,ip,nw_dst=10.0.0.1 actions=output:"s1-eth1"
 cookie=0x0, duration=123.677s, table=0, n_packets=6, n_bytes=588, priority=100,ip,nw_dst=10.0.0.2 actions=output:"s1-eth2"
 cookie=0x0, duration=123.677s, table=0, n_packets=6, n_bytes=588, priority=100,ip,nw_dst=10.0.0.3 actions=output:"s1-eth3"
 cookie=0x0, duration=123.677s, table=0, n_packets=6, n_bytes=588, priority=100,ip,nw_dst=10.0.0.4 actions=output:"s1-eth4"
 cookie=0x0, duration=123.677s, table=0, n_packets=24, n_bytes=1008, priority=10,arp actions=FLOOD
 cookie=0x0, duration=123.677s, table=0, n_packets=55, n_bytes=6304, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s2
 cookie=0x0, duration=125.818s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.1 actions=output:"s2-eth3"
 cookie=0x0, duration=125.818s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.2 actions=output:"s2-eth3"
 cookie=0x0, duration=125.818s, table=0, n_packets=6, n_bytes=588, priority=100,ip,nw_dst=10.0.0.3 actions=output:"s2-eth1"
 cookie=0x0, duration=125.818s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.4 actions=output:"s2-eth3"
 cookie=0x0, duration=125.825s, table=0, n_packets=24, n_bytes=1008, priority=10,arp actions=FLOOD
 cookie=0x0, duration=125.825s, table=0, n_packets=31, n_bytes=3429, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ sudo ovs-ofctl -O OpenFlow13 dump-flows s3
 cookie=0x0, duration=128.086s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.1 actions=output:"s3-eth3"
 cookie=0x0, duration=128.086s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.2 actions=output:"s3-eth3"
 cookie=0x0, duration=128.086s, table=0, n_packets=2, n_bytes=196, priority=100,ip,nw_dst=10.0.0.3 actions=output:"s3-eth3"
 cookie=0x0, duration=128.086s, table=0, n_packets=6, n_bytes=588, priority=100,ip,nw_dst=10.0.0.4 actions=output:"s3-eth1"
 cookie=0x0, duration=128.086s, table=0, n_packets=24, n_bytes=1008, priority=10,arp actions=FLOOD
 cookie=0x0, duration=128.086s, table=0, n_packets=31, n_bytes=3446, priority=0 actions=CONTROLLER:65535
seed@seedvm2006:~/Documents/mininet$ 
```
