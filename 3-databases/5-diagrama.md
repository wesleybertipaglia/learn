# Entity-Relationship Diagrams (ERD)

## 1. What is an Entity-Relationship Diagram (ERD)?
An **Entity-Relationship Diagram (ERD)** is a visual representation that models the logical structure of a database. It describes the entities of the system, their attributes, and the relationships between them, helping to design or understand the organization of the data.

## 2. Elements of an ER Diagram
The main components of an ER diagram are:

### 2.1. Entities
**Entities** represent objects or concepts about which information is stored in the database. Each entity becomes a table in the relational database.
- **Example**: Customer, Order, Product.

### 2.1.1. Types of Entities
- **Strong Entities**: They exist independently and have their own primary key.
- Example: Customer.
- **Weak Entities**: They depend on another entity to exist and do not have their own primary key.
- Example: Order Details (it depends on the Order).

### 2.2. Attributes
**Attributes** are the properties or characteristics of entities. Each attribute becomes a column in the table corresponding to the entity.
- **Example**: Name (for Customer), Price (for Product).

#### 2.2.1. Types of Attributes
- **Simple Attribute**: Contains a single atomic value.
- Example: `Name`.
- **Compound Attribute**: Can be subdivided into several smaller attributes.
- Example: `Address` (which can be divided into Street, City, Zip Code).
- **Multivalued Attribute**: Can contain more than one value.
- Example: `Phones` (a customer can have more than one phone number).
- **Derived Attribute**: An attribute that can be calculated from other attributes.
- Example: `Age`, derived from date of birth.

### 2.3. Relationships
**Relationships** describe how entities are associated with each other. They indicate the connections between two or more entities.
- **Example**: A Customer places an Order.

#### 2.3.1. Types of Relationships
- **1:1 (One to One)**: An entity A is associated with at most one entity B, and vice versa.
- Example: Each person has a unique identity number.
- **1:N (One to Many)**: An entity A can be associated with multiple entities B, but an entity B can only be associated with one entity A.
- Example: A Customer can place multiple Orders, but each Order belongs to only one Customer.
- **N:M (Many to Many)**: An entity A can be associated with multiple entities B, and vice versa.
- Example: A Student can be enrolled in multiple Courses, and a Course can have multiple Students.

### 2.4. Cardinality
The **cardinality** of a relationship indicates the number of instances of an entity that can be related to instances of another entity. The three main types of cardinality are:
- **1:1** (one-to-one).
- **1:N** (one-to-many).
- **N:M** (many-to-many).

### 2.5. Keys
**Keys** are attributes that uniquely identify an entity or relate one entity to another.

#### 2.5.1. Primary Key (PK)
An attribute (or set of attributes) that uniquely identifies each instance of an entity.
- **Example**: `Customer_ID` as the primary key for the Customer entity.

#### 2.5.2. Foreign Key (FK)
An attribute in an entity that references the primary key of another entity, establishing a relationship between the two.
- **Example**: `Customer_ID` as a foreign key in the Order table, referencing the Customer table.

## 3. Notations in ER Diagrams
There are several notations used in ER diagrams to represent entities, attributes and relationships. The most common include:

- **Rectangles**: Represent entities.
- **Ellipses**: Represent attributes.
- **Diamonds**: Represent relationships between entities.
- **Lines**: Connect entities and relationships, usually marked with cardinality.

### Popular Notations
- **Chen Notation**: One of the most traditional, with ellipses for attributes and diamonds for relationships.
- **Crow’s Foot Notation**: Uses “crow’s feet” to represent cardinality (e.g.: a line with three dashes for many, one dash for one).

## 4. ER Diagram Example
Let's model a simple example of an ordering system, with the entities **Customer**, **Order**, and **Product**.

1. **Customer**: Has attributes such as `Customer_ID` (PK), `Name`, and `Address`.
2. **Order**: Has attributes such as `Order_ID` (PK), `Date`, and `Customer_ID` (FK).
3. **Product**: Has attributes such as `Product_ID` (PK), `Product_Name`, and `Price`.

Relationships:
- **Customer places Order** (1:N).
- **Order includes Product** (N:M) — you would need an associative table, such as `Order_Items`, to represent this relationship.

## 5. Benefits of an ER Diagram
- **Design Clarity**: Helps visualize the data model and understand how the data relates.
- **Improved Communication**: Serves as a clear reference document between development teams and stakeholders.
- **Basis for Database Creation**: A well-structured ERD makes it easier to implement a relational database.

## 6. Limitations of ER Diagrams
- **Complexity**: For very large systems, the diagram can become complex and difficult to understand.
- **Focus on Structure, not Processes**: ERDs show the structure of data, but not how it will be used or how the system will function.

---

- [Previous](./4-normalization.md)