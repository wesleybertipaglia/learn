# Network Administration

## 1. Network Monitoring
**Network monitoring** is the process of observing and analyzing the activity and performance of a network to ensure that it is operating efficiently and securely. It helps identify performance issues, failures, bottlenecks, and security threats.

### 1.1. Monitoring Tools
Monitoring tools are used to collect and analyze network performance data.
- **Nagios**: Monitors servers, switches, and routers, alerting you to failures and bottlenecks.
- **Zabbix**: Provides real-time performance monitoring of networks, servers, and applications.
- **Wireshark**: A packet analysis tool that captures and inspects network traffic.
- **Prometheus + Grafana**: Monitors network metrics with data visualization in dashboards.

### 1.2. Common Monitoring Metrics
- **Bandwidth**: Volume of data transmitted per unit of time.
- **Latency**: Time it takes for a packet to travel from one point to another on the network.
- **Packet Loss**: Percentage of data packets that are discarded during transmission.
- **Error Rate**: Percentage of packets that are corrupted or lost during transmission.

## 2. IPsec (Internet Protocol Security)
**IPsec** is a suite of protocols that provide authentication, integrity, and encryption of data in point-to-point communications at the network layer (layer 3 - IP). It is primarily used in **VPNs** and to secure communications on the Internet.

### 2.1. IPsec Components
- **AH (Authentication Header)**: Provides packet integrity authentication.
- **ESP (Encapsulating Security Payload)**: Provides confidentiality (encryption), integrity, and packet authentication.
- **SA (Security Association)**: Defines the security parameters (algorithms, keys) used to protect communication.
- **IKE (Internet Key Exchange)**: Protocol used to negotiate security keys and establish SAs.

### 2.2. Operation Modes
- **Transport Mode**: Only the payload (data) of the IP packet is encrypted, maintaining the original IP header.
- **Tunnel Mode**: The entire packet (header and payload) is encrypted and encapsulated in a new IP packet.

### 2.3. IPsec Applications
- **Corporate VPNs**: Protect communication between remote networks.
- **Internet Data Protection**: Provides security for communications over insecure networks.

## 3. BGP (Border Gateway Protocol)
**BGP** is the routing protocol used to exchange routing information between autonomous networks on the Internet (AS - Autonomous Systems). It is crucial to ensure global connectivity between different service providers.

### 3.1. How BGP Works
BGP decides which path data should follow to reach a destination, based on rules and policies defined by administrators. It uses **autonomous systems** to route traffic between different networks.

### 3.2. Types of BGP
- **IBGP (Internal BGP)**: Used within the same autonomous system.
- **EBGP (External BGP)**: Used for communication between different autonomous systems.

### 3.3. Risks and Considerations
- **Security**: Attacks such as "prefix hijacking" can redirect traffic to malicious networks.
- **Slow convergence**: BGP can take a while to adjust to changes in the network, especially on a large scale.
- **Routing Policies**: BGP allows you to configure complex routing policies, but this requires careful planning.

### 3.4. Using BGP
- **Internet Service Providers**: Manage routing between ISPs and ensure that traffic follows optimized paths.
- **Large Enterprises**: Connect different offices or data centers via multiple routes.

## 4. VPN (Virtual Private Network)
**VPN** creates a secure, encrypted connection between two or more devices over a public or private network, such as the Internet. It is widely used for secure remote access and for connecting different networks.

### 4.1. Types of VPN
- **Site-to-Site VPN**: Connects local area networks (LANs) in different locations via the Internet. Used by companies to connect branch offices.
- **Remote Access VPN (Client-to-Site)**: Allows remote users to securely connect to the corporate network. - **SSL VPNs**: Uses the SSL/TLS protocol to create a secure tunnel through web browsers.

### 4.2. Common VPN Protocols
- **OpenVPN**: One of the most widely used, it offers high security and flexibility.
- **L2TP/IPsec**: Combines the L2TP protocol for tunneling with IPsec for security.
- **PPTP (Point-to-Point Tunneling Protocol)**: Simple, but less secure compared to other protocols.

### 4.3. VPN Applications
- **Secure Remote Access**: Users can access corporate resources from anywhere.
- **Internet Privacy**: VPNs are used to hide IP addresses and encrypt Internet traffic.
- **Branch Office Connection**: Companies can connect remote offices
securely.

## 5. Load Balancing
**Load Balancing** distributes network traffic across multiple servers or resources to ensure availability, performance, and redundancy. It helps prevent overloading of individual servers and improves system response time.

### 5.1. Types of Load Balancing
- **Network Load Balancing (L3/L4)**: Works at the network or transport layer, redirecting traffic based on IP address and port.
- **Application Load Balancing (L7)**: Works at the application layer, redirecting traffic based on packet content (e.g., HTTP headers).

### 5.2. Common Distribution Algorithms
- **Round Robin**: Traffic is distributed equally among servers in a cyclical fashion.
- **Least Connections**: Traffic is sent to the server with the fewest active connections. - **Hashing**: Uses a hash value (such as the client IP) to decide which server will receive the connection.

### 5.3. Load Balancing Tools
- **Nginx**: A popular web server that also offers load balancing capabilities.
- **HAProxy**: A widely used software for high-performance load balancing.
- **AWS Elastic Load Balancer (ELB)**: A managed load balancing service in Amazon Web Services cloud environments.

### 5.4. Advantages of Load Balancing
- **High availability**: Ensures that the service continues to function, even if a server fails.
- **Scalability**: Makes it easier to add more servers as demand increases.
- **Improved performance**: Reduces response time by distributing the load efficiently.

---

- [Previous](./7-monitoring.md)