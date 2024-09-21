# Normalization and Denormalization

## 1. What is Normalization?
**Normalization** is the process of organizing data in a database to minimize redundancy and avoid insertion, update, and deletion anomalies. The goal is to ensure data integrity by eliminating duplication of information and structuring data into smaller tables with well-defined relationships.

### 1.1. Normal Forms
Normal forms are levels of normalization that follow progressively stricter rules. Each level corrects different types of data organization problems.

#### 1.1.1. First Normal Form (1NF)
- **Rule**: Eliminates repeated groups of data and ensures that each cell contains a unique value (atomic data).
- **Example**: Separate combined data, such as multiple phone numbers in a single cell, into several distinct rows or columns.

#### 1.1.2. Second Normal Form (2NF)
- **Rule**: Satisfies 1NF and ensures that all attributes depend entirely on the primary key (there can be no partial dependencies).
- **Example**: Move attributes that do not depend exclusively on the primary key to a separate table.

#### 1.1.3. Third Normal Form (3NF)
- **Rule**: Satisfies 2NF and removes transitive dependencies, that is, when a non-key attribute depends on another attribute that is not a primary key.
- **Example**: If in an orders table, the customer address depends on the customer ID (and not the order), a separate table should be created for customers.

### 1.2. Benefits of Normalization
- **Redundancy Reduction**: Avoids unnecessary duplication of data.
- **Improved Data Integrity**: Ensures that changes to related data are consistent. - **Ease of Maintenance**: Updates and deletions become easier, minimizing anomalies.

## 2. What is Denormalization?
**Denormalization** is the opposite process to normalization, in which data is deliberately duplicated and combined to improve query performance. While normalization aims at storage efficiency and data integrity, denormalization seeks to optimize data reading by reducing the number of joins in complex queries.

### 2.1. When to Use Denormalization?
Denormalization is useful in systems where data reading is more frequent and query performance needs to be optimized. Examples include analytics systems, data warehouses, and applications with high read volumes.

### 2.2. Denormalization Techniques
- **Add calculated columns**: Columns that store the results of frequently used calculations, preventing them from being recalculated at runtime. - **Data Duplication**: Storing information that would normally be in separate tables in a single table to avoid the use of `JOIN`.
- **Aggregate Tables**: Creating tables containing aggregated data (e.g. totals, averages) to optimize reports and analytical queries.

### 2.3. Benefits of Denormalization
- **Performance Improvement**: Reduces the number of joins required in complex queries, making them faster.
- **Ease of Query**: Queries become simpler, since the necessary data is in a single table.

### 2.4. Disadvantages of Denormalization
- **Increased Redundancy**: Data duplication can lead to inconsistency if the data is not updated correctly.
- **Difficulty of Maintenance**: Changes in data may require updates in multiple tables.

## 3. Comparison between Normalization and Denormalization

| **Criteria** | **Normalization** | **Denormalization** |
|-----------------------|-----------------------------------------|------------------------------------------|
| **Objective** | Minimize redundancy, improve integrity | Improve read performance |
| **Structure** | Data split across multiple tables | Data combined into larger tables |
| **Main Advantage** | Reduce inconsistencies and anomalies | Reduce query time |
| **Main Disadvantage** | Makes complex queries difficult | Increases redundancy and may generate inconsistencies |
| **Application** | Transactional systems (OLTP) | Analytical systems (OLAP) or read-intensive systems |

---

- [Previous](./3-nosql.md)
- [Next](./5-diagrama.md)