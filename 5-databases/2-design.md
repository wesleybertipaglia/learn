# Database Design Summary

Database design is the process of defining the structure, storage, and relationships of data in a database. Effective design is crucial for efficient data management, retrieval, and integrity.

## Phases of Database Design

### 1. Requirements Gathering
- Identify the data needs of users.
- Gather functional and non-functional requirements.

### 2. Conceptual Design
- Create a high-level model of the database.
- Use Entity-Relationship Diagrams (ERDs) to visualize entities, attributes, and relationships.

### 3. Logical Design
- Convert the conceptual model into a logical model.
- Define tables, columns, data types, and relationships (using normalization techniques).

### 4. Physical Design
- Define how data is stored physically.
- Optimize for performance (indexes, partitions, storage).

## Key Concepts in Database Design

### Entities and Attributes
- **Entity**: A real-world object or concept (e.g., Customer, Product).
- **Attribute**: A property of an entity (e.g., Customer Name, Product Price).

### Relationships
Defines how entities interact with each other:
- **One-to-One**: Each entity in A is related to one in B.
- **One-to-Many**: An entity in A can be related to many in B.
- **Many-to-Many**: Entities in A can relate to many in B and vice versa.

## Database Schema
- The structure that defines the organization of data.
- Includes definitions of tables, fields, relationships, and constraints.

## Data Integrity Constraints
Rules that ensure accuracy and consistency of data:
- **Primary Key**: Unique identifier for a table.
- **Foreign Key**: Links to primary keys in other tables.
- **Unique Constraint**: Ensures all values in a column are distinct.
- **Check Constraint**: Validates values based on specified conditions.

## Indexing
- Improves data retrieval speed.
- Types of indexes include:
  - **Primary Index**: Based on primary key.
  - **Secondary Index**: Based on non-primary key attributes.

## Designing for Performance
- Considerations for scalability and speed:
  - Optimize queries and indexing.
  - Use appropriate data types.
  - Partition large tables for better performance.

## Security Considerations
- Implement access controls and permissions.
- Use encryption for sensitive data.
- Regular audits for compliance and security.

## Documentation
- Keep thorough documentation of the database design.
- Use ERDs, schema diagrams, and data dictionaries for clarity.

---

- [Previous](./1-foundations.md)
- [Next](./3-sql.md)
