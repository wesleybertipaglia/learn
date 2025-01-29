# ACID Transactions

ACID is a set of principles that ensure reliable processing of database transactions, vital for maintaining data integrity. It stands for:

## ACID Properties

### Atomicity
- **Description**: A transaction is treated as a single, indivisible unit. If any part of the transaction fails, the entire transaction is rolled back to its previous state.
- **Example**: In a money transfer, both the debit from one account and the credit to another must occur. If one fails, neither should happen.
- **Implementation**: This is often achieved using transaction logs that track changes, allowing rollback on failure.

### Consistency
- **Description**: Every transaction must take the database from one consistent state to another. All defined rules (such as data validation and constraints) must be adhered to.
- **Example**: If a rule states that an account balance cannot be negative, any transaction resulting in a negative balance must be rejected.
- **Implementation**: Enforced through database constraints (e.g., primary keys, foreign keys, check constraints).

### Isolation
- **Description**: Transactions must operate independently and transparently to ensure that concurrent transactions do not interfere with each other.
- **Example**: If two transactions are running simultaneously, the outcome of each should remain unaffected by the other until they are both committed.
- **Implementation**: Isolation levels (such as Read Committed, Repeatable Read, Serializable) define how transactions interact, balancing performance with data integrity.

### Durability
- **Description**: Once a transaction has been committed, its effects are permanent, even in the event of a system failure.
- **Example**: If a transaction to update account balances is committed, the changes must survive any crashes or failures.
- **Implementation**: This is typically managed through write-ahead logging, where changes are recorded to a durable storage before committing.

## Importance of ACID
- **Data Integrity**: Ensures that all transactions leave the database in a valid state, preventing corruption.
- **Reliability**: Systems can trust that transactions will behave predictably.
- **Error Handling**: Simplifies error management by ensuring that incomplete transactions are rolled back.
- **Business Trust**: Critical in applications like banking and e-commerce, where data accuracy is paramount.

## Challenges and Considerations
- **Performance**: Implementing ACID can lead to overhead, particularly with isolation levels. For example, higher isolation can reduce concurrency.
- **Trade-offs**: Some systems may sacrifice strict ACID compliance for performance (e.g., NoSQL databases may opt for eventual consistency).
- **Complexity**: Managing ACID properties requires careful design, particularly in distributed systems.

## Practical Example
In a banking application, consider a transaction where User A transfers $100 to User B:
1. **Atomicity**: Both the debit from User A’s account and the credit to User B’s account must occur together.
2. **Consistency**: After the transaction, both accounts must reflect accurate balances.
3. **Isolation**: If User A initiates the transaction while User C checks their balance, User C should see a consistent state of the database.
4. **Durability**: Once the transaction is committed, User A’s and User B’s accounts should reflect the changes even if the system crashes immediately afterward.

---

- [Previous](./6-denormalization.md)
- [Next](./8-cap.md)
