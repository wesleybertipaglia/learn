# Network Addressing

Addressing is essential for communication in computer networks, allowing devices to locate and communicate with each other. There are several types of addressing, depending on the layer of the network model in which they operate.

## 1. IP Addressing

### IPv4 (Internet Protocol version 4)

- **Format**: 32-bit addresses, represented as four octets in dotted decimal notation (e.g. 192.168.1.1).
- **Division**:
- **Network Address**: Identifies the network to which a device belongs.
- **Host Address**: Identifies a specific device within the network.
- **Subnet Mask**: Defines the division between the network address and the host address (e.g. 255.255.255.0).

### IPv6 (Internet Protocol version 6)

- **Format**: 128-bit addresses, represented as eight groups of four hexadecimal digits separated by colons (e.g. 2001:db8::1).
- **Benefits**: Larger address space, better support for mobility, and integrated security.
- **Prefixes**: Used to identify the network portion of the address.

## 2. MAC (Media Access Control) Addressing

- **Format**: 48-bit addresses, typically represented as six pairs of hexadecimal digits separated by colons or hyphens (e.g. 00:1A:2B:3C:4D:5E).
- **Function**: Uniquely identifies a device at the data link layer (layer 2 of the OSI model).
- **Assignment**: Typically assigned by the hardware manufacturer and is unique to each network device.

## 3. Network Addressing

### CIDR (Classless Inter-Domain Routing)

- **Function**: Allows for more flexible allocation of IP addresses, replacing the old class system (Class A, B, C).
- **Format**: Represents the subnet mask as a suffix after the IP address (e.g. 192.168.1.0/24).
- **Benefits**: Improves the efficiency of IP address usage and facilitates routing.

## 4. NAT (Network Address Translation)

- **Function**: Allows multiple devices on a local network to share a single public IP address.
- **Types**:
- **Static NAT**: Fixed mapping between an internal and an external IP address.
- **Dynamic NAT**: Maps internal addresses to a pool of available external addresses.
- **PAT (Port Address Translation)**: A type of NAT that uses different ports to distinguish simultaneous connections (also known as overloaded NAT).

## 5. DHCP (Dynamic Host Configuration Protocol)

- **Function**: Automatically assigns IP addresses and other network settings to devices on a network.
- **Process**:
- **Discovery**: The DHCP client sends a discovery request.
- **Offer**: The DHCP server responds with a configuration offer.
- **Request**: The client requests the offered configuration.
- **Confirmation**: The server confirms the configuration to the client.

## 6. DNS (Domain Name System)

- **Function**: Translates human-readable domain names into IP addresses that can be used to locate devices on the network.
- **Components**:
- **Name Resolution**: The process of finding the IP address associated with a domain name. - **DNS Servers**: These include authoritative name servers and recursive resolution servers.

## 7. Subnet Addressing

- **Function**: Divide a larger network into smaller networks to improve organization and efficiency.
- **Subnet Mask**: Defines the size of the subnet and the portion of the IP address dedicated to the network and hosts.
- **Example**: A subnet mask of 255.255.255.0 divides a network into subnets with 254 possible host addresses.

---

- [Previous](./4-protocols.md)
- [Next](./6-security.md)