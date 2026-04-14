# after starting up mininet

```bash
seed@seedvm2006:~/Documents/mininet$ sudo mn --custom topology/topo_orange.py --topo orange --controller remote,ip=127.0.0.1,port=6653 --switch ovsk,protocols=OpenFlow13
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 
*** Adding switches:
s1 s2 s3 
*** Adding links:
(h1, s1) (h2, s1) (h3, s2) (h4, s3) (s1, s2) (s1, s3) 
*** Configuring hosts
h1 h2 h3 h4 
*** Starting controller
c0 
*** Starting 3 switches
s1 s2 s3 ...
*** Starting CLI:
mininet> 

```

# pingall, etc

```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 
h2 -> h1 h3 h4 
h3 -> h1 h2 h4 
h4 -> h1 h2 h3 
*** Results: 0% dropped (12/12 received)
mininet> h1 ping -c 5 h3
PING 10.0.0.3 (10.0.0.3) 56(84) bytes of data.
64 bytes from 10.0.0.3: icmp_seq=1 ttl=64 time=0.606 ms
64 bytes from 10.0.0.3: icmp_seq=2 ttl=64 time=0.320 ms
64 bytes from 10.0.0.3: icmp_seq=3 ttl=64 time=0.129 ms
64 bytes from 10.0.0.3: icmp_seq=4 ttl=64 time=0.158 ms
64 bytes from 10.0.0.3: icmp_seq=5 ttl=64 time=0.119 ms

--- 10.0.0.3 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4102ms
rtt min/avg/max/mdev = 0.119/0.266/0.606/0.184 ms
mininet> h2 ping -c 5 h4
PING 10.0.0.4 (10.0.0.4) 56(84) bytes of data.
64 bytes from 10.0.0.4: icmp_seq=1 ttl=64 time=1.82 ms
64 bytes from 10.0.0.4: icmp_seq=2 ttl=64 time=0.274 ms
64 bytes from 10.0.0.4: icmp_seq=3 ttl=64 time=0.111 ms
64 bytes from 10.0.0.4: icmp_seq=4 ttl=64 time=0.131 ms
64 bytes from 10.0.0.4: icmp_seq=5 ttl=64 time=0.134 ms

--- 10.0.0.4 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4070ms
rtt min/avg/max/mdev = 0.111/0.494/1.822/0.666 ms
mininet> h3 iperf -s &
mininet> h1 iperf -c h3 -t 10
------------------------------------------------------------
Client connecting to 10.0.0.3, TCP port 5001
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.1 port 45632 connected with 10.0.0.3 port 5001
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-10.0091 sec  11.4 GBytes  9.78 Gbits/sec
mininet> 
```

# after deleting flows and restarting mininet to show regression test

```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> X X X 
h2 -> X X X 
h3 -> X X X 
h4 -> X X X 
*** Results: 100% dropped (0/12 received)
mininet> exit
*** Stopping 1 controllers
c0 
*** Stopping 6 links
......
*** Stopping 3 switches
s1 s2 s3 
*** Stopping 4 hosts
h1 h2 h3 h4 
*** Done
completed in 494.082 seconds
seed@seedvm2006:~/Documents/mininet$ sudo mn --custom topology/topo_orange.py --topo orange --controller remote,ip=127.0.0.1,port=6653 --switch ovsk,protocols=OpenFlow13
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 
*** Adding switches:
s1 s2 s3 
*** Adding links:
(h1, s1) (h2, s1) (h3, s2) (h4, s3) (s1, s2) (s1, s3) 
*** Configuring hosts
h1 h2 h3 h4 
*** Starting controller
c0 
*** Starting 3 switches
s1 s2 s3 ...
*** Starting CLI:
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 
h2 -> h1 h3 h4 
h3 -> h1 h2 h4 
h4 -> h1 h2 h3 
*** Results: 0% dropped (12/12 received)
mininet> 
```