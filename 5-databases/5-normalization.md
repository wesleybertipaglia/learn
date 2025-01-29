# Normalization

**Normalization** is the process of organizing data in a database to minimize redundancy and avoid insertion, update, and deletion anomalies. The goal is to ensure data integrity by eliminating duplication of information and structuring data into smaller tables with well-defined relationships.

## Normal Forms
Normal forms are levels of normalization that follow progressively stricter rules. Each level corrects different types of data organization problems.

### First Normal Form (1NF)
- **Rule**: Eliminates repeated groups of data and ensures that each cell contains a unique value (atomic data).
- **Example**: Separate combined data, such as multiple phone numbers in a single cell, into several distinct rows or columns.

### Second Normal Form (2NF)
- **Rule**: Satisfies 1NF and ensures that all attributes depend entirely on the primary key (there can be no partial dependencies).
- **Example**: Move attributes that do not depend exclusively on the primary key to a separate table.

### Third Normal Form (3NF)
- **Rule**: Satisfies 2NF and removes transitive dependencies, that is, when a non-key attribute depends on another attribute that is not a primary key.
- **Example**: If in an orders table, the customer address depends on the customer ID (and not the order), a separate table should be created for customers.

## Benefits of Normalization
- **Redundancy Reduction**: Avoids unnecessary duplication of data.
- **Improved Data Integrity**: Ensures that changes to related data are consistent. - **Ease of Maintenance**: Updates and deletions become easier, minimizing anomalies.

---

- [Previous](./4-nosql.md)
- [Next](./6-denormalization.md)
