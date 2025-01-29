# Network Protocols

Network protocols are standardized rules that allow devices to communicate and share data over a network. Below is an overview of these protocols, grouped by their primary purposes.

## 1. Communication Protocols
Protocols that govern the exchange of data between devices.

### Transmission Control Protocol (TCP)
- **Function**: Ensures reliable data transmission.
- **Key Features**:
  - Establishes a connection before data transfer.
  - Guarantees data delivery and order.
  - Provides error-checking and retransmission.

### User Datagram Protocol (UDP)
- **Function**: Allows fast, connectionless communication.
- **Key Features**:
  - No connection establishment.
  - Lower overhead than TCP.
  - Suitable for real-time applications (e.g., streaming).

## 2. Network Layer Protocols
Protocols that facilitate the routing of data across different networks.

### Internet Protocol (IP)
- **Function**: Addresses and routes packets between devices.
- **Key Features**:
  - IP Version 4 (IPv4) and IP Version 6 (IPv6) are the most common.
  - Handles packet fragmentation and reassembly.
  - Provides logical addressing (IP addresses).

### Internet Control Message Protocol (ICMP)
- **Function**: Provides error messages and operational information.
- **Key Features**:
  - Used for diagnostics (e.g., ping and traceroute).
  - Helps with network troubleshooting.

## 3. Application Layer Protocols
Protocols that support specific applications and services.

### Hypertext Transfer Protocol (HTTP)
- **Function**: Governs the transfer of web pages.
- **Key Features**:
  - Forms the foundation of data communication on the web.
  - Works with secure version (HTTPS) for encrypted communication.

### Hypertext Transfer Protocol Secure (HTTPS)
- **Function**: Secures web communication using encryption.
- **Key Features**:
  - Encrypts data transmitted between the client and server.
  - Uses SSL/TLS for secure connections.

### File Transfer Protocol (FTP)
- **Function**: Facilitates the transfer of files between devices.
- **Key Features**:
  - Allows uploading and downloading files.
  - Supports authentication and multiple file types.

### Simple Mail Transfer Protocol (SMTP)
- **Function**: Handles the sending of emails.
- **Key Features**:
  - Operates primarily for sending messages.
  - Works with other protocols (e.g., POP3, IMAP) for receiving.

### Internet Message Access Protocol (IMAP)
- **Function**: Retrieves emails from a mail server.
- **Key Features**:
  - Allows users to access emails stored on servers.
  - Supports multiple devices accessing the same mailbox.

### Post Office Protocol (POP3)
- **Function**: Downloads emails to a local device.
- **Key Features**:
  - Retrieves emails from a mail server.
  - Typically deletes messages from the server after download.

## 4. Network Management Protocols
Protocols used for monitoring and managing network devices.

### Simple Network Management Protocol (SNMP)
- **Function**: Monitors and manages network devices.
- **Key Features**:
  - Gathers performance data and alerts administrators.
  - Supports remote management of devices.

### Network Time Protocol (NTP)
- **Function**: Synchronizes clocks of networked devices.
- **Key Features**:
  - Ensures accurate timekeeping across devices.
  - Important for logging and transaction accuracy.

## 5. Security Protocols
Protocols that provide secure communication over a network.

### Secure Sockets Layer (SSL) / Transport Layer Security (TLS)
- **Function**: Secures data transmitted over networks.
- **Key Features**:
  - Provides encryption for data in transit.
  - Ensures integrity and authentication.

### Internet Protocol Security (IPsec)
- **Function**: Secures Internet Protocol communications.
- **Key Features**:
  - Operates at the network layer.
  - Provides encryption and authentication for IP packets.

---

- [Previous](./5-tcp.md)
- [Next](./7-addressing.md)
