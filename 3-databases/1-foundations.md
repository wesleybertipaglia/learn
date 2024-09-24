# Database Foundations

A database is an organized collection of structured information, or data, typically stored electronically in a computer system. It allows for efficient storage, retrieval, and management of data.

## Types of Databases

### Relational Databases (SQL)
- **Structure**: Based on tables (relations) with rows (records) and columns (attributes).
- **Key Concept**: Tables are connected by **keys** (primary and foreign keys).
- **Example Systems**: MySQL, PostgreSQL, Oracle, SQL Server.
- **Query Language**: Structured Query Language (SQL).

### Non-Relational Databases (NoSQL)
- **Structure**: Non-relational, designed to handle unstructured data.
- **Key Concept**: Schema-less, flexible data models (key-value, document, graph, etc.).
- **Example Systems**: MongoDB (document), Redis (key-value), Neo4j (graph).
- **Query Language**: Varied by system, e.g., MongoDB query language.

## Core Concepts

- **Data**: Raw facts or figures stored in the database.
- **Database**: Collection of related data organized in a structured format.
- **SQL**: Structured Query Language used to interact with databases.
- **NoSQL**: Databases that do not use the traditional tabular structure.
- **Model**: Representation of the database structure.
- **Schema**: Blueprint or structure of the database.
- **Keys**: Identifiers used to establish relationships between tables.
- **Indexes**: Data structures used to speed up data retrieval.
- **Transactions**: A sequence of operations treated as a single unit of work.
- **Query**: A request for data from the database.

## Database Design

The process of designing a database involves several steps:

1. **Requirements Analysis**: Understand the data and its relationships.
2. **Conceptual Design**: Define the high-level structure of the database.
3. **Logical Design**: Translate the conceptual design into a logical schema.
4. **Physical Design**: Implement the logical schema in the DBMS.
5. **Testing and Optimization**: Ensure the database meets requirements and is performant.

## Database Management Systems (DBMS)

A DBMS is software that allows users to define, create, maintain, and control access to databases.

### Functions of a DBMS
- **Data Definition**: Define and modify data structure.
- **Data Retrieval**: Query data using a query language.
- **Data Update**: Insert, update, or delete data.
- **Data Integrity**: Ensure accuracy and consistency of data.
- **Transaction Management**: Ensure **ACID** properties (Atomicity, Consistency, Isolation, Durability).
- **Concurrency Control**: Manage simultaneous access to data.
- **Backup and Recovery**: Ensure data is recoverable in case of failure.

### Popular DBMS
- **Relational**: MySQL, PostgreSQL, Oracle, SQL Server.
- **NoSQL**: MongoDB, Cassandra, Couchbase, Neo4j, Redis, Memcached.

## Normalization
A process in relational databases to minimize redundancy and dependency by organizing fields and tables:
- **1NF (First Normal Form)**: Eliminate repeating groups, ensure atomic values.
- **2NF (Second Normal Form)**: Remove partial dependencies on non-primary key attributes.
- **3NF (Third Normal Form)**: Remove transitive dependencies between non-primary key attributes.

## ACID Transactions
A sequence of operations performed as a single logical unit of work. The ACID properties ensure reliability and consistency of transactions:
- **Atomicity**: All or nothing; the transaction is completed fully or not at all.
- **Consistency**: The database moves from one valid state to another.
- **Isolation**: Transactions do not interfere with each other.
- **Durability**: Once a transaction is committed, it remains even in case of a system failure.

## CAP Theorem
In distributed databases, you can only achieve two out of the three:
- **Consistency**: All nodes see the same data at the same time.
- **Availability**: Every request receives a response, without guarantee of consistency.
- **Partition Tolerance**: The system continues to function even when network partitions occur.

## Database Security
Ensuring the confidentiality, integrity, and availability of data:
- **Authentication**: Verifying identity of users.
- **Authorization**: Granting access rights to data.
- **Encryption**: Protecting data at rest and in transit.
- **Auditing**: Logging actions for later review.

## Backup and Recovery
Critical for maintaining data availability:
- **Full Backup**: Complete copy of the database.
- **Incremental Backup**: Backup only changes since the last backup.
- **Point-in-Time Recovery**: Restoring the database to a specific point in time.

## Replication
Replication is the process of copying and keeping multiple databases synchronized on different servers. It can be used to improve availability and scalability.

---

- [Next](./2-sql.md)