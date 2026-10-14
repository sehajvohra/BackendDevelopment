# Experiment 4

## Title

HTTP Requests, DevTools, CURL, Postman, and fetch

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

To understand the structure of HTTP requests and responses, inspect API communication using Browser DevTools, curl, and Postman, and compare how the same API response can be tested across Express.js and Flask implementations.

## Software Requirements

- Node.js
- npm
- Express.js
- Python
- Flask
- Browser DevTools
- curl
- Postman
- Visual Studio Code or any code editor

## Problem Statement

The experiment requires creating and inspecting simple student API endpoints using backend servers and API testing tools. The request-response cycle must be observed through Browser DevTools, curl, and Postman. The same HTTP concepts must also be verified using a Flask server to show that HTTP communication is independent of the backend framework.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Inspect a GET request using Browser DevTools | Implemented an Express.js student API and captured the `/students` request in Browser DevTools. |
| Task 2 | Send requests using curl | Used the same Express.js API to verify verbose output, single-student lookup, and response headers through curl. |
| Task 3 | Send requests using Postman | Tested the Express.js API in Postman, including GET requests, an `Accept` header, and an unsupported POST request result. |
| Task 4 | Compare the same request across three tools | Tested `GET /students/2` using Browser DevTools, curl, and Postman. |
| Task 5 | Inspect a Flask server | Implemented a Flask version of the student API and tested it using curl and Postman. |

## Task 1: Inspect a Request Using Browser DevTools

### Task Given

The task required starting an Express server, opening Browser DevTools, sending a request to `http://localhost:3000/students`, and inspecting the request method, request URL, response status, response headers, and JSON response body.

### Implementation

An Express.js server was implemented with an in-memory `students` array. The server exposes a home route, a `/students` route that returns all students as JSON, and a `/students/:id` route that returns a single student or a `404` JSON error when the student is not found. Browser DevTools was used to inspect the `GET /students` request and view the JSON response.

### Code Location

- [Task 1 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4/Task1)
- [server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task1/server.js)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task1/package.json)

### Screenshots

![Browser DevTools GET students request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task1/screenshots/01_DevTools_GET_students.png%20%281%29.png)

![Browser DevTools response body](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task1/screenshots/02_DevTools_Response.png)

### Result

The Express.js API successfully returned the student list as JSON for `GET /students`, and Browser DevTools displayed the request-response details, including the request method, response status, headers, and response body.

## Task 2: Send Requests Using curl

### Task Given

The task required using curl to send GET requests to the Express.js server, inspect verbose request-response details, request a single student, test a missing student, and include response headers in the output.

### Implementation

The same Express.js student API was implemented for command-line testing. curl was used to inspect HTTP traffic for the `/students` and `/students/:id` endpoints. The implementation supports successful JSON responses for existing students and returns a `404` JSON error for missing student IDs.

### Code Location

- [Task 2 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4/Task2)
- [server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task2/server.js)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task2/package.json)

### Screenshots

![curl verbose request and response](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task2/screenshots/01_curl_VERBOSE.png)

![curl student lookup](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task2/screenshots/02_curl_STUDENT_LOOKUP.png)

![curl response headers](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task2/screenshots/03_curl_HEADERS.png)

### Result

curl successfully tested the Express.js routes from the terminal. The verbose and header-inclusive outputs demonstrated the HTTP method, request headers, response headers, status information, and JSON response body.

## Task 3: Send Requests Using Postman

### Task Given

The task required testing the student API using Postman, sending a GET request to `/students`, adding an `Accept: application/json` header, attempting a POST request, and saving the GET request in a Postman collection.

### Implementation

An Express.js server with GET-only student routes was used for Postman testing. Postman was used to send a GET request to retrieve all students and another GET request with an explicit `Accept` header. A POST request was also tested, but the actual implementation does not define a POST route, so the POST request produced an expected error or unsupported-method result rather than creating a new student.

### Code Location

- [Task 3 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4/Task3)
- [server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task3/server.js)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task3/package.json)

### Screenshots

![Postman GET students request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task3/screenshots/01_Postman_GET_students.png)

![Postman Accept header request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task3/screenshots/02_Postman_Accept_Header..png)

![Postman POST expected error](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task3/screenshots/03_Postman_POST_expected_error.png)

![Postman saved GET students request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task3/screenshots/04_Postman_Saved_GET_Students.png)

### Result

Postman successfully displayed the JSON response for GET requests and allowed inspection of status, headers, and body. The POST test showed that the current Express.js implementation does not include a POST endpoint, which matches the actual project code.

## Task 4: Same Request, Three Tools

### Task Given

The task required sending the same request, `GET http://localhost:3000/students/2`, using Browser DevTools, curl, and Postman, then comparing how each tool displays the same HTTP response.

### Implementation

The Express.js API was implemented with a `/students/:id` route. The route parses the ID from the URL parameter and searches the in-memory student list. For ID `2`, the server returns the matching student object as JSON. The same request was tested in Browser DevTools, curl, and Postman.

### Code Location

- [Task 4 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4/Task4)
- [server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task4/server.js)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task4/package.json)

### Screenshots

![Browser DevTools students 2 request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task4/screenshots/01_Browser_DevTools_students_2.png)

![curl students 2 request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task4/screenshots/02_curl_students_2.png)

![Postman students 2 request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task4/screenshots/03_Postman_students_2.png)

### Result

The same `GET /students/2` request returned the same student data across all three tools. Browser DevTools provided browser-based network inspection, curl showed terminal-level HTTP details, and Postman provided a graphical API testing interface.

## Task 5: Flask Server Inspection

### Task Given

The task required starting a Flask server, sending requests to `http://localhost:5000/students`, and inspecting the response using curl and Postman.

### Implementation

A Flask application was implemented with an in-memory `students` list. It provides a home route, a `/students` route for all student records, and a `/students/<int:student_id>` route for fetching one student by ID. The Flask implementation returns JSON responses using `jsonify()` and returns a `404` JSON error when the requested student is not found.

### Code Location

- [Task 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4/Task5)
- [app.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture4/Task5/app.py)

### Screenshots

![Flask curl students request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task5/screenshots/01_Flask_curl_students.png)

![Flask Postman students request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture4/Task5/screenshots/02_Flask_Postman_students.png)

### Result

The Flask server successfully returned JSON student data on port `5000`. curl and Postman confirmed that the HTTP request-response structure remains consistent even when the backend framework changes from Express.js to Flask.

## Project Structure

```text
Theory/Unit1/Lecture4/
+-- Task1/
|   +-- server.js
|   +-- package.json
|   +-- package-lock.json
|   +-- screenshots/
|       +-- 01_DevTools_GET_students.png (1).png
|       +-- 02_DevTools_Response.png
+-- Task2/
|   +-- server.js
|   +-- package.json
|   +-- package-lock.json
|   +-- screenshots/
|       +-- 01_curl_VERBOSE.png
|       +-- 02_curl_STUDENT_LOOKUP.png
|       +-- 03_curl_HEADERS.png
+-- Task3/
|   +-- server.js
|   +-- package.json
|   +-- package-lock.json
|   +-- screenshots/
|       +-- 01_Postman_GET_students.png
|       +-- 02_Postman_Accept_Header..png
|       +-- 03_Postman_POST_expected_error.png
|       +-- 04_Postman_Saved_GET_Students.png
+-- Task4/
|   +-- server.js
|   +-- package.json
|   +-- package-lock.json
|   +-- screenshots/
|       +-- 01_Browser_DevTools_students_2.png
|       +-- 02_curl_students_2.png
|       +-- 03_Postman_students_2.png
+-- Task5/
|   +-- app.py
|   +-- screenshots/
|       +-- 01_Flask_curl_students.png
|       +-- 02_Flask_Postman_students.png
+-- Report.md
```

## Concepts Used

- HTTP request and response cycle
- HTTP methods, status codes, headers, and response body inspection
- Express.js route handling
- Flask route handling
- JSON API responses
- URL parameters
- Browser DevTools Network tab
- curl command-line API testing
- Postman graphical API testing
- Comparison of the same HTTP request across multiple tools

## Overall Result

The experiment successfully demonstrated HTTP request-response inspection using Browser DevTools, curl, and Postman. The Express.js implementation was used for testing multiple API inspection workflows, and the Flask implementation verified that the same HTTP concepts apply across backend frameworks.

## Observations

- The Express.js tasks implement only GET routes for `/`, `/students`, and `/students/:id`.
- The POST request tested in Postman is not supported by the actual Express.js implementation, so it correctly does not create a new student.
- Browser DevTools is useful for observing requests generated from the browser.
- curl is useful for direct terminal-based request testing and header inspection.
- Postman provides a structured interface for testing, saving, and reviewing API requests.
- The Flask task uses different student sample data from the Express tasks but follows the same API structure.
- No separate client-side JavaScript `fetch()` implementation is present in the Lecture 4 project files.
- The implemented screenshot files are stored under `Theory/Unit1/Lecture4/Task*/screenshots/`, not under `Lab/Exp 4/screenshots/`.

## Conclusion

This experiment provided practical understanding of HTTP request and response inspection. The implemented Express.js and Flask APIs demonstrated how JSON endpoints can be tested through Browser DevTools, curl, and Postman. The comparison across tools showed that the underlying HTTP exchange remains the same, while each tool presents the request and response details in a different format.

## Experiment Link

GitHub Pages Link: Not published as a GitHub Pages experiment because the implementation requires local Express.js and Flask servers.

Complete Experiment Source Code: [Theory/Unit1/Lecture4](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture4)
