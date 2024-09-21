# NoSQL (Not Only SQL)

## 1. What is NoSQL?
**NoSQL** refers to a set of database management systems that do not follow the traditional table-based relational database model. NoSQL is designed to handle large volumes of distributed data, provide high scalability, data flexibility, and support unstructured data types.

## 2. Characteristics of NoSQL Databases
- **Horizontal Scalability**: Supports expansion by distributing data across multiple servers.
- **Schema Flexibility**: Unlike relational databases, NoSQL allows you to store data without a fixed schema, making it easy to change the format of the data over time.
- **Large-Scale Performance**: Optimized for large data volumes and high read/write throughput.
- **High Availability and Data Partitioning**: Supports distributed systems and fault tolerance. - **Unstructured Data Storage**: Allows you to store data in JSON, XML, and other formats, without following a column and table structure.

## 3. Types of NoSQL Databases
There are different categories of NoSQL databases, each suited to a specific type of need:

### 3.1. Key-Value Databases
This model stores data as key-value pairs, where the key is unique and is used to retrieve the associated value. It is simple, fast, and efficient for unstructured data.

- **Examples**: Redis, DynamoDB, Riak.
- **When to Use**: Ideal for storing cache, user sessions, and user profiles.

#### Example of structure:
```json
{
"user123": {
"name": "Maria",
"age": 29,
"city": "São Paulo"
}
}
```

### 3.2. Document-Oriented Databases
Store data in document format (usually JSON or BSON). Each document can have a different schema, providing flexibility.

- **Examples**: MongoDB, CouchDB, Amazon DocumentDB.
- **When to Use**: Applications that deal with semi-structured data or that require schema flexibility (e.g., product catalogs, user profiles).

Example of a JSON document:
```json
{
"_id": "12345",
"name": "John",
"address": {
"city": "Rio de Janeiro",
"state": "RJ"
},
"orders": [
{"order_id": 1, "value": 150},
{"order_id": 2, "value": 200}
]
}
```

### 3.3. Column-Oriented Databases
Store data in columns instead of rows. Each column can be stored and read independently, which optimizes read-intensive queries.

- **Examples**: Cassandra, HBase.
- **When to Use**: For large volumes of data with high read rates, such as event logs and data warehouses.

Example of column structure:
```
| Customer_ID | Name | Email |
|------------|--------|------------------|
| 1 | John | joao@email.com |
```

### 3.4. Graph-Oriented Databases
Are designed to store and navigate complex relationships between data. Entities are represented as nodes, and relationships between them are stored as edges.

- **Examples**: Neo4j, ArangoDB, Amazon Neptune.
- **When to Use**: For social network modeling, recommendation systems, fraud detection, and network analysis.

Graph Example:
- **Nodes**: Person (John), Person (Mary)
- **Edges**: John is a friend of Mary

## 4. Advantages of NoSQL
- **Horizontal Scalability**: Ability to add more servers (scale "horizontally") to handle data growth.
- **High Performance**: Designed to handle large volumes of reads and writes, especially in distributed systems.
- **Flexibility**: Does not require a fixed schema, allowing the storage of data of different types without structural changes.
- **Fault Tolerance**: NoSQL systems are designed to operate effectively in distributed and high-availability environments.

## 5. Disadvantages of NoSQL
- **Consistency**: Many NoSQL systems follow the CAP (Consistency, Availability, and Partition Tolerance) model, sacrificing consistency in favor of availability and partitioning. - **Transaction Support**: NoSQL databases generally have limited support for ACID transactions, although some have begun to offer more transactional features.
- **Lack of Standardization**: Different NoSQL systems may have very different APIs and functionality, making portability between them difficult.
- **Query Complexity**: Complex queries such as JOINs and GROUP BY may not be as efficient or supported as in relational databases.

## 6. When to Use NoSQL?
- **Large Data Volumes**: NoSQL is ideal for applications that manage large volumes of distributed data.
- **Semi-structured or Unstructured Data**: If you need to store data that changes format frequently, or that does not fit well into a rigid table schema.
- **High Read/Write Rate**: Applications with many simultaneous users that require high read and write rates.
- **Scalability**: When it is necessary to scale horizontally and distribute data across multiple servers.

## 7. Examples of NoSQL Use Cases
- **Social networks**: For modeling complex relationships and personalized recommendations.
- **E-commerce**: Storage of product catalogs that vary in attributes.
- **Real-time applications**: Recommendation systems, chats, monitoring systems and event analysis.
- **Data Lakes**: Storage of large volumes of data without a defined structure for later analysis.

---

- [Previous](./2-sql.md)
- [Next](./4-normalization.md)