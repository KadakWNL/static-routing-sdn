# SDN Mininet Mini Project - Orange Problem

## Project Title
Static Routing using SDN Controller

## Problem Statement
Implement static routing paths in an SDN network using Mininet and an OpenFlow controller (Ryu). The controller should install explicit match-action flow rules and demonstrate deterministic routing behavior.

## Objective
- Build a custom Mininet topology.
- Connect switches to a remote Ryu controller.
- Implement packet handling and flow-rule installation logic.
- Demonstrate functional correctness in live Mininet demo.
- Measure latency, throughput, and flow-table behavior.
- Perform regression/validation checks.

---

## Final Deliverables (As per Guidelines)

1. Working Demonstration
- Live demo in Mininet.
- Functional correctness.

2. Source Code on GitHub (Public)
- Final demo code.
- Clean and modular structure.
- Proper comments.

3. README Documentation on GitHub
- Problem statement.
- Setup and execution steps.
- Expected outputs.

4. Proof of Execution
- Screenshots or logs (Wireshark or equivalent tools allowed).
- Flow table snapshots.
- Ping and iperf outputs.

---

## Prerequisites
- Ubuntu VM (20.04 or 22.04 preferred)
- Sudo access
- Internet connectivity
- Python 3

Quick check:

```bash
lsb_release -a
python3 --version
```

---

## Installation

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install -y mininet openvswitch-switch python3-pip wireshark tshark iperf tcpdump net-tools
pip3 install ryu
```

If eventlet compatibility issue appears:

```bash
ryu-manager controller/static_routing_controller.py
```

---

## Project Structure

```text
static-routing-sdn/
  README.md
  controller/
    static_routing_controller.py
  topology/
    topo_orange.py
  results/
    logs/
    screenshots/
```

---

## Topology Used
- Hosts: h1, h2, h3, h4
- Switches: s1, s2, s3
- Host links:
  - h1 - s1
  - h2 - s1
  - h3 - s2
  - h4 - s3
- Inter-switch links:
  - s1 - s2
  - s1 - s3

Why this design:
- Clearly demonstrates static routing paths.
- Allows destination-based forwarding decisions.
- Easy to validate with flow tables.

---

## Controller Logic Summary
File: `controller/static_routing_controller.py`

The controller:
- Handles switch connection (`EventOFPSwitchFeatures`).
- Installs table-miss rule (priority 0 -> controller).
- Installs ARP flood rule (priority 10).
- Installs static IPv4 destination rules (priority 100).
- Logs PacketIn events for visibility and debugging.

---

## Setup and Execution Steps
Use 3 terminals.

## Terminal 1: Start Controller

```bash
ryu-manager controller/static_routing_controller.py
```

Expected:
- Controller app loads.
- Switch connect logs appear.

## Terminal 2: Start Mininet Topology

```bash
sudo mn -c
sudo mn --custom topology/topo_orange.py --topo orange --controller remote,ip=127.0.0.1,port=6653 --switch ovsk,protocols=OpenFlow13
```

## Terminal 2: Functional Tests in Mininet CLI

```bash
pingall
h1 ping -c 4 h3
h2 ping -c 4 h4
h3 iperf -s &
h1 iperf -c h3 -t 10
```

## Terminal 3: Flow Verification in Shell

```bash
sudo ovs-vsctl list-br
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
sudo ovs-ofctl -O OpenFlow13 dump-flows s2
sudo ovs-ofctl -O OpenFlow13 dump-flows s3
```

Important:
- Run `ovs-ofctl` in normal shell, not in Mininet prompt.

---

## Expected Output

### Connectivity
- `pingall` should show `0% dropped`.

### Latency
- First ping may have higher RTT due to ARP/initial setup.
- Subsequent packets should be lower and stable.

### Throughput
- `iperf` should show successful TCP transfer and bandwidth.

### Flow Tables
- Priority 100: static IPv4 destination rules.
- Priority 10: ARP flood.
- Priority 0: table-miss to controller.

Result note: Flow deletion caused failure; restart restored rules and connectivity (see [results/logs/mininet_logs.md](results/logs/mininet_logs.md), [results/logs/dump_flows.md](results/logs/dump_flows.md), and [results/logs/controller_logs.md](results/logs/controller_logs.md)).

---

## Test Scenarios

## Scenario A: Functional Correctness
Commands:

```bash
pingall
h1 ping -c 4 h3
h2 ping -c 4 h4
```

Pass condition:
- End-to-end connectivity successful.

## Scenario B: Regression by Restart
Commands:

```bash
# In Mininet
exit

# In shell
sudo mn -c
sudo mn --custom topology/topo_orange.py --topo orange --controller remote,ip=127.0.0.1,port=6653 --switch ovsk,protocols=OpenFlow13
```

Then rerun (Note restart the controller):

```bash
pingall
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```

Pass condition:
- Connectivity and intended flow behavior remain consistent.

## Scenario C: Advanced Regression by Flow Deletion (Optional)
Delete IPv4 forwarding entries:

```bash
sudo ovs-ofctl -O OpenFlow13 del-flows s1 "ip"
sudo ovs-ofctl -O OpenFlow13 del-flows s2 "ip"
sudo ovs-ofctl -O OpenFlow13 del-flows s3 "ip"
```

Verify deletion:

```bash
sudo ovs-ofctl -O OpenFlow13 dump-flows s1 | grep "priority=100"
sudo ovs-ofctl -O OpenFlow13 dump-flows s2 | grep "priority=100"
sudo ovs-ofctl -O OpenFlow13 dump-flows s3 | grep "priority=100"
```

Observation:
- If static rules are removed and not auto-reinstalled, forwarding may fail until reconnect/restart.

---

## Performance Observation and Analysis

Latency:

```bash
h1 ping -c 5 h3
```

Throughput:

```bash
h3 iperf -s &
h1 iperf -c h3 -t 10
```

Flow counters:

```bash
sudo ovs-ofctl -O OpenFlow13 dump-flows s1
```

---

## Proof of Execution Artifacts
Logs are stored in `results/logs/` and screenshots are stored in `results/screenshots/`.

Current screenshots in `results/screenshots/`:
- `controller_running.png`
- `mn_pingall_ping.png`
- `mn_ping_iperf.png`
- `flow_initial_del.png`
- `flow_reappear_reg.png`
- `mn_regression_test.png`

---

<!-- ## Proof of Execution Checklist
Save under `results/screenshots` and `results/logs`:
- Controller startup and switch-connect logs.
- `pingall` output.
- Targeted ping output.
- iperf output.
- Flow table dumps for s1/s2/s3.
- Regression run evidence before/after restart. -->

<!-- ## Troubleshooting

`mn: command not found`

```bash
sudo apt install mininet -y
```

`ryu-manager: command not found`

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

`ovs-ofctl: switch is not a bridge or socket`
- Mininet is not currently running, or switch was removed after `exit`.

Controller terminates unexpectedly
- Avoid running `sudo mn -c` after controller startup in same sequence.

-->
