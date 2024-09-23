# Networking Fundamentals

A computer network is a system that allows multiple devices to communicate with each other, making it easier to share information and resources. Networks consist of physical and digital components that work together to keep these devices connected.

## 1. Network Basics

Key concepts in networking include:

- **Data Transmission**: Data moves between devices in packets, which are small units of data.
- **Bandwidth**: The amount of data that can be transmitted in a given time.
- **Latency**: The time it takes for data to travel from one point to another.
- **Protocols**: Rules that devices follow to communicate.
- **Client-Server Model**: Devices can act as clients (requesting data) or servers (providing data).
- **Peer-to-Peer Model**: Devices can communicate directly with each other without a central server.
- **Internet**: A global network of networks that allows devices to connect worldwide.

## 2. Network Classification

Networks can be categorized in different ways based on their characteristics:

- **Size**: Local (LAN), city-wide (MAN), or even global (WAN). Personal networks (PAN) are for individual use.
- **Connection Method**: Devices can connect via cables (Wired) or through radio signals (Wireless).
- **Ownership**: A network may be owned privately or publicly.
- **Scope**: Networks can operate internally (Intranet), externally for specific partners (Extranet), or globally (Internet).
- **Topology**: The layout of a network’s connections can take different shapes like Star, Bus, Ring, or Mesh.

## 3. Network Devices

Different devices help networks function smoothly, each performing a specific role:

- **Routers**: Help data travel between different networks.
- **Switches**: Connect devices within the same network and direct data based on device addresses.
- **Hubs**: Basic devices that connect multiple devices by sending data to all of them at once.
- **Modems**: Translate data between your home network and the internet.
- **Access Points**: Allow wireless devices to connect to a wired network.
- **Firewalls**: Protect the network by controlling what data can enter or leave.
- **Servers**: Provide services like file storage, email, or website hosting.

## 4. Reference Models

Reference models explain how networks work by breaking them into layers. The most common are the OSI and TCP/IP models.

### OSI Model

This model has seven layers that describe how data moves from one device to another:

1. **Physical Layer**: Transmits raw data (bits) across physical connections.
2. **Link Layer**: Ensures data is properly formatted and handles errors.
3. **Network Layer**: Finds the best path for data to travel.
4. **Transport Layer**: Manages reliable data transfer.
5. **Session Layer**: Manages and maintains communication between devices.
6. **Presentation Layer**: Translates data formats and encrypts information.
7. **Application Layer**: Directly interacts with the user’s software, such as email or web browsers.

### TCP/IP Model

This model focuses on fewer layers, specifically on the communication between different networks:

1. **Application Layer**: Handles network services like web browsing and email.
2. **Transport Layer**: Ensures data delivery using protocols like TCP and UDP.
3. **Internet Layer**: Routes data between devices using the IP protocol.
4. **Network Interface Layer**: Controls how data is transmitted on the physical network.

## 5. Network Protocols

Network protocols are rules that devices follow to communicate. Some common protocols include:

- **IP (Internet Protocol)**: Routes data to the correct device.
- **TCP (Transmission Control Protocol)**: Ensures data is sent and received in order.
- **UDP (User Datagram Protocol)**: Sends data quickly but without confirmation of delivery.
- **HTTP (Hypertext Transfer Protocol)**: Transfers web pages.
- **FTP (File Transfer Protocol)**: Moves files between devices.
- **SMTP (Simple Mail Transfer Protocol)**: Sends email messages.
- **IMAP (Internet Message Access Protocol)**: Accesses emails stored on servers.
- **POP3 (Post Office Protocol)**: Downloads emails to a local device.

## 6. Addressing

Every device on a network has a unique address to identify it. Common addressing methods include:

- **IP Addresses**: Identify devices on a network. IPv4 (e.g., 192.168.1.1) or IPv6 (e.g., 2001:db8::1).
- **MAC Addresses**: Unique identifiers for devices within a local network.
- **Subnet Masks**: Separate the network part of an IP address from the device part.
- **NAT (Network Address Translation)**: Allows multiple devices to share a single public IP address.

## 7. Network Security

Securing a network means protecting it from unauthorized access and potential threats. Key security measures include:

- **Firewalls**: Control what data can enter and leave the network.
- **Encryption**: Secures data so only authorized users can access it.
- **Authentication and Authorization**: Ensures only the right users have access to network resources.
- **Intrusion Detection Systems (IDS)**: Detect suspicious activity or potential attacks.
- **Virtual Private Networks (VPNs)**: Create secure, encrypted connections for remote users.
- **Antivirus Software**: Protects devices from malicious software.

## 8. Network Monitoring

Monitoring a network helps keep it running smoothly by checking its performance and security. Some common monitoring tools include:

- **Ping**: Tests if a device can be reached.
- **Traceroute**: Shows the path data takes across the network.
- **SNMP (Simple Network Management Protocol)**: Collects data to monitor network health.
- **NetFlow**: Analyzes network traffic to identify issues.
- **Packet Sniffing**: Captures and analyzes network traffic to troubleshoot problems.
- **Syslog**: Collects logs from network devices to track events.
- **Network Performance Monitoring**: Measures things like speed, delay, and data loss.

## 9. Network Management

Managing a network involves maintaining and optimizing its performance. Key tasks include:

- **Configuration Management**: Keeping devices up-to-date and correctly configured.
- **Performance Management**: Monitoring and improving network speed and reliability.
- **Fault Management**: Detecting and fixing problems quickly.
- **Security Management**: Ensuring the network is protected from threats.
- **Accounting Management**: Tracking resource usage and costs.
- **Change Management**: Planning and implementing changes in the network.
- **Inventory Management**: Keeping track of all devices and resources on the network.

---

- [Next](./2-classification.md)
