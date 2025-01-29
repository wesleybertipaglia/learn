# Networking in Linux

Network management in Linux involves configuring interfaces, monitoring traffic, and diagnosing network problems. Here are some essential concepts and commands:

## Basic Concepts

- **Network Interface**: A device or software that allows communication between a computer and a network. Examples include `eth0` for Ethernet and `wlan0` for Wi-Fi.
- **IP (Internet Protocol)**: A protocol that provides addresses to identify devices on a network.
- **Subnet Mask**: Defines the network and hosts within an IP network.
- **Gateway**: A device that connects a network to other networks, including the Internet.

## Important Commands

### Interface Configuration

- `ip`: A modern tool for configuring and displaying information about network interfaces. - Display all interfaces and their IP addresses:
```bash
ip addr show
```
- Configure an IP address on an interface:
```bash
ip addr add 192.168.1.10/24 dev eth0
```
- Enable or disable an interface:
```bash
ip link set eth0 up
ip link set eth0 down
```

- `ifconfig`: Older tool for configuring and displaying interface information. - Display information about interfaces:
```bash
ifconfig
```
- Configure an IP address on an interface:
```bash
ifconfig eth0 192.168.1.10 netmask 255.255.255.0
```
- Enable or disable an interface:
```bash
ifconfig eth0 up
ifconfig eth0 down
```

### Network Diagnostics

- `ping`: Tests connectivity to another device on the network.
```bash
ping 8.8.8.8
```

- `traceroute`: Shows the path that packets follow to reach a destination.
``bash
traceroute www.google.com
```

- **`netstat`**: Displays information about network connections, routing tables, and statistics.
- Display network connections:
```bash
netstat -tuln
```
- Display routing table:
```bash
netstat -r
```

- `ss`: Modern tool to display information about network connections, replacing `netstat`.
- Display network connections:
```bash
ss -tuln
```

### Routing Configuration

- `route`: Displays or modifies the routing table. - Display the routing table:
```bash
route -n
```
- Add a static route:
```bash
route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
```
- Remove a route:
```bash
route del -net 192.168.1.0
```

- `ip route`: Modern tool for configuring routes. - Display the routing table:
```bash
ip route show
```
- Add a route:
```bash
ip route add 192.168.1.0/24 via 192.168.1.1
```
- Remove a route:
```bash
ip route del 192.168.1.0/24
```

### Configuration Files

- **/etc/network/interfaces**: Traditional file used in many distributions to configure network interfaces (mainly in Debian and derivatives).
- **/etc/sysconfig/network-scripts/ifcfg-<interface>**: File used in Red Hat-based distributions (such as CentOS and Fedora) to configure interfaces.
- **/etc/netplan/**: Directory used in newer Ubuntu-based distributions for network configuration.

### Monitoring Tools

- `tcpdump`: Captures and displays network packets.

```bash
tcpdump -i eth0
```

- `wireshark`: Graphical tool for detailed analysis of network packets (requires installation).

---

- [Previous](./7-processes.md)
- [Next](./9-security.md)

