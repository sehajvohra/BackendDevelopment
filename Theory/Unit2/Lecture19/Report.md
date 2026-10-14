# Lecture 19

## Title

Implementing RESTful APIs: Building API Endpoints

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

To implement RESTful API endpoints using FastAPI and SQLAlchemy, configure database connectivity, define database models and Pydantic schemas, implement student CRUD operations, develop course and enrollment endpoints, and verify API behavior through automated testing.

## Software Requirements

1. Python
2. FastAPI
3. Uvicorn
4. SQLAlchemy
5. Pydantic
6. SQLite
7. Python dotenv
8. Pytest
9. HTTPX and FastAPI TestClient
10. Visual Studio Code
11. Web browser for Swagger UI

## Problem Statement

Develop a RESTful API for managing student, department, course, and enrollment data. The implementation should provide database connectivity, structured data models, request validation, student CRUD operations, course management, enrollment management, appropriate HTTP responses, and API testing.

The implementation is organized into seven tasks covering project setup, database configuration, database models, Pydantic schemas, student CRUD operations, course and enrollment operations, and automated testing.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Project Setup | Created the FastAPI project with application, database, model, schema, and dependency configuration files. |
| Task 2 | Database Configuration | Configured SQLAlchemy database connectivity and database session management. |
| Task 3 | Database Models | Defined Department, Student, Course, and Enrollment models. |
| Task 4 | Pydantic Schemas | Defined schemas for structured input validation and response handling. |
| Task 5 | Student CRUD API | Implemented student creation, listing, retrieval, updating, deletion, filtering, and pagination. |
| Task 6 | Courses and Enrollments | Implemented course listing and creation, enrollment listing and creation, and enrollment deletion. |
| Task 7 | Final Testing | Created automated tests for student creation, listing, missing student handling, and invalid input validation. |

## Task 1: Project Setup

### Task Given

Set up a FastAPI application with the files and dependencies required to build database integrated RESTful APIs.

### Implementation

The project was organized into separate task folders. The initial application setup contains the main application, SQLAlchemy models, Pydantic schemas, database configuration, environment settings, and dependency requirements.

The application uses FastAPI to define API endpoints and SQLAlchemy to interact with the database.

### Code Location

* [Task 1 Project Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19/Task1_Project_Setup)
* [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/main.py)
* [database.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/database.py)
* [models.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/models.py)
* [schemas.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/schemas.py)
* [requirements.txt](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/requirements.txt)

### Screenshot

![Project setup and application files](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task1_Project_Setup/screenshots/task1-project-setup.png)
### Result

The initial FastAPI project structure was created, and the application files required for database integration and API development were established.

## Task 2: Database Configuration

### Task Given

Configure database connectivity and provide a mechanism for API endpoints to access and manage database sessions.

### Implementation

The database configuration uses SQLAlchemy to create the database engine and session factory. The application uses SQLite as its default database configuration and provides a `get_db()` dependency to supply database sessions to API endpoints.

The configuration supports environment based database settings through the `.env` file.

### Code Location

* [Database Configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/database.py)
* [Environment Configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/.env)
* [Task 2 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19/Task2_Database_Configuration)

### Screenshot

![Database configuration](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task2_Database_Configuration/screenshots/task2-database-configuration.png)
### Result

Database engine creation and session management were configured for use by the FastAPI application.

## Task 3: Database Models

### Task Given

Define SQLAlchemy models representing the entities required for the student and course management system.

### Implementation

The project defines four database models:

1. **Department:** Represents department information.
2. **Student:** Represents student information, including name, email, branch, and related database fields.
3. **Course:** Represents course information, including course identifiers, credits, and department association.
4. **Enrollment:** Represents the association between students and courses, including enrollment related information.

These models establish the database structure used by the API endpoints.

### Code Location

* [models.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/models.py)
* [Task 3 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19/Task3_Database_Models)

### Screenshot

![SQLAlchemy database models](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task3_Database_Models/screenshots/task3-database-models.png)
### Result

The SQLAlchemy models for departments, students, courses, and enrollments were defined for database operations.

## Task 4: Pydantic Schemas

### Task Given

Create Pydantic schemas for validating incoming API data and structuring responses returned by the application.

### Implementation

The project defines schemas for the department, student, course, and enrollment entities. These schemas support request validation and response formatting.

Student input validation was tested by submitting an invalid email address to the API. The application rejected the invalid data with HTTP status code `422 Unprocessable Entity`.

### Code Location

* [schemas.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/schemas.py)
* [Task 4 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19/Task4_Pydantic_Schemas)

### Screenshot

![Pydantic schemas](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task4_Pydantic_Schemas/screenshots/task4-pydantic-schemas.png)
### Result

Pydantic schemas were established for request validation and response data handling. Invalid student input was rejected during API testing.

## Task 5: Student CRUD API

### Task Given

Implement RESTful endpoints to create, retrieve, update, and delete student records. Provide student listing functionality with filtering and pagination.

### Implementation

The Student API was implemented in the main FastAPI application.

The implemented functionality includes:

1. **Create student:** Accepts student details and creates a student record.
2. **List students:** Returns student records using a paginated response containing data and pagination metadata.
3. **Retrieve student:** Retrieves a student using the student identifier accepted by the endpoint.
4. **Update student:** Updates existing student information.
5. **Delete student:** Deletes a student record.
6. **Filtering:** Supports branch, department, and search filters.
7. **Pagination:** Supports paginated student listing.

The API was tested using Swagger UI. Testing demonstrated successful student creation, listing, retrieval, updating, and deletion. The student branch was updated to ECE during testing. A subsequent retrieval after deletion returned a not found response, and invalid email input produced a validation error.

### Code Location

* [Student CRUD API](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/main.py)
* [Student Database Model](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/models.py)
* [Student Schemas](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task1_Project_Setup/schemas.py)
* [Task 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API)

### Screenshots

![Student API in Swagger UI](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API/screenshots/task5-student-api-swagger.png)

![Create student](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API/screenshots/task5-create-student.png)

![List students](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API/screenshots/task5-list-students.png)

![Retrieve student](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API/screenshots/task5-get-student.png)

![Update student](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API/screenshots/task5-update-student.png)

![Delete student](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API/screenshots/task5-delete-student.png)

![Verify student deletion](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API/screenshots/task5-verify-student-deletion.png)

![Student input validation error](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task5_Student_CRUD_API/screenshots/task5-validation-error.png)
### Result

The Student API was tested successfully for its principal CRUD operations, filtering, pagination, and request validation. The application returned appropriate successful responses and handled deletion and invalid input cases.

## Task 6: Courses and Enrollments

### Task Given

Extend the API to manage courses and student enrollments, including the creation, retrieval, and deletion of enrollment records.

### Implementation

A separate application was created inside `Task6_Courses_And_Enrollments`. It contains its own application, database configuration, models, schemas, requirements, environment configuration, and supporting test data script.

The implemented endpoints include:

| Method | Endpoint | Functionality |
|---|---|---|
| GET | `/courses` | Lists courses with department and credit filters. |
| POST | `/courses` | Creates a course. |
| GET | `/students/{student_id}/enrollments` | Lists enrollments for a student. |
| POST | `/students/{student_id}/enrollments` | Creates a student enrollment. |
| DELETE | `/students/{student_id}/enrollments/{course_id}` | Deletes a student enrollment. |

The course API was tested by creating the course `BD101`, named Backend Development, with four credits. The enrollment workflow was tested with a student record and the course. An existing enrollment produced a conflict response when a duplicate creation was attempted. The enrollment was subsequently deleted, and a follow up request returned an empty enrollment list.

### Code Location

* [Task 6 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments)
* [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/main.py)
* [database.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/database.py)
* [models.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/models.py)
* [schemas.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/schemas.py)
* [create_test_student.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/create_test_student.py)

### Screenshots

![Courses and enrollments API in Swagger UI](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/screenshots/task6-courses-enrollments-swagger.png)

![Create course](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/screenshots/task6-create-course.png)

![List courses](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/screenshots/task6-list-courses.png)

![List student enrollments](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/screenshots/task6-list-enrollments.png)

![Delete enrollment](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/screenshots/task6-delete-enrollment.png)

![Verify enrollment deletion](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task6_Courses_And_Enrollments/screenshots/task6-verify-enrollment-deletion.png)
### Result

Course and enrollment endpoints were implemented and tested. Course creation, course listing, enrollment retrieval, duplicate enrollment handling, enrollment deletion, and verification of the deleted enrollment were demonstrated.

## Task 7: Final Testing

### Task Given

Create automated tests to verify student API operations, listing responses, missing student handling, and validation of invalid input.

### Implementation

A separate automated test file, `test_api.py`, was created in `Task7_Final_Testing`. The test setup imports the application from Task 1 and overrides its database dependency to use a separate temporary SQLite database.

The automated test suite contains four tests:

1. Student creation.
2. Student listing and validation of the paginated response structure.
3. Handling a student identifier that does not exist.
4. Rejection of invalid student data.

The tests were executed using Pytest. The final run completed with **four passing tests**. Five warnings were reported, relating to deprecated TestClient usage and Pydantic configuration. These warnings did not prevent the tests from passing.

### Code Location

* [Task 7 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19/Task7_Final_Testing)
* [test_api.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task7_Final_Testing/test_api.py)
* [requirements.txt](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit2/Lecture19/Task7_Final_Testing/requirements.txt)

### Screenshot

![Automated test results showing four passing tests](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit2/Lecture19/Task7_Final_Testing/screenshots/task7-automated-tests-passed.png)
### Result

The automated test suite completed with four passing tests. The tests verified student creation, the paginated listing response, handling of a missing student, and rejection of invalid input.

## Project Structure

```text
Lecture19/
├── Report.md
├── Task1_Project_Setup/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   ├── .env
│   └── screenshots/
│       └── task1-project-setup.png
├── Task2_Database_Configuration/
│   └── screenshots/
│       └── task2-database-configuration.png
├── Task3_Database_Models/
│   └── screenshots/
│       └── task3-database-models.png
├── Task4_Pydantic_Schemas/
│   └── screenshots/
│       └── task4-pydantic-schemas.png
├── Task5_Student_CRUD_API/
│   └── screenshots/
│       ├── task5-student-api-swagger.png
│       ├── task5-create-student.png
│       ├── task5-list-students.png
│       ├── task5-get-student.png
│       ├── task5-update-student.png
│       ├── task5-delete-student.png
│       ├── task5-verify-student-deletion.png
│       └── task5-validation-error.png
├── Task6_Courses_And_Enrollments/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   ├── .env
│   ├── create_test_student.py
│   └── screenshots/
│       ├── task6-courses-enrollments-swagger.png
│       ├── task6-create-course.png
│       ├── task6-list-courses.png
│       ├── task6-list-enrollments.png
│       ├── task6-delete-enrollment.png
│       └── task6-verify-enrollment-deletion.png
└── Task7_Final_Testing/
    ├── test_api.py
    ├── requirements.txt
    └── screenshots/
        └── task7-automated-tests-passed.png
```
## Concepts Used

1. RESTful API design and HTTP methods.
2. FastAPI application and endpoint development.
3. SQLAlchemy database engine and session management.
4. SQLite database integration.
5. Object relational mapping through database models.
6. Pydantic request validation and response schemas.
7. CRUD operations.
8. Query parameters and filtering.
9. Pagination and structured API responses.
10. Course and enrollment relationships.
11. HTTP status codes and error handling.
12. Duplicate resource and enrollment conflict handling.
13. Automated testing using Pytest.
14. FastAPI TestClient and dependency overrides.
15. Temporary SQLite databases for isolated tests.
16. Interactive API testing through Swagger UI.

## Overall Result

The Lecture 19 project implemented a FastAPI based student and course management API with SQLAlchemy database integration and Pydantic validation. Student CRUD operations, filtering, pagination, course management, and enrollment management were implemented and tested.

The final automated test suite completed with four passing tests, confirming the tested student API operations and validation behavior.

## Observations

1. SQLAlchemy provides database session management and object relational mapping for the application.
2. Pydantic schemas validate incoming request data and help maintain consistent response structures.
3. The student listing endpoint returns a paginated object containing student data and pagination metadata rather than a plain list.
4. Invalid student input is rejected with HTTP `422 Unprocessable Entity`.
5. Missing student handling depends on the identifier format accepted by the endpoint and the route's validation behavior.
6. Course and enrollment endpoints support related resource operations and duplicate enrollment handling.
7. Using a separate temporary database for automated testing prevents the tests from modifying the application's normal database records.
8. The final test run passed all four tests. The reported deprecation warnings did not cause test failures.

## Conclusion

This practical demonstrated the implementation and testing of RESTful APIs using FastAPI, SQLAlchemy, SQLite, and Pydantic. The project covered database configuration, model definition, schema validation, student CRUD operations, course and enrollment management, and automated testing. The successful final test run confirmed the behavior of the four tested student API scenarios.

## Experiment Link

[Backend Development GitHub Pages](https://sehajvohra.github.io/BackendDevelopment/)

## Complete Source Code

[Lecture 19: Implementing RESTful APIs: Building API Endpoints](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit2/Lecture19)
