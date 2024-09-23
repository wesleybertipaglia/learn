# OSI (Open Systems Interconnection) Model

The OSI Model is a reference model for computer networks that divides network communication into 7 distinct layers. Each layer has a specific function and interacts with the layers above and below it to ensure efficient communication.

## 1. Physical Layer

- **Function**: Transmission of bits through the physical medium.
- **Protocols and Technologies**: Ethernet, fiber optic cables, electrical signals, connectors.
- **Examples**: Cable connections, signal voltages, physical characteristics of transmission media.

## 2. Data Link Layer

- **Function**: Transmission of frames and physical layer error control. Manages communication between devices on the same network.
- **Protocols and Technologies**: Ethernet, PPP (Point-to-Point Protocol), ARP (Address Resolution Protocol).
- **Examples**: Error detection and correction, medium access control (MAC), physical addressing (MAC addresses).

## 3. Network Layer

- **Function**: Packet routing and logical addressing. Determines the path that packets should follow in the network.
- **Protocols and Technologies**: IP (Internet Protocol), ICMP (Internet Control Message Protocol).
- **Examples**: IP addressing, routers, routing path selection.

## 4. Transport Layer

- **Function**: Flow and error control, and reliable (or unreliable) data transport. Ensures correct and ordered delivery of data.
- **Protocols and Technologies**: TCP (Transmission Control Protocol), UDP (User Datagram Protocol).
- **Examples**: Packet retransmission control, data segmentation and reassembly.

## 5. Session Layer

- **Function**: Establishing, maintaining, and terminating communication sessions between applications. Coordinates dialogue between systems.
- **Protocols and Technologies**: NetBIOS, RPC (Remote Procedure Call).
- **Examples**: Controlling communication sessions, synchronizing dialogue.

## 6. Presentation Layer

- **Function**: Translating, formatting, and encrypting data. Ensures that data is presented in a way that the application layer understands.
- **Protocols and Technologies**: SSL/TLS (for encryption), data formats such as JPEG, MPEG.
- **Examples**: Data compression, format conversion, encryption, and decryption.

## 7. Application Layer

- **Function**: Interface between applications and the network. Provides network services for user applications. - **Protocols and Technologies**: HTTP (Hypertext Transfer Protocol), FTP (File Transfer Protocol), SMTP (Simple Mail Transfer Protocol).
- **Examples**: Web browsers, email clients, file transfer services.

---

- [Previous](./3-devices.md)
- [Next](./5-tcp.md)
