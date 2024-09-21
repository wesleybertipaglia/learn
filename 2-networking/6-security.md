# Network Security

Network security is crucial to protect data and systems against unauthorized access, attacks and threats. It involves a combination of practices, protocols and tools to ensure data integrity, confidentiality and availability.

## 1. Information Security Triad

Information security is based on the security triad, which consists of three fundamental principles:

### Confidentiality

- **Objective**: Ensure that only authorized users can access sensitive data.
- **Methods**:
- **Encryption**: Encrypts data so that only authorized recipients can decrypt it.
- **Symmetric Encryption**: Uses the same key to encrypt and decrypt (e.g. AES, DES).
- **Asymmetric Encryption**: Uses public and private key pairs (e.g. RSA, ECC).
- **Access Control**: Defines who can access which resources and at what level. - **Authentication**: Verifies the identity of users (e.g., passwords, biometrics).
- **Authorization**: Controls access to resources based on the user's identity.

### Integrity

- **Purpose**: Ensures that data is not altered or corrupted during transmission or storage.
- **Methods**:
- **Hashing**: Uses hash functions to create a digest of the data, allowing verification of whether it has been altered (e.g., MD5, SHA-256).
- **Digital Signatures**: Uses cryptography to verify the authenticity and integrity of a message or document.

### Availability

- **Purpose**: Ensures that data and services are accessible when needed.
- **Methods**:
- **Redundancy**: Implements redundant systems and backups to prevent data loss. - **Distributed Denial of Service (DDoS) Protection**: Uses techniques to mitigate attacks that aim to overload and take down services.

## 2. Authentication and Authorization

- **Authentication**: Process of verifying the identity of the user or device.
- **Methods**: Passwords, two-factor authentication (2FA), biometrics (fingerprints, facial recognition).
- **Protocols**:
- **LDAP (Lightweight Directory Access Protocol)**: Used to query and modify user directories.
- **Kerberos**: Authentication protocol that uses tickets to allow secure access.

- **Authorization**: Process of defining permissions and rights to access specific resources.
- **Templates**:
- **RBAC (Role-Based Access Control)**: Assigns permissions based on user roles. - **ABAC (Attribute-Based Access Control)**: Sets permissions based on user, resource, and environment attributes.

## 3. Threat Protection

- **Firewall**: Monitors and controls network traffic based on security rules.

- **Types**: Network firewalls (between networks) and host firewalls (on individual devices).

- **Antivirus and Antimalware**: Detects and removes malicious software such as viruses, worms, and spyware.

- **Regular Updates**: Keeps software up to date to protect against new threats.

- **Intrusion Detection and Prevention Systems (IDS/IPS)**: Monitors and analyzes traffic to detect and prevent suspicious activity.

- **IDS (Intrusion Detection System)**: Detects and alerts you to potential threats.

- **IPS (Intrusion Prevention System)**: In addition to detecting, it also blocks suspicious activity.

## 4. Layered Security

- **Concept**: Implement multiple layers of security to protect against a variety of threats.

- **Examples**: Use firewalls, encryption, antivirus, and access control together to create a comprehensive defense.

## 5. Security Policies and Procedures

- **Security Policies**: Documents that define rules and guidelines for protecting information and systems.

- **Examples**: Acceptable use policies, password policies, incident response policies.

- **Incident Response Procedures**: Plans and actions for dealing with security events, such as data breaches or cyberattacks.

## 6. Physical Security

- **Purpose**: Protect network devices and infrastructure from unauthorized physical access and damage.

- **Methods**:

- **Physical Access Control**: Use of access cards, biometrics, and security in restricted areas. - **Controlled Environments**: Keep servers and equipment in safe rooms with temperature and humidity control.

---

- [Previous](./5-address.md)
- [Next](./7-monitoring.md)