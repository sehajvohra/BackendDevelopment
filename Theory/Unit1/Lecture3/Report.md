# Lecture 3

## Title

Setting Up the Backend Environment

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

To understand HTTP fundamentals, the request response cycle, backend server setup, and practical implementation of backend servers using Express.js and Flask. The experiment demonstrates multiple routes, JSON responses, HTML responses, EJS templating, and inspection of HTTP requests using browser DevTools.

## Software Requirements

1. Node.js
2. npm
3. Python
4. pip
5. Express.js
6. Flask
7. EJS
8. Visual Studio Code
9. Web browser with Developer Tools

## Problem Statement

The experiment focuses on establishing a backend development environment and implementing basic backend servers using Express.js and Flask. The implementation demonstrates HTTP based communication through routes and responses, including plain text, JSON, HTML, and server side rendered EJS responses. The final task demonstrates observation of the request response cycle through browser DevTools.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Hello World Server | Express server returning a plain text response from the root route |
| Task 2 | Multiple Routes | Express server implementing multiple GET routes |
| Task 3 | Returning JSON Data | Express routes returning student data as JSON |
| Task 4 | Sending HTML Responses | Express routes returning dynamically constructed HTML |
| Task 5 | EJS Templating | Express server rendering home and student pages using EJS |
| Task 6 | Flask Hello World Server | Flask server returning a plain text response |
| Task 7 | Flask Routes and JSON | Flask routes returning student data as JSON |
| Task 8 | Browser DevTools | Express JSON endpoint inspected using browser DevTools |

## Task 1: Hello World Server

### Task Given

The task required creation of a basic Express.js backend server with a root route that returns a simple response.

### Implementation

The project contains a separate Express.js application for Task 1. The application imports Express, creates an Express application, defines a GET route for `/`, and returns the text `Backend Server Running`.

The server listens on port `3000`.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task1_Hello_World_Server/server.js)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task1_Hello_World_Server/package.json)

[Task 1 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3/Task1_Hello_World_Server)

### Screenshot

No screenshot for Task 1 is present in the supplied project archive.

### Result

The Express server is configured to respond to a GET request at `/` with `Backend Server Running`.

## Task 2: Multiple Routes

### Task Given

The task required extending the Express server with multiple routes including a root route, a students route, and an individual student route.

### Implementation

The project implements three GET routes:

1. `/` returns `Welcome to the Student Management API`
2. `/students` returns `List of all students`
3. `/students/1` returns `Student: Aarav, Roll No: 1`

The server runs on port `3000`.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task2_Multiple_Routes/server.js)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task2_Multiple_Routes/package.json)

[Task 2 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3/Task2_Multiple_Routes)

### Screenshot

No screenshot for Task 2 is present in the supplied project archive.

### Result

Multiple GET endpoints are implemented successfully, allowing different responses to be returned according to the requested URL.

## Task 3: Returning JSON Data

### Task Given

The task required an Express server that returns student information as JSON, including retrieval of all students and retrieval of an individual student using an ID.

### Implementation

The project contains an in memory array containing three students:

1. Aarav, CSE
2. Diya, ECE
3. Rohan, IT

The `/students` route returns the complete array using `res.json()`.

The `/students/:id` route searches the array using the requested numeric ID. If the student exists, the corresponding student object is returned as JSON. If the student does not exist, the server returns a JSON error message with HTTP status code `404`.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task3_Returning_JSON_Data/server.js)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task3_Returning_JSON_Data/package.json)

[Task 3 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3/Task3_Returning_JSON_Data)

### Screenshot

No screenshot specifically belonging to Task 3 is present in the supplied project archive.

### Result

The implementation provides JSON responses for the complete student collection and individual student records. An unsuccessful student lookup produces a `404` JSON response containing `Student not found`.

## Task 4: Sending HTML Responses

### Task Given

The task required an Express server capable of returning HTML responses instead of only plain text or JSON.

### Implementation

The project implements three GET routes.

The root route returns an HTML heading and paragraph.

The `/students` route creates an array containing three students and constructs an HTML unordered list using JavaScript.

The `/students/:id` route searches the student array and returns an HTML response containing the student's name and branch. If the ID is not found, the implementation returns an HTML `Student not found` response with status code `404`.

The actual student data in the project is:

1. Sehaj, CSE
2. Ajay, ECE
3. Kabir, IT

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task4_Sending_HTML_Responses/server.js)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task4_Sending_HTML_Responses/package.json)

[Task 4 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3/Task4_Sending_HTML_Responses)

### Screenshot

No screenshot specifically belonging to Task 4 is present in the supplied project archive.

### Result

The Express application generates HTML responses directly from the server. Both collection and individual student routes are implemented, including a `404` response for an unavailable student.

## Task 5: EJS Templating

### Task Given

The task introduced EJS as a template engine for Express. The task required configuring EJS, creating views, and rendering templates from Express routes.

### Implementation

The project configures Express to use EJS as its view engine.

The implementation contains two EJS templates:

1. `home.ejs`
2. `students.ejs`

The root route renders the `home` template.

The `/students` route renders the `students` template and passes the student array to the template.

The student template uses EJS iteration and output expressions to display each student's name and branch. The home template provides a link to the student list.

The actual student data in the project is:

1. Sehaj, CSE
2. Ajay, ECE
3. Kabir, IT

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task5_EJS_Templating/server.js)

[home.ejs](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task5_EJS_Templating/views/home.ejs)

[students.ejs](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task5_EJS_Templating/views/students.ejs)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task5_EJS_Templating/package.json)

[Task 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3/Task5_EJS_Templating)

### Screenshot

No screenshot specifically belonging to Task 5 is present in the supplied project archive.

### Result

The Express application is configured for EJS rendering and defines separate templates for the home page and student list. Student data is passed from the Express route to the EJS template for server side rendering.

## Task 6: Flask Hello World Server

### Task Given

The task required creation of a basic Flask backend server with a root route returning a simple response.

### Implementation

The project contains a Python Flask application.

The application imports Flask, creates the Flask application object, and defines a root route using `@app.route("/")`.

The root route returns `Backend Server Running`.

The application starts using Flask's development server with debug mode enabled.

### Code Location

[app.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task6_Flask_Hello_World/app.py)

[Task 6 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3/Task6_Flask_Hello_World)

### Screenshot

No screenshot for Task 6 is present in the supplied project archive.

### Result

The Flask application contains a functional root endpoint that returns the backend server status message.

## Task 7: Flask Routes and JSON

### Task Given

The task required extending the Flask server with multiple routes and JSON responses, including retrieval of all students and retrieval of an individual student.

### Implementation

The actual Flask implementation contains an in memory student list with three records:

1. Sehaj, CSE
2. Ajay, ECE
3. Kabir, IT

The root route returns `Student Management API`.

The `/students` route uses `jsonify()` to return the complete student list.

The `/students/<int:student_id>` route searches the student list using the supplied integer ID. If a matching record is found, it is returned as JSON. Otherwise, the implementation returns a JSON error response with HTTP status code `404`.

### Code Location

[app.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task7_Flask_Routes_JSON/app.py)

[Task 7 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3/Task7_Flask_Routes_JSON)

### Screenshot

No screenshot specifically belonging to Task 7 is present in the supplied project archive.

### Result

The Flask application implements multiple routes and JSON responses, including individual student retrieval and `404` handling for an unavailable student.

## Task 8: Browser DevTools

### Task Given

The task required observing the HTTP request response cycle using browser Developer Tools by opening the Network tab and inspecting an API request.

### Implementation

The actual project for Task 8 contains an Express server with a `/students` endpoint.

The endpoint returns three student records as JSON:

1. Aarav, CSE
2. Diya, ECE
3. Rohan, IT

The supplied screenshots show the `/students` request being inspected in Chrome DevTools.

The first screenshot shows the request URL, GET request method, HTTP `200 OK` status, request headers, response headers, and the local Express server.

The second screenshot shows the selected `/students` request in the Network panel and its JSON response containing the three student records.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task8_Browser_DevTools/server.js)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lecture3/Task8_Browser_DevTools/package.json)

[Task 8 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3/Task8_Browser_DevTools)

### Screenshots

![Chrome DevTools Network panel showing the GET request, 200 OK status, request URL, and response headers](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lecture3/Task8_Browser_DevTools/screenshots/request-response%20%281%29.png)

![Chrome DevTools Response panel showing the JSON response from the students endpoint](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lecture3/Task8_Browser_DevTools/screenshots/request-response%20%282%29.png)

### Result

The request response cycle was observed successfully through Chrome DevTools. The `/students` endpoint generated a GET request with an HTTP `200 OK` response, and the Response panel displayed the JSON student data.

## Project Structure

```text
Lecture3/
│
├── Task1_Hello_World_Server/
│   ├── package.json
│   ├── package-lock.json
│   └── server.js
│
├── Task2_Multiple_Routes/
│   ├── package.json
│   ├── package-lock.json
│   └── server.js
│
├── Task3_Returning_JSON_Data/
│   ├── package.json
│   ├── package-lock.json
│   └── server.js
│
├── Task4_Sending_HTML_Responses/
│   ├── package.json
│   ├── package-lock.json
│   └── server.js
│
├── Task5_EJS_Templating/
│   ├── package.json
│   ├── package-lock.json
│   ├── server.js
│   └── views/
│       ├── home.ejs
│       └── students.ejs
│
├── Task6_Flask_Hello_World/
│   └── app.py
│
├── Task7_Flask_Routes_JSON/
│   └── app.py
│
└── Task8_Browser_DevTools/
    ├── package.json
    ├── package-lock.json
    ├── server.js
    └── screenshots/
        ├── request-response (1).png
        └── request-response (2).png
```

## Concepts Used

1. HTTP request and response cycle
2. Client server communication
3. HTTP GET method
4. HTTP status codes
5. Express.js
6. Express routing
7. Route parameters
8. JSON responses
9. HTML responses
10. In memory data handling
11. HTTP `404` error handling
12. Flask
13. Flask routing
14. Flask `jsonify()`
15. EJS template engine
16. Server side rendering
17. Dynamic template data
18. Browser Developer Tools
19. Network request inspection
20. Request headers and response headers
21. Localhost based backend testing
22. Backend server ports

## Overall Result

The experiment successfully implements the eight practical tasks present in the supplied Lecture 3 project.

The project contains independent Express.js implementations for basic server creation, multiple routes, JSON responses, HTML responses, and EJS templating. It also contains Flask implementations for a basic server and JSON based routes. The final task demonstrates inspection of an Express JSON request through Chrome DevTools, supported by the two screenshots present in the project.

The additional lab exercise modifications involving the `/students/branch/:branch` route and `POST /students` route are not present in the supplied project and therefore are not claimed as implemented.

## Observations

1. Express.js is used to create lightweight HTTP servers and define GET routes.
2. Separate task folders are used for the Express implementations.
3. Each Express task maintains its own package configuration.
4. The JSON implementation uses an in memory JavaScript array rather than an external database.
5. The Express JSON implementation uses a parameterized route for individual student retrieval.
6. Both Express and Flask implementations include handling for a student that cannot be found.
7. Task 4 constructs HTML responses directly inside the Express server.
8. Task 5 separates HTML presentation from server logic using EJS templates.
9. The EJS implementation contains separate `home.ejs` and `students.ejs` files.
10. The Flask implementations use Python files named `app.py`.
11. Task 8 uses an Express endpoint returning JSON data for observing the request response cycle.
12. The supplied Task 8 screenshots show a GET request to `/students` returning HTTP `200 OK`.
13. The Task 8 response contains three student records represented as JSON.
14. The project does not contain the additional `POST /students` route specified in the lab exercise.
15. The project does not contain the additional `/students/branch/:branch` route specified in the lab exercise.
16. No GitHub Pages publication or experiment specific `index.html` was found in the supplied project archive.

## Conclusion

The experiment established the practical foundation of backend development by implementing HTTP based servers using Express.js and Flask. The completed tasks demonstrate routing, plain text responses, JSON responses, HTML responses, EJS based server side rendering, parameterized routes, error handling, and browser based inspection of HTTP communication.

The practical implementation demonstrates the request response concepts introduced in the experiment material and provides a structured foundation for subsequent backend development experiments involving HTTP requests and API testing.

## Lecture Link

No GitHub Pages publication for this experiment is present in the supplied project structure. Therefore, no GitHub Pages experiment link is included.

## Complete Lecture Source Code

[Complete Lecture 3 Experiment Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lecture3)
