# Network Addressing

Addressing is essential for communication in computer networks, allowing devices to locate and communicate with each other. There are several types of addressing, depending on the layer of the network model in which they operate.

## 1. MAC (Media Access Control) Addressing

- **Format**: 48-bit addresses, typically represented as six pairs of hexadecimal digits separated by colons or hyphens (e.g., `00:1A:2B:3C:4D:5E`).
- **Function**: Uniquely identifies a device at the data link layer (Layer 2 of the OSI model).
- **Assignment**: Assigned by the hardware manufacturer, ensuring that each network device has a unique MAC address.

## 2. IP Addressing

### IPv4 (Internet Protocol version 4)

- **Format**: 32-bit addresses, represented as four octets in dotted decimal notation (e.g., `192.168.1.1`).
- **Components**:
  - **Network Address**: Identifies the network to which a device belongs.
  - **Host Address**: Identifies a specific device within that network.
  - **Subnet Mask**: Defines the division between the network address and the host address (e.g., `255.255.255.0`).

### IPv6 (Internet Protocol version 6)

- **Format**: 128-bit addresses, represented as eight groups of four hexadecimal digits separated by colons (e.g., `2001:db8::1`).
- **Benefits**: Offers a larger address space, better support for mobility, and enhanced security features.
- **Prefixes**: Indicate the network portion of the address.

### DHCP (Dynamic Host Configuration Protocol)

- **Function**: Automatically assigns IP addresses and other network settings to devices on a network.
- **Process**:
  - **Discovery**: The DHCP client sends a discovery request to locate a DHCP server.
  - **Offer**: The DHCP server responds with an available configuration offer.
  - **Request**: The client requests the offered configuration.
  - **Confirmation**: The server confirms the configuration to the client.

## 3. Network Addressing

### CIDR (Classless Inter-Domain Routing)

- **Function**: Allows for flexible allocation of IP addresses, replacing the traditional class system (Class A, B, C).
- **Format**: Represents the subnet mask as a suffix after the IP address (e.g., `192.168.1.0/24`).
- **Benefits**: Improves the efficiency of IP address usage and facilitates better routing.

## 4. NAT (Network Address Translation)

- **Function**: Allows multiple devices on a local network to share a single public IP address.
- **Types**:
  - **Static NAT**: Fixed mapping between an internal and an external IP address.
  - **Dynamic NAT**: Maps internal addresses to a pool of available external addresses.
  - **PAT (Port Address Translation)**: A type of NAT that distinguishes simultaneous connections by using different ports (also known as overloaded NAT).

## 5. Subnet Addressing

- **Function**: Divides a larger network into smaller, manageable subnets to improve organization and efficiency.
- **Subnet Mask**: Defines the size of the subnet and indicates which portion of the IP address is dedicated to the network and which is dedicated to hosts.
- **Example**: A subnet mask of `255.255.255.0` allows for 256 addresses (254 usable for hosts) within that subnet.

## 6. DNS (Domain Name System)

- **Function**: Translates human-readable domain names into IP addresses, enabling the location of devices on a network.
- **Components**:
  - **Name Resolution**: The process of finding the IP address associated with a domain name.
  - **DNS Servers**: Include authoritative name servers (which provide answers for specific domains) and recursive resolution servers (which query other servers to resolve names).

---

- [Previous](./6-protocols.md)
- [Next](./8-security.md)