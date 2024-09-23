# TCP/IP Model

The TCP/IP Model is a network architecture that serves as the basis for the Internet and private networks. It consists of four layers, each with specific responsibilities for ensuring communication between systems.

## 1. Application Layer

- **Function**: Provides network interfaces and services for user applications. This is where application communication protocols operate.
- **Protocols and Technologies**: HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), SMTP (Simple Mail Transfer Protocol), DNS (Domain Name System).
- **Examples**: Web browsers, email clients, file transfer applications.

## 2. Transport Layer

- **Function**: Ensures reliable or unreliable delivery of data between applications. Controls end-to-end communication and can offer guarantees of delivery and packet order.
- **Protocols and Technologies**: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
- **Examples**: Establishing TCP connections, flow control and packet retransmission to ensure delivery, communication via UDP for streaming services and games.

## 3. Internet Layer

- **Function**: Deals with addressing and routing data packets between different networks. Ensures that packets are forwarded from source to destination across multiple networks.
- **Protocols and Technologies**: IP (Internet Protocol), ICMP (Internet Control Message Protocol), IGMP (Internet Group Management Protocol).
- **Examples**: IP addressing (IPv4 and IPv6), routers, error message control protocols.

## 4. Network Interface Layer (or Network Access Layer)

- **Function**: Deals with data transmission between the device and the physical network medium. It is responsible for placing and removing packets on the physical transmission medium. - **Protocols and Technologies**: Ethernet, Wi-Fi, PPP (Point-to-Point Protocol), ARP (Address Resolution Protocol).
- **Examples**: Transmission of Ethernet frames, configuration of wireless network interfaces, physical medium access protocols.

---

- [Previous](./4-osi.md)
- [Next](./6-protocols.md)
