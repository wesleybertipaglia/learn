# Database Fundamentals

## 1. What is a Database?
A database is an organized collection of data that can be accessed, managed, and updated. It allows for the structured storage of information so that it can be retrieved and manipulated easily.

## 2. Types of Databases
- **Relational Databases (SQL):** Structured in tables with rows and columns. Ex: MySQL, PostgreSQL.
- **Non-relational Databases (NoSQL):** Designed to handle large volumes of unstructured data. Ex: MongoDB, Cassandra.

## 3. Basic Concepts
- **Tables:** main structures in relational databases, composed of rows (records) and columns (attributes).

- **Primary Key:** one or more fields that uniquely identify a record in a table.

- **Foreign Key:** a field that creates a relationship between two tables by referencing the primary key of another table.

- **Indexes:** structures that speed up data retrieval, allowing faster searches.

- **Queries:** requests made to a database to retrieve or manipulate data. In relational databases, SQL (Structured Query Language) is used.

## 4. Data Modeling
Data modeling involves creating a **data model** that represents the logical structure of the data. This includes:
- **Entity-Relationship Diagram (ERD)**: A visual model that describes how data is related.
- **Normalization**: The process of organizing data to reduce redundancy and improve data integrity.

## 5. Normalization
- **1st Normal Form (1NF)**: Eliminates duplicate columns and creates separate tables for related groups of data.

## 6. Data Modeling
- **1st Normal Form (1NF)**: Eliminates duplicate columns and creates separate tables for related groups of data. - **2nd Normal Form (2NF)**: Ensures that all attributes depend entirely on the primary key.
- **3rd Normal Form (3NF)**: Removes transitive dependencies (when a field depends on another field that is not the primary key).

## 6. ACID (Transaction Properties)
1. **Atomicity**: Transactions are "all or nothing" (they complete completely or fail completely).
2. **Consistency**: Ensures that the transaction takes the database from one valid state to another valid state.
3. **Isolation**: Concurrent transactions do not interfere with each other.
4. **Durability**: After commit, data persists in the database, even in case of failure.

## 7. Basic SQL
### 7.1. Data Manipulation Commands (DML)
- `SELECT`: Query data.
- `INSERT`: Inserts data into a table.
- `UPDATE`: Updates existing data.
- `DELETE`: Removes data from a table.

### 7.2. Data Definition (DDL) Commands
- `CREATE`: Creates new tables or objects.
- `ALTER`: Modifies the structure of tables.
- `DROP`: Removes tables or objects from the database.

### 7.3. Transaction Control Commands (TCL)
- `COMMIT`: Commits a transaction.
- `ROLLBACK`: Rolls back a transaction.

### 7.4. Access Control Commands (DCL)
- `GRANT`: Grants privileges to users.
- `REVOKE`: Revokes privileges from users.

### 7.5. Aggregate Functions
- `COUNT()`: Counts the number of rows.
- `SUM()`: Sums the values ​​of a column.
- `AVG()`: Calculates the average of the values ​​of a column.
- `MAX()`: Returns the largest value of a column.
- `MIN()`: Returns the smallest value of a column.

### 7.6. SQL Clauses
- `WHERE`: Filters the results.
- `ORDER BY`: Orders the results.
- `GROUP BY`: Groups the results.
- `HAVING`: Filters the results of groups.
- `JOIN`: Combines data from two or more tables.

## 8. NoSQL
NoSQL databases are designed to work with large volumes of unstructured or semi-structured data. There are four main categories:
- **Documents**: Stores data in document format (JSON, BSON). Ex: MongoDB.
- **Key-Value**: Data stored as key-value pairs. Ex: Redis.
- **Columnar**: Stores data in columns, optimizing large volumes of data. Ex: Cassandra.
- **Graphs**: Optimizes the representation of networks and relationships. Ex: Neo4j.

## 9. Database Management Tools (DBMS)
A Database Management System (DBMS) is a software that allows you to create, manage and manipulate databases.
- **Examples of Relational DBMSs**: MySQL, PostgreSQL, Oracle, SQL Server.
- **Examples of NoSQL DBMSs**: MongoDB, CouchDB, Cassandra.

## 10. Database Security
Includes techniques to ensure that data is protected against unauthorized access. Some practices include:
- **Authentication**: Verifying the identity of users.
- **Authorization**: Controlling the level of user access.
- **Encryption**: Protecting data at rest and in transit.

## 11. Backup and Recovery
**Backup** and **recovery** strategies are essential to ensure that data can be restored in the event of loss or failure.
- **Full Backup**: Copy of the entire database.
- **Incremental Backup**: Copy of changes made since the last backup.

## 12. Replication
Replication is the process of copying and keeping multiple databases synchronized on different servers. It can be used to improve availability and scalability.

---

- [Next](./2-sql.md)