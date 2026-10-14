# Experiment 5

## Title

RESTful APIs and FastAPI

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

To design and implement a RESTful Course Management API using FastAPI, demonstrate CRUD operations, apply request validation using Pydantic models, use query parameters for filtering, and verify automatically generated API documentation.

## Software Requirements

- Python
- FastAPI
- Uvicorn
- Pydantic
- Browser
- Swagger UI
- ReDoc
- Visual Studio Code or any code editor

## Problem Statement

The experiment requires building a RESTful API using FastAPI for managing course resources. The API should support creating, reading, updating, deleting, and filtering course records. The implementation should also demonstrate FastAPI's automatic documentation support through generated API documentation.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Create a FastAPI course resource API | Implemented a FastAPI application titled `Course Management API` with Pydantic models for course data. |
| Task 2 | Retrieve course records | Implemented `GET /courses` and `GET /courses/{course_id}` endpoints. |
| Task 3 | Filter courses by department | Implemented `GET /courses?department=CSE` using an optional query parameter. |
| Task 4 | Create a new course | Implemented `POST /courses` with request body validation and `201 Created` status code. |
| Task 5 | Update and delete courses | Implemented `PUT /courses/{course_id}` and `DELETE /courses/{course_id}` endpoints. |
| Task 6 | Verify API documentation | Verified generated ReDoc documentation for the FastAPI application. |

## Task 1: Create a FastAPI Course Resource API

### Task Given

The task required creating a RESTful API using FastAPI for a `Course` resource with fields such as `id`, `title`, `credits`, and `department`.

### Implementation

A FastAPI application named `Course Management API` was implemented in `main.py`. The project defines two Pydantic models: `Course` for complete course records and `CourseCreate` for create and update request bodies. The API uses an in-memory list of course objects as the data source and runs with Uvicorn on `127.0.0.1:5000`.

### Code Location

- [Lecture 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5)
- [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture5/main.py)

### Screenshot

![ReDoc documentation for Course Management API](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture5/screenshots/L05_ReDoc_Documentation.png)

### Result

The FastAPI application was successfully created with typed request and response models, automatic validation support, and generated API documentation.

## Task 2: Retrieve Course Records

### Task Given

The task required implementing read operations for retrieving all courses and retrieving a single course by ID.

### Implementation

The API implements `GET /courses` to return all available course records and `GET /courses/{course_id}` to return a specific course by ID. If a requested course ID is not found, the implementation raises an `HTTPException` with status code `404` and the message `Course not found`.

### Code Location

- [Lecture 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5)
- [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture5/main.py)

### Screenshots

![GET all courses](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture5/screenshots/L05_GET_All_Courses.png)

![GET course by ID](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture5/screenshots/L05_GET_Course_By_ID.png)

### Result

The API successfully returned all course records and also returned an individual course when a valid course ID was provided.

## Task 3: Filter Courses by Department

### Task Given

The task required adding a query parameter to filter courses by department, such as `GET /courses?department=CSE`.

### Implementation

The `GET /courses` endpoint accepts an optional `department` query parameter using FastAPI's `Query`. When a department is provided, the API filters the in-memory course list by comparing department values in a case-insensitive manner. If no department is provided, all courses are returned.

### Code Location

- [Lecture 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5)
- [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture5/main.py)

### Screenshot

![GET courses filtered by CSE department](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture5/screenshots/L05_GET_Courses_Filter_CSE.png)

### Result

The API successfully filtered course records by department and returned matching course objects for the `CSE` department query.

## Task 4: Create a New Course

### Task Given

The task required implementing a POST endpoint to create a new course record using request body data.

### Implementation

The API implements `POST /courses` using the `CourseCreate` Pydantic model for request validation. The server assigns the next available course ID using the `next_id` variable, appends the new course to the in-memory list, increments the ID counter, and returns the created course with status code `201`.

### Code Location

- [Lecture 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5)
- [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture5/main.py)

### Screenshot

![POST create course](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture5/screenshots/L05_POST_Create_Course.png)

### Result

The API successfully accepted course data, created a new course object with an automatically assigned ID, and returned the created resource with the correct creation status.

## Task 5: Update and Delete Courses

### Task Given

The task required implementing update and delete operations for existing course records using RESTful routes.

### Implementation

The API implements `PUT /courses/{course_id}` to replace an existing course with updated `title`, `credits`, and `department` values. It also implements `DELETE /courses/{course_id}` to remove a course from the in-memory list. Both endpoints search for the course by ID, and if no matching course is found, they raise a `404` error with `Course not found`.

### Code Location

- [Lecture 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5)
- [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture5/main.py)

### Screenshots

![PUT update course](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture5/screenshots/L05_PUT_Update_Course.png)

![DELETE course](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture5/screenshots/L05_DELETE_Course.png)

### Result

The API successfully updated existing course records and deleted course records through RESTful endpoints. The delete endpoint uses status code `204`, which indicates successful deletion with no response body.

## Task 6: Verify API Documentation

### Task Given

The task required verifying that FastAPI generated API documentation for the implemented REST API.

### Implementation

FastAPI automatically generated documentation from route definitions, Pydantic models, request bodies, response models, and status codes. The available screenshot verifies ReDoc documentation for the Course Management API. No separate Swagger UI screenshot is present in the project folder, so only the verified ReDoc screenshot is included.

### Code Location

- [Lecture 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5)
- [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture5/main.py)

### Screenshot

![ReDoc documentation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture5/screenshots/L05_ReDoc_Documentation.png)

### Result

The generated ReDoc documentation successfully displayed the implemented course endpoints and schemas based on the FastAPI application.

## Project Structure

```text
Theory/Unit1/Lecture5/
+-- main.py
+-- screenshots/
|   +-- L05_DELETE_Course.png
|   +-- L05_GET_All_Courses.png
|   +-- L05_GET_Courses_Filter_CSE.png
|   +-- L05_GET_Course_By_ID.png
|   +-- L05_POST_Create_Course.png
|   +-- L05_PUT_Update_Course.png
|   +-- L05_ReDoc_Documentation.png
+-- Report.md
```

## Concepts Used

- RESTful API design
- FastAPI application development
- Pydantic request and response models
- Type hints with `List` and `Optional`
- Query parameters using `Query`
- Path parameters
- CRUD operations
- HTTP status codes
- `HTTPException` error handling
- Uvicorn server execution
- Auto-generated API documentation with ReDoc

## Overall Result

The experiment successfully implemented a RESTful Course Management API using FastAPI. The API supports listing courses, retrieving a course by ID, filtering by department, creating a course, updating a course, deleting a course, and viewing generated ReDoc documentation.

## Observations

- The actual implementation manages a `Course` resource, not the `Student` resource shown in the lecture example.
- The API uses an in-memory Python list, so data changes are temporary and reset when the server restarts.
- `CourseCreate` excludes the `id` field because IDs are generated by the server.
- The `GET /courses` endpoint supports optional department filtering.
- The `POST /courses` endpoint returns status code `201`.
- The `DELETE /courses/{course_id}` endpoint returns status code `204`.
- Missing course IDs are handled using `HTTPException` with status code `404`.
- A ReDoc screenshot exists and is included; no Swagger UI screenshot file is present in the verified project folder.
- The implemented screenshots are stored under `Theory/Unit1/Lecture5/screenshots/`, not under `Lab/Exp 5/screenshots/`.

## Conclusion

This experiment demonstrated the development of a RESTful API using FastAPI. The implemented Course Management API followed REST principles through resource-based routes, appropriate HTTP methods, response models, validation, status codes, and generated documentation. The practical work confirms how FastAPI can be used to create structured, documented, and testable backend APIs.

## Experiment Link

GitHub Pages Link: Not published as a GitHub Pages experiment because the implementation requires a local FastAPI server.

Complete Experiment Source Code: [Theory/Unit1/Lecture5](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture5)
