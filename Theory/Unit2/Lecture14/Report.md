# Lecture 14

## Title

Database Schema Design: ER Diagrams, Normalization, Relationships

## Name

Sehaj Vohra

## SAP ID

590011624

## Course

Backend Development

## Program

B.Tech Computer Science and Engineering

## Semester

5

## Objective

To design and implement a Library Management database using Entity Relationship modeling, relational tables, primary keys, foreign keys, and constraints. The practical also demonstrates normalization of an order table into Third Normal Form (3NF), insertion of sample records, and verification through SQL queries.

## Software Requirements

1. Visual Studio Code
2. XAMPP Control Panel
3. MySQL
4. phpMyAdmin
5. A web browser

## Problem Statement

Design a database schema for a Library Management System containing Book, Author, Member, and Loan entities. Establish appropriate relationships and implement the schema using SQL.

Normalize the supplied order table into 3NF, create the normalized tables in MySQL, insert sample records, and verify the data using SQL queries.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Draw the Library Management ER diagram | ER diagram saved in the screenshots folder |
| Task 2 | Design the database schema | Five relational tables defined in `schema.sql` |
| Task 3 | Create tables and verify relationships | Tables created in MySQL and four foreign key relationships verified |
| Task 4 | Normalize the order table into 3NF | Four normalized tables created in `normalization.sql` |
| Task 5 | Insert and verify normalized sample data | SQL joins and order total calculations returned expected results |

## Task 1: Library Management ER Diagram

### Task Given

Draw an Entity Relationship diagram for a Library Management System containing Book, Author, Member, and Loan entities, including relevant attributes and relationships.

### Implementation

A Library Management ER diagram was prepared and saved in the project screenshots folder. It was used as the design reference for the relational schema.

### Code Location

[Lecture 14 folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture14)

### Screenshot

![Library Management ER Diagram](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/Library%20ER%20Diagram.png)

### Result

The ER diagram provides a visual representation of the main Library Management entities and their relationships.

## Task 2: Database Schema Design

### Task Given

Design a relational schema with primary keys, foreign keys, and appropriate relationships. A book may have multiple authors, and a member may borrow multiple books.

### Implementation

The file `schema.sql` defines five tables:

1. `Author` stores author information.
2. `Book` stores book details.
3. `Member` stores member details.
4. `Loan` records borrowing information and references `Member` and `Book`.
5. `BookAuthor` implements the many to many relationship between books and authors using a composite primary key.

The schema uses primary keys, foreign keys, and constraints including `NOT NULL`, `UNIQUE`, and `DEFAULT`.

### Code Location

[View schema.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture14/schema.sql)

### Screenshot

![Library Management ER Diagram](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/Library%20ER%20Diagram.png)

### Result

The relational schema defines five tables and the intended key relationships.

## Task 3: Create Tables and Verify Relationships in MySQL

### Task Given

Execute the schema in MySQL and verify that all tables and foreign key relationships are present.

### Implementation

A database named `library_management` was created in phpMyAdmin using XAMPP. The statements in `schema.sql` were executed in that database.

The `SHOW TABLES` query confirmed the five Library Management tables. A query against `INFORMATION_SCHEMA.KEY_COLUMN_USAGE` verified these foreign key relationships:

1. `Loan.member_id` references `Member.member_id`.
2. `Loan.book_id` references `Book.book_id`.
3. `BookAuthor.book_id` references `Book.book_id`.
4. `BookAuthor.author_id` references `Author.author_id`.

### Code Location

[View schema.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture14/schema.sql)

### Screenshots

![MySQL tables verified](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/task3-mysql-tables-verified.png)

![Foreign key relationships verified](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/task3-foreign-keys-verified.png)

### Result

All five Library Management tables and the four expected foreign key relationships were verified in MySQL.

## Task 4: Normalize the Order Table into 3NF

### Task Given

Normalize the supplied order table containing `order_id`, `customer_name`, `customer_email`, `product_name`, `product_price`, and `quantity` into Third Normal Form (3NF).

### Implementation

The file `normalization.sql` defines four tables:

1. **Customer:** Stores customer details with `customer_id` as the primary key.
2. **Orders:** Stores each order and references Customer through `customer_id`.
3. **Product:** Stores product details with `product_id` as the primary key.
4. **OrderItem:** Connects orders and products, stores quantity, and uses the composite primary key `(order_id, product_id)`.

The normalized tables separate customer details, order details, product details, and order quantities. Sample data was inserted into the four tables.

### Code Location

[View normalization.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture14/normalization.sql)

### Screenshots

![Order table normalization solution](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/task4-order-table-3nf.png)

![Normalized tables verified](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/task4-normalized-tables-verified.png)

![Normalized sample data verified](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/task4-normalized-sample-data-verified.png)

### Result

The four normalized tables were created in MySQL, and sample records were inserted and verified.

## Task 5: Verify Normalized Data Using SQL Queries

### Task Given

Insert sample data into the normalized tables and verify the relationships and calculated order totals.

### Implementation

An SQL join combined `Orders`, `Customer`, `OrderItem`, and `Product` to display each order item with its customer, product, price, and quantity.

A second query used `SUM(product_price * quantity)` with `GROUP BY` to calculate the order total.

The verified results were:

| Order ID | Customer | Order Total |
|---|---|---:|
| 1 | Aarav | 66000.00 |
| 2 | Diya | 1500.00 |

Aarav's total consists of one Laptop at 65000 and two Mouse units at 500 each. Diya's total consists of one Keyboard at 1500.

### Code Location

[View normalization.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture14/normalization.sql)

### Screenshots

![Normalized tables joined successfully](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/task5-normalized-join-results.png)

![Order totals verified](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture14/screenshots/task5-order-totals-verified.png)

### Result

The join query returned three order item rows, and the aggregate query returned the expected totals for both customers.

## Project Structure

```text
Theory/
└── Unit2/
    └── Lecture14/
        ├── screenshots/
        │   ├── Library ER Diagram.png
        │   ├── task3-foreign-keys-verified.png
        │   ├── task3-mysql-tables-verified.png
        │   ├── task4-normalized-sample-data-verified.png
        │   ├── task4-normalized-tables-verified.png
        │   ├── task4-order-table-3nf.png
        │   ├── task5-normalized-join-results.png
        │   └── task5-order-totals-verified.png
        ├── normalization.sql
        ├── Report.md
        └── schema.sql
```

## Concepts Used

1. Entity Relationship modeling
2. Relational database schema design
3. Primary keys and composite primary keys
4. Foreign keys and referential integrity
5. One to many and many to many relationships
6. SQL table creation and constraints
7. Database normalization and 3NF
8. Inserting sample records
9. Inspecting metadata through `INFORMATION_SCHEMA`
10. Joining related tables using `JOIN`
11. Aggregation using `SUM` and `GROUP BY`

## Overall Result

The Library Management schema was created and verified in MySQL. Its five tables and four foreign key relationships were checked. The order table was decomposed into Customer, Orders, Product, and OrderItem tables. Sample data was inserted, and join and aggregation queries returned the expected results.

## Observations

1. Primary keys uniquely identify records.
2. Foreign keys link related records and enforce referential integrity.
3. `BookAuthor` represents the many to many relationship between books and authors.
4. Separating customer and product details reduces repeated information in order records.
5. `OrderItem` records the products and quantities belonging to each order.
6. Join queries retrieve related information from normalized tables.
7. Aggregate queries calculate order totals from prices and quantities.
8. The implementation was verified using phpMyAdmin and MySQL queries.

## Conclusion

This practical demonstrated ER modeling, relational schema design, primary and foreign keys, and normalization. The Library Management schema was implemented and verified in MySQL. The order data was normalized into separate related tables, and SQL queries were used to verify sample records and calculate order totals.

## Experiment Link

[Lecture 14 source folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture14)

A published GitHub Pages URL for this lecture was not verified.

## Complete Source Code

[View the complete Lecture 14 folder on GitHub](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture14)

[View schema.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture14/schema.sql)

[View normalization.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture14/normalization.sql)
