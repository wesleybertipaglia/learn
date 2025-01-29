# CAP Theorem

The CAP theorem, formulated by Eric Brewer, states that in a distributed data store, it is impossible to simultaneously guarantee all three of the following properties:

## CAP Guarantees

### Consistency (C)
- **Description**: Every read receives the most recent write or an error. All nodes see the same data at the same time.
- **Example**: If a value is updated on one node, all other nodes must reflect this update immediately.

### Availability (A)
- **Description**: Every request receives a response, regardless of whether the data is the most recent. The system remains operational even if some nodes fail.
- **Example**: Even if one part of the system goes down, users can still read and write data.

### Partition Tolerance (P)
- **Description**: The system continues to function despite network partitions that prevent some nodes from communicating with others.
- **Example**: If a network failure occurs, nodes should still operate and handle requests independently.

## Trade-offs
According to the CAP theorem, a distributed system can only provide two of the three guarantees at any given time:

### CP (Consistency and Partition Tolerance)
The system will prioritize consistency and can sacrifice availability in the event of a network partition.
- **Example**: In a bank transaction system, it’s crucial to maintain consistent data even if it means refusing requests during a partition.

### AP (Availability and Partition Tolerance)
The system will remain available and operational but may serve stale data during partitions.
- **Example**: In a social media application, it’s more important to allow users to post updates even if some users see outdated information temporarily.

## Real-World Applications

### CP Systems
Databases like HBase and Google Spanner prioritize consistency and partition tolerance, ensuring that all nodes reflect the same data, even at the cost of availability during network issues.

### AP Systems
NoSQL databases like Cassandra and DynamoDB prioritize availability and partition tolerance, allowing continued operations and eventual consistency.

## Importance of CAP Theorem
### Design Decisions
Helps developers and architects understand the limitations of distributed systems, guiding design choices based on application needs.

### Trade-off Awareness
Encourages consideration of how applications handle data consistency, availability, and network reliability.

---

- [Previous](./7-acid.md)
- [Next](./9-security.md)
