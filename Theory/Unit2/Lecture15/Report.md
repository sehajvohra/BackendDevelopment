# Experiment 15

## Title

Data Modeling: Designing Models for Applications

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

To design and implement application data models using conceptual
modeling, SQLAlchemy ORM, Mongoose ODM, and Pydantic based validation.
The experiment demonstrates how application requirements are translated
into structured data models, relationships, database operations,
document schemas, and validation rules.

## Software Requirements

1.  Python
2.  SQLAlchemy
3.  SQLite
4.  Node.js
5.  npm
6.  MongoDB
7.  Mongoose
8.  FastAPI
9.  Pydantic
10. Uvicorn
11. Visual Studio Code
12. Web browser

## Problem Statement

The experiment focuses on data modeling for backend applications. The
required work includes designing a conceptual data model for an E
Commerce system, creating related SQLAlchemy models for a Student
Management System, performing CRUD operations using SQLAlchemy, defining
Mongoose schemas for a Blog application, and implementing validation
rules to maintain data integrity.

## Task Summary

  -----------------------------------------------------------------------
  Task                    Description             Implementation
  ----------------------- ----------------------- -----------------------
  Task 1                  SQLAlchemy Student      Python SQLAlchemy
                          Management Data         models for Department,
                          Modeling and CRUD       Student, Course, and
                                                  Enrollment with SQLite
                                                  storage and Create,
                                                  Read, Update, and
                                                  Delete operations

  Task 2                  E Commerce Conceptual   Mermaid conceptual
                          Data Model              model containing
                                                  Customer, Cart,
                                                  Product, and Order
                                                  entities with their
                                                  relationships

  Task 3                  Mongoose Blog Models    Node.js application
                                                  using Mongoose with
                                                  Post and Comment
                                                  schemas, MongoDB
                                                  connection, post
                                                  creation, post
                                                  retrieval, comment
                                                  creation, and comment
                                                  retrieval with the
                                                  related post

  Task 4                  Data Validation         FastAPI and Pydantic
                                                  based student
                                                  validation with
                                                  required fields, email
                                                  validation, branch
                                                  pattern validation, and
                                                  validation error
                                                  testing
  -----------------------------------------------------------------------

## Task 1: SQLAlchemy Student Management Data Modeling and CRUD

### Task Given

The task required creation of SQLAlchemy models for a Student Management
System with appropriate relationships and implementation of CRUD
operations. The required operations included creating a student with
department assignment, retrieving students from a specific branch,
updating a student's branch, and deleting a student followed by
verification.

### Implementation

The implementation uses SQLAlchemy with SQLite through the database file
`students.db`.

Four models are defined:

1.  `Department`
2.  `Student`
3.  `Course`
4.  `Enrollment`

The models contain primary keys, foreign keys, unique constraints,
required fields, and SQLAlchemy relationships.

The application:

1.  Creates the database tables.
2.  Finds or creates the Computer Science department.
3.  Creates a student named Sehaj Vohra with CSE branch and department
    assignment.
4.  Reads students whose branch is CSE.
5.  Updates the student's branch from CSE to ECE.
6.  Deletes the student using the email address.
7.  Verifies that the student is no longer found after deletion.

The final execution successfully demonstrated the database creation,
student creation, retrieval, update, deletion, and deletion
verification.

### Code Location

[model.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture15/Task1_Data_Modeling/model.py)

[Task 1
Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture15/Task1_Data_Modeling)

### Screenshots

![Database tables created and database file
generated](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task1_Data_Modeling/screenshots/task1-database-created.png)

![Student creation
result](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task1_Data_Modeling/screenshots/task1-student-created.png)

![Student update
result](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task1_Data_Modeling/screenshots/task1-update-student.png)

![CRUD operations and deletion
verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task1_Data_Modeling/screenshots/task1-crud-operations.png)

### Result

The SQLAlchemy implementation successfully created the SQLite database
and its tables. A student was associated with the Computer Science
department, retrieved using the CSE branch, updated to the ECE branch,
deleted, and then verified as not found.

## Task 2: E Commerce Conceptual Data Model

### Task Given

The task required a conceptual data model for an E Commerce system
containing the entities Product, Order, Customer, and Cart and
representing the relationships between them.

### Implementation

The project contains a Mermaid based conceptual data model in
`diagram.md`.

The model contains the following entities and attributes:

1.  `CUSTOMER`
    -   `customer_id`
    -   `name`
    -   `email`
2.  `CART`
    -   `cart_id`
    -   `customer_id`
3.  `PRODUCT`
    -   `product_id`
    -   `name`
    -   `price`
4.  `ORDER`
    -   `order_id`
    -   `customer_id`
    -   `order_date`

The diagram represents these relationships:

1.  Customer owns Cart.
2.  Customer places Order.
3.  Cart contains Product.
4.  Order includes Product.

A separate `model.txt` file is also present in the task folder.

### Code Location

[diagram.md](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture15/Task2_Ecommerce_Model/diagram.md)

[model.txt](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture15/Task2_Ecommerce_Model/model.txt)

[Task 2
Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture15/Task2_Ecommerce_Model)

### Screenshot

No screenshot of the rendered Task 2 diagram was available in the
supplied project evidence, so no screenshot link is included.

### Result

The conceptual E Commerce data model was documented using Mermaid
notation with the required Customer, Cart, Product, and Order entities
and their relationships.

## Task 3: Mongoose Blog Models

### Task Given

The task required creation of Mongoose schemas for a Blog application
containing Post and Comment models.

### Implementation

The implementation is a Node.js application using Mongoose and MongoDB.

A connection is established with the local MongoDB database:

`blog_database`

Two Mongoose schemas are implemented:

1.  `Post`
    -   `title`
    -   `content`
    -   `author`
2.  `Comment`
    -   `text`
    -   `author`
    -   `postId`

The `postId` field references the `Post` model.

The application implements the following operations:

1.  Connect to MongoDB.
2.  Create a sample post when the post does not already exist.
3.  Read all posts.
4.  Create a comment associated with the existing post.
5.  Read all comments.
6.  Display the related post title for each comment.

The application output confirms successful MongoDB connection, post
retrieval, comment creation, and comment retrieval.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture15/Task3_Mongoose_Blog/app.js)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture15/Task3_Mongoose_Blog/package.json)

[Task 3
Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture15/Task3_Mongoose_Blog)

### Screenshots

![Post creation
result](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task3_Mongoose_Blog/screenshots/task3-post-created.png)

![Post read
operation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task3_Mongoose_Blog/screenshots/task3-read-post.png)

![Comment creation
result](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task3_Mongoose_Blog/screenshots/task3-comment-created.png)

![Comment read
operation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task3_Mongoose_Blog/screenshots/task3-read-comments.png)

### Result

The Mongoose application successfully connected to MongoDB, created or
retrieved the sample post, displayed post data, created a comment
associated with the post, and retrieved comments together with the
related post information.

## Task 4: Data Validation

### Task Given

The task required validation rules to ensure data integrity, including
required fields, valid email values, and valid fixed values.

### Implementation

The actual implementation uses FastAPI and Pydantic for request
validation.

The `StudentCreate` model validates:

1.  `name` as a required string with length restrictions.
2.  `email` using Pydantic `EmailStr`.
3.  `branch` using a regular expression that permits CSE, ECE, IT, ME,
    or CE.
4.  `enrollment_date` as an optional date.

A `StudentResponse` model defines the response structure.

A `POST /students` endpoint accepts validated student data and returns a
student record with a generated ID and HTTP status `201`.

The validation was tested using FastAPI Swagger UI with:

1.  Valid student data.
2.  Invalid email.
3.  Invalid branch.
4.  Missing required branch.

The invalid inputs produced HTTP `422 Unprocessable Content` validation
responses.

The actual implementation in this task uses FastAPI and Pydantic
validation. No Mongoose validation implementation was added to this
task.

### Code Location

[app.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture15/Task4_Data_Validation/app.py)

[Task 4
Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture15/Task4_Data_Validation)

### Screenshots

![Valid student request with HTTP 201
response](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task4_Data_Validation/screenshots/task4-valid-student.png)

![Invalid email
validation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task4_Data_Validation/screenshots/task4-invalid-email.png)

![Invalid branch
validation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task4_Data_Validation/screenshots/task4-invalid-branch.png)

![Missing required branch
validation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture15/Task4_Data_Validation/screenshots/task4-missing-branch.png)

### Result

The FastAPI validation endpoint successfully accepted valid student data
with HTTP `201`. Invalid email values, invalid branch values, and
missing required branch data were rejected with HTTP `422` validation
errors.

## Project Structure

``` text
BackendDevelopment/
└── Theory/
    └── Unit2/
        └── Lecture15/
            ├── Task1_Data_Modeling/
            │   ├── model.py
            │   ├── students.db
            │   └── screenshots/
            │       ├── task1-crud-operations.png
            │       ├── task1-database-created.png
            │       ├── task1-student-created.png
            │       └── task1-update-student.png
            │
            ├── Task2_Ecommerce_Model/
            │   ├── diagram.md
            │   └── model.txt
            │
            ├── Task3_Mongoose_Blog/
            │   ├── app.js
            │   ├── package.json
            │   ├── package-lock.json
            │   └── screenshots/
            │       ├── task3-comment-created.png
            │       ├── task3-post-created.png
            │       ├── task3-read-comments.png
            │       └── task3-read-post.png
            │
            └── Task4_Data_Validation/
                ├── app.py
                └── screenshots/
                    ├── task4-invalid-branch.png
                    ├── task4-invalid-email.png
                    ├── task4-missing-branch.png
                    └── task4-valid-student.png
```

## Concepts Used

1.  Conceptual data modeling
2.  Entity and relationship modeling
3.  Logical data modeling
4.  SQLAlchemy ORM
5.  SQLite database interaction
6.  Primary keys
7.  Foreign keys
8.  Unique constraints
9.  SQLAlchemy relationships
10. Create, Read, Update, and Delete operations
11. MongoDB
12. Mongoose ODM
13. Mongoose schemas
14. ObjectId references
15. MongoDB document retrieval
16. FastAPI
17. Pydantic models
18. Email validation
19. Pattern based validation
20. Required field validation
21. HTTP status codes
22. Swagger UI API testing

## Overall Result

The experiment successfully demonstrated the complete data modeling
workflow across conceptual modeling, relational ORM implementation,
document based ODM implementation, and API level data validation.

The implemented project contains an E Commerce conceptual model, a
SQLAlchemy Student Management implementation with CRUD operations, a
Mongoose Blog implementation using MongoDB, and a FastAPI and Pydantic
validation implementation.

## Observations

1.  SQLAlchemy maps Python model classes to relational database tables
    and supports relationships using foreign keys and ORM relationships.
2.  The Student Management implementation uses SQLite through the
    `students.db` database file.
3.  The `email` field in the Student model is configured as unique, so
    duplicate email values are rejected by the database.
4.  Mongoose provides schema based modeling for MongoDB documents.
5.  The Blog implementation uses an ObjectId reference from Comment to
    Post.
6.  FastAPI validates request bodies through Pydantic before the
    endpoint processes the request.
7.  Invalid email and branch values produced HTTP `422` validation
    responses.
8.  Missing required fields also produced HTTP `422` validation
    responses.
9.  The Task 4 implementation validates data in memory and does not
    persist the validated student records to a database.
10. The experiment demonstrates that validation and database modeling
    are complementary parts of backend application development.

## Conclusion

The experiment demonstrated how backend applications translate business
requirements into structured data models and validation rules.
SQLAlchemy was used to model relational data and perform database
operations, Mongoose was used to define MongoDB document schemas and
relationships, and FastAPI with Pydantic was used to validate API input.
The practical implementation shows how conceptual models, ORM and ODM
schemas, CRUD operations, and validation contribute to reliable backend
data handling.

## Experiment Link

This Lecture 15 implementation was not published as a separate GitHub
Pages experiment. The complete source is available in the GitHub
repository below.

## Complete Experiment Source Code

[Lecture 15 Complete
Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture15)

[BackendDevelopment GitHub
Repository](https://github.com/sehajvohra/BackendDevelopment)
