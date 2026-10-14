# Lecture 13

## Title

Introduction to Databases

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

To understand the basic operations of database systems by implementing student data management in PostgreSQL and MongoDB. The practical demonstrates database creation, table creation, record insertion, filtering, updating, deleting, final verification, and a comparison between relational and document-oriented database models.

## Software Requirements

1. Visual Studio Code
2. PostgreSQL
3. MongoDB
4. MongoDB Shell or MongoDB Playground
5. Terminal or command-line interface

## Problem Statement

Create and manage a student database using PostgreSQL and MongoDB. In PostgreSQL, create a database and a `students` table, insert student records, retrieve records using conditions, update a record, delete a record, and verify the final table data. In MongoDB, create/select the student management database, insert student documents, retrieve students from the CSE branch, and compare PostgreSQL with MongoDB.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Create a PostgreSQL database and students table | `student_management` database and `students` table defined in `lecture13.sql` |
| Task 2 | Insert and retrieve student records in PostgreSQL | Five records inserted and filtered using SQL `SELECT` queries |
| Task 3 | Update, delete, and verify PostgreSQL data | Student branch updated, one record deleted, and final records selected |
| Task 4 | Perform MongoDB student document operations | `student_management` database selected, three documents inserted, and CSE students queried |
| Task 5 | Compare PostgreSQL and MongoDB | Comparison notes included in `mongodb.js` |

## Task 1: PostgreSQL Database and Table Creation

### Task Given

Create a database for student management and define a table to store student details.

### Implementation

The PostgreSQL script creates a database named `student_management`. It defines a `students` table with the following fields:

1. `id` as an automatically generated identity primary key
2. `name` as a required text field
3. `branch` as a required text field
4. `email` as a unique and required field
5. `enrollment_date` as a date field

### Code Location

[lecture13.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture13/lecture13.sql)

### Screenshots

![PostgreSQL database created](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-create-database.png)

![PostgreSQL students table created](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-create-students-table.png)

### Result

The `student_management` database and `students` table were successfully created in PostgreSQL with suitable constraints for storing student records.

## Task 2: Insert and Retrieve Student Records in PostgreSQL

### Task Given

Insert sample student records into the PostgreSQL table and retrieve records using conditional queries.

### Implementation

The SQL script inserts five student records into the `students` table. The records include student names, branches, email addresses, and enrollment dates.

Two conditional retrieval queries are implemented:

1. Retrieve all students from the CSE branch.
2. Retrieve students enrolled after January 2024.

### Code Location

[lecture13.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture13/lecture13.sql)

### Screenshots

![Student records inserted in PostgreSQL](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-insert-students.png)

![CSE students selected in PostgreSQL](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-select-cse-students.png)

![Students enrolled after January 2024 selected in PostgreSQL](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-select-enrolled-after-jan-2024.png)

### Result

Five student records were inserted successfully. The PostgreSQL `SELECT` queries returned branch-specific records and date-filtered records as expected.

## Task 3: Update, Delete, and Verify PostgreSQL Data

### Task Given

Modify an existing student record, delete a student record, and verify the final table contents.

### Implementation

The SQL script updates the branch of the student with `id = 1` to `ECE`. It then deletes the student record with `id = 3`.

After these operations, a final verification query retrieves all remaining student records ordered by `id`.

### Code Location

[lecture13.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture13/lecture13.sql)

### Screenshots

![Student branch updated in PostgreSQL](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-update-student.png)

![Student record deleted in PostgreSQL](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-delete-student.png)

![Final PostgreSQL student records verified](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-final-students.png)

### Result

The update and delete operations were completed successfully. The final verification query showed the remaining student records after modification and deletion.

## Task 4: MongoDB Student Document Operations

### Task Given

Perform basic student data operations using MongoDB and retrieve students from a specific branch.

### Implementation

The MongoDB script selects the `student_management` database and inserts three student documents into the `students` collection. Each document stores the student's name, branch, email, and enrollment date.

The script then retrieves students whose branch is `CSE` using a MongoDB `find()` query with a branch filter.

### Code Location

[mongodb.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture13/mongodb.js)

### Screenshots

![MongoDB student management database selected](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-mongodb-database.png)

![Student documents inserted in MongoDB](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-mongodb-insert-students.png)

![CSE students selected in MongoDB](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-mongodb-select-cse.png)

### Result

The student documents were inserted successfully into MongoDB. The filter query returned the student documents belonging to the CSE branch.

## Task 5: PostgreSQL and MongoDB Comparison

### Task Given

Compare PostgreSQL and MongoDB based on their database model, structure, query approach, and suitable use cases.

### Implementation

The comparison is documented as comments in `mongodb.js`. PostgreSQL is described as a relational database that uses tables, rows, columns, SQL queries, fixed schemas, and foreign keys. MongoDB is described as a document database that uses collections, documents, MongoDB query methods, and flexible document structures.

### Code Location

[mongodb.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture13/mongodb.js)

### Screenshot

![CSE students selected in MongoDB](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture13/screenshots/lecture13-mongodb-select-cse.png)

### Result

The practical highlighted the difference between relational and document-oriented databases. PostgreSQL was used for structured tabular data, while MongoDB was used for flexible document-based storage.

## Project Structure

```text
Theory/
+-- Unit2/
    +-- Lecture13/
        +-- screenshots/
        |   +-- lecture13-create-database.png
        |   +-- lecture13-create-students-table.png
        |   +-- lecture13-delete-student.png
        |   +-- lecture13-final-students.png
        |   +-- lecture13-insert-students.png
        |   +-- lecture13-mongodb-database.png
        |   +-- lecture13-mongodb-insert-students.png
        |   +-- lecture13-mongodb-select-cse.png
        |   +-- lecture13-select-cse-students.png
        |   +-- lecture13-select-enrolled-after-jan-2024.png
        |   +-- lecture13-update-student.png
        +-- lecture13.sql
        +-- mongodb.js
        +-- Report.md
```

## Concepts Used

1. Relational database creation
2. PostgreSQL table creation
3. Primary key constraint
4. Identity column generation
5. `NOT NULL` and `UNIQUE` constraints
6. SQL `INSERT` operation
7. SQL `SELECT` queries
8. Filtering data using `WHERE`
9. Date-based filtering
10. SQL `UPDATE` operation
11. SQL `DELETE` operation
12. Final data verification using `ORDER BY`
13. MongoDB database selection
14. MongoDB collections and documents
15. MongoDB `insertMany()` operation
16. MongoDB `find()` query
17. Relational database and NoSQL database comparison

## Overall Result

The practical successfully implemented student data management using both PostgreSQL and MongoDB. PostgreSQL was used to create a structured table, insert records, retrieve filtered data, update a record, delete a record, and verify the final output. MongoDB was used to store student data as documents and retrieve CSE branch students using a document query.

## Observations

1. PostgreSQL stores data in structured tables with fixed columns and constraints.
2. The `id` column uniquely identifies each student record in the PostgreSQL table.
3. The `email` column uses a unique constraint to prevent duplicate email addresses.
4. SQL `WHERE` clauses allow records to be filtered by branch and enrollment date.
5. Update and delete operations modify the stored table data permanently after execution.
6. MongoDB stores student information as flexible documents inside a collection.
7. MongoDB queries use object-style filters instead of SQL syntax.
8. PostgreSQL is suitable for strongly structured relational data, while MongoDB is suitable for flexible document-based data.

## Conclusion

This practical demonstrated the basic use of PostgreSQL and MongoDB for backend data storage. The PostgreSQL implementation showed database creation, table definition, constraints, insertion, querying, updating, deletion, and final verification. The MongoDB implementation showed document insertion and filtered retrieval. The experiment also helped compare relational and NoSQL database approaches in a practical student management context.

## Experiment Link

[Lecture 13 GitHub Pages Report](https://sehajvohra.github.io/BackendDevelopment/Theory/Unit2/Lecture13/Report.html)

[Complete Lecture 13 Source Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture13)

[lecture13.sql](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture13/lecture13.sql)

[mongodb.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture13/mongodb.js)
