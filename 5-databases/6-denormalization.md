# Denormalization

**Denormalization** is the opposite process to normalization, in which data is deliberately duplicated and combined to improve query performance. While normalization aims at storage efficiency and data integrity, denormalization seeks to optimize data reading by reducing the number of joins in complex queries.

### When to Use Denormalization?
Denormalization is useful in systems where data reading is more frequent and query performance needs to be optimized. Examples include analytics systems, data warehouses, and applications with high read volumes.

### Denormalization Techniques
- **Add calculated columns**: Columns that store the results of frequently used calculations, preventing them from being recalculated at runtime. - **Data Duplication**: Storing information that would normally be in separate tables in a single table to avoid the use of `JOIN`.
- **Aggregate Tables**: Creating tables containing aggregated data (e.g. totals, averages) to optimize reports and analytical queries.

### Benefits of Denormalization
- **Performance Improvement**: Reduces the number of joins required in complex queries, making them faster.
- **Ease of Query**: Queries become simpler, since the necessary data is in a single table.

### Disadvantages of Denormalization
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

- [Previous](./5-normalization.md)
- [Next](./7-acid.md)
