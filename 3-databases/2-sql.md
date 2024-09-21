# SQL (Structured Query Language)

## 1. What is SQL?
**SQL** (Structured Query Language) is a standard language used to manage and manipulate relational databases. It allows you to execute commands to create, modify, query, and control access to data in a database.

## 2. SQL Command Categories
SQL commands can be classified into several categories, depending on their purpose:

### 2.1. DML (Data Manipulation Language)
Commands used to manipulate data, i.e., insert, update, delete, and query data in tables.

- **`SELECT`**: Retrieves data from a table.
- Example: `SELECT * FROM Clientes;`
- **`INSERT`**: Inserts new data into a table.
- Example: `INSERT INTO Customers (Name, Email) VALUES ('John', 'john@email.com');`
- **`UPDATE`**: Updates existing data in a table.
- Example: `UPDATE Customers SET Email = 'john@newemail.com' WHERE Customer_ID = 1;`
- **`DELETE`**: Deletes data from a table.
- Example: `DELETE FROM Customers WHERE Customer_ID = 1;`

### 2.2. DDL (Data Definition Language)
Commands used to define or modify the structure of databases and tables.

- **`CREATE`**: Creates new tables, databases, indexes or other objects. - Example: `CREATE TABLE Clientes (ID_Cliente INT PRIMARY KEY, Nome VARCHAR(100), Email VARCHAR(100));`
- **`ALTER`**: Modifies the structure of an existing table (e.g.: add or remove columns).
- Example: `ALTER TABLE Clientes ADD Telefone VARCHAR(15);`
- **`DROP`**: Removes a table, database or other object.
- Example: `DROP TABLE Clientes;`

### 2.3. DCL (Data Control Language)
Commands used to control user access and permissions in the database.

- **`GRANT`**: Grants permissions to users.
- Example: `GRANT SELECT, INSERT ON Clientes TO Usuario;`
- **`REVOKE`**: Revokes user permissions.
- Example: `REVOKE INSERT ON Clientes FROM Usuario;`

### 2.4. TCL (Transaction Control Language)
Commands used to manage transactions in the database, ensuring data consistency.

- **`COMMIT`**: Commits the changes made in the transaction.
- Example: `COMMIT;`
- **`ROLLBACK`**: Undoes the changes made during the transaction.
- Example: `ROLLBACK;`
- **`SAVEPOINT`**: Sets a point in the transaction so that you can do a partial rollback.
- Example: `SAVEPOINT point1;`

## 3. Common SQL Clauses
SQL offers several clauses that can be used to modify `SELECT` queries and other operations. Some of the most important are:

### 3.1. `WHERE`
Filters records based on a specific condition.
- Example: `SELECT * FROM Clientes WHERE Cidade = 'São Paulo';`

### 3.2. `ORDER BY`
Sorts the results based on one or more columns.
- Example: `SELECT * FROM Customers ORDER BY Name ASC;`

### 3.3. `GROUP BY`
Groups the records based on one or more columns and is usually used with aggregate functions (such as `COUNT`, `SUM`, `AVG`).
- Example: `SELECT City, COUNT(*) FROM Customers GROUP BY City;`

### 3.4. `HAVING`
Filters the groups created by the `GROUP BY` clause based on a condition.
- Example: `SELECT City, COUNT(*) FROM Customers GROUP BY City HAVING COUNT(*) > 5;`

### 3.5. `JOIN`
Combines data from two or more tables based on a condition. There are several types of joins:
- **`INNER JOIN`**: Returns records that have matches in both tables.
- Example: `SELECT Customers.Name, Orders.Order_ID FROM Customers INNER JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID;`
- **`LEFT JOIN`**: Returns all records from the table on the left and the corresponding ones from the table on the right. If there is no match, returns `NULL`.
- Example: `SELECT Customers.Name, Orders.Order_ID FROM Customers LEFT JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID;`
- **`RIGHT JOIN`**: Returns all records from the table on the right and the corresponding ones from the table on the left. - Example: `SELECT Customers.Name, Orders.Order_ID FROM Customers RIGHT JOIN Orders ON Customers.Customer_ID = Orders.Customer_ID;`

## 4. Aggregate Functions
Aggregate functions perform calculations on a set of values ​​and return a single value.

- **`COUNT()`**: Counts the number of rows.
- Example: `SELECT COUNT(*) FROM Customers;`
- **`SUM()`**: Adds the values ​​of a numeric column.
- Example: `SELECT SUM(Price) FROM Products;`
- **`AVG()`**: Calculates the average of the values ​​of a numeric column.
- Example: `SELECT AVG(Price) FROM Products;`
- **`MAX()`**: Returns the maximum value of a column. - Example: `SELECT MAX(Price) FROM Products;`
- **`MIN()`**: Returns the minimum value of a column.
- Example: `SELECT MIN(Price) FROM Products;`

## 5. Subqueries
**Subqueries** are nested queries inside another SQL query. They can be used in multiple clauses, such as `WHERE`, `FROM`, or `SELECT`.

- **Example**: `SELECT Name FROM Customers WHERE Customer_ID IN (SELECT Customer_ID FROM Orders WHERE Value > 1000);`

## 6. Indexes
**Indexes** are used to speed up data retrieval in a table, allowing the database to locate data more quickly.

- **Creating an Index**: `CREATE INDEX idx_nome ON Clientes(Nome);`
- **Removing an Index**: `DROP INDEX idx_nome;`

## 7. Views
A **view** is a virtual table based on the result of an SQL query. Views are used to simplify complex queries, improve security, and reduce maintenance complexity.

- **Creating a View**: `CREATE VIEW vista_clientes_pedidos AS SELECT Clientes.Nome, Pedidos.Date FROM Clientes INNER JOIN Pedidos ON Clientes.ID_Cliente = Pedidos.ID_Cliente;`
- **Querying a View**: `SELECT * FROM vista_clientes_pedidos;`
- **Removing a View**: `DROP VIEW vista_clientes_pedidos;`

## 8. Stored Procedures and Functions
**Stored Procedures** are blocks of SQL code that can be stored and executed on the database server.

- **Procedure**:
```sql
-- creating a procedure
CREATE PROCEDURE AtualizaEstoque(IN produto_id INT, IN quanto INT)
BEGIN
UPDATE Produtos SET Estoque = Estoque + quanto WHERE ID_Produto = produto_id;
END;

-- calling a procedure
CALL AtualizaEstoque(1, 10);
```

- **Functions** are blocks of SQL code that return a value.

```sql
-- creating a function
CREATE FUNCTION CalculatesDiscount(price DECIMAL(10,2), discount DECIMAL(4,2))
RETURNS DECIMAL(10,2)

BEGIN
DECLARE discount_value DECIMAL(10,2);
SET discount_value = price * (discount / 100);
RETURN price - discount_value;
END;

-- calling a function
SELECT CalculatesDiscount(100, 10);
```

## 9. Transactions

A transaction is a set of SQL operations that must be executed as a single logical unit. ACID (Atomicity, Consistency, Isolation, Durability) properties ensure the reliability of transactions.

- Starting a Transaction: `START TRANSACTION;`
- Committing a Transaction: `COMMIT;`
- Rolling Back a Transaction: `ROLLBACK;`

---

- [Previous](./1-fundamentals.md)
- [Next](./3-nosql.md)