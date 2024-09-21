# Networking Fundamentals

## 1. Introduction to Networks

Computer networks allow communication between devices, facilitating the sharing of resources and data. They are formed by a combination of hardware and software that connect devices and services.

## 2. Types of Networks

- **LAN (Local Area Network)**: Local network that covers a geographically restricted area, such as a home or office.
- **WAN (Wide Area Network)**: Network that covers a large geographical area, such as cities or countries.
- **MAN (Metropolitan Area Network)**: Network that covers an area larger than a LAN, but smaller than a WAN, such as a city.
- **PAN (Personal Area Network)**: Short-range network used to connect personal devices, such as smartphones and tablets.

## 3. Network Topologies

- **Star**: All devices are connected to a central point.
- **Bus**: Devices are connected to a single central cable. - **Ring**: Each device is connected to two others, forming a ring.
- **Mesh**: Each device is connected to several others, offering redundancy.

## 4. Network Devices

- **Routers**: Forward packets between different networks.
- **Switches**: Connect devices within the same network and forward packets based on MAC addresses.
- **Hubs**: Simple devices that connect several devices, transmitting data to all connected devices.
- **Modems**: Convert digital signals to analog and vice versa, allowing connection to the Internet.

## 5. Reference Models

- **OSI (Open Systems Interconnection) Model**: Divided into 7 layers:
1. **Physical Layer**: Transmission of bits through the physical medium.
2. **Link Layer**: Transmission of frames and error detection. 3. **Network Layer**: Packet routing and logical addressing.
4. **Transport Layer**: Flow and error control, data transport.
5. **Session Layer**: Establishment and control of communication sessions.
6. **Presentation Layer**: Data translation and encryption.
7. **Application Layer**: Network interfaces and services for applications.

- **TCP/IP model**: Fewer layers, focused on specific protocols:
1. **Application Layer**: Application protocols such as HTTP, FTP.
2. **Transport Layer**: Protocols such as TCP and UDP.
3. **Internet Layer**: IP protocol, packet routing.
4. **Network Interface Layer**: Control access to the physical medium.

## 6. Communication Protocols

- **IP (Internet Protocol)**: Responsible for addressing and routing packets on the network.
- **TCP (Transmission Control Protocol)**: Ensures the correct and ordered delivery of packets.
- **UDP (User Datagram Protocol)**: Connectionless protocol, used for fast transmissions.
- **HTTP (Hypertext Transfer Protocol)**: Used for web data transfer.
- **FTP (File Transfer Protocol)**: Used for file transfer.
- **SMTP (Simple Mail Transfer Protocol)**: Used for sending e-mails.
- **IMAP (Internet Message Access Protocol)**: Used to access e-mails on servers.
- **POP3 (Post Office Protocol)**: Used to download e-mails from the server.

## 7. Addressing

- **IP Addresses**: Identify devices on a network. They can be IPv4 (e.g. 192.168.1.1) or IPv6 (e.g. 2001:db8::1).
- **MAC Addresses**: Identify devices on a local network. They are unique to each device.
- **Subnet Masks**: Define the division between the network portion and the host portion of the IP address.
- **NAT (Network Address Translation)**: Allows multiple devices to communicate using a single public IP address.

### Addressing Protocols

- **DHCP (Dynamic Host Configuration Protocol)**: Automatically assigns IP addresses to devices on the network.
- **DNS (Domain Name System)**: Translates domain names into IP addresses.
- **ARP (Address Resolution Protocol)**: Maps IP addresses to MAC addresses.

## 8. Network Security

- **Firewalls**: Monitor and control network traffic to protect against unauthorized access.
- **Encryption**: Protect data during transmission, ensuring that only authorized recipients can access the information.
- **Authentication and Authorization**: Ensure that only authorized users have access to network resources.

## 9. Monitoring and Management

- **SNMP (Simple Network Management Protocol)**: Protocol for monitoring and managing network devices.
- **Traffic Analysis**: Tools and techniques for monitoring performance and diagnosing network problems.

---

- [Next](./2-osi.md)