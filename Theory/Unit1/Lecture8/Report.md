# Experiment 8

## Title

Server-Side Rendering and Templating Engines

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

To understand server-side rendering concepts and implement dynamic web pages using templating engines with Express.js, EJS, FastAPI, Jinja2, and static asset handling.

## Software Requirements

- Node.js
- npm
- Express.js
- EJS
- Python
- FastAPI
- Uvicorn
- Jinja2
- Browser
- Visual Studio Code or any code editor

## Problem Statement

The experiment requires implementing server-side rendered pages using templating engines. The project demonstrates how backend applications combine templates with data to generate complete HTML responses. It also shows how static files such as CSS and images are served in Express.js and FastAPI applications.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Display students in an HTML table with alternating row colors | Implemented an Express.js application using EJS, a student array, and CSS classes for alternating rows. |
| Task 2 | Add an EJS about page with backend variables | Implemented an Express.js `/about` route that renders course and lecturer details in an EJS template. |
| Task 3 | Display current date and time using Jinja2 | Implemented a FastAPI application that renders the current date and time using a Jinja2 template. |
| Task 4 | Serve custom CSS with Express | Implemented an Express.js student table page with a custom CSS file served from the `public` folder. |
| Task 5 | Serve and display a static image with FastAPI | Implemented FastAPI static file mounting and displayed `logo.png` in a Jinja2 template. |

## Task 1: Express EJS Student Table

### Task Given

The task required converting the Express student list example into an HTML table and applying alternating row colors using CSS classes.

### Implementation

An Express.js server was implemented with EJS as the view engine. The server stores an in-memory list of students with `id`, `name`, and `branch` fields. The `/` route renders `students.ejs` and passes the student list to the template. The EJS template uses a loop to generate table rows and applies `even` and `odd` CSS classes based on the row index.

### Code Location

- [Task 1 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8/Task1)
- [server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task1/server.js)
- [students.ejs](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task1/views/students.ejs)
- [style.css](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task1/public/css/style.css)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task1/package.json)

### Screenshot

![Student table with alternating row colors](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture8/Task1/screenshots/task1-student-table.png)

### Result

The Express.js application successfully rendered a dynamic student table using EJS and displayed alternating row colors through CSS.

## Task 2: EJS About Page

### Task Given

The task required adding a new EJS route, `GET /about`, that renders an about page using course name and lecturer name variables passed from the backend.

### Implementation

An Express.js server was implemented with an `/about` route. The route renders `about.ejs` and passes `course` as `Backend Development` and `lecturer` as `Dr. Prateek Raj Gautam`. The EJS template displays these values inside the rendered HTML page.

### Code Location

- [Task 2 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8/Task2)
- [server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task2/server.js)
- [about.ejs](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task2/views/about.ejs)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task2/package.json)

### Screenshot

![About page rendered with EJS](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture8/Task2/screenshots/task2-about-page.png)

### Result

The `/about` route successfully rendered a server-side EJS page containing backend-provided course and lecturer information.

## Task 3: FastAPI Jinja2 Date and Time Page

### Task Given

The task required building a FastAPI page that displays the current date and time using the Jinja2 placeholder `{{ now }}`.

### Implementation

A FastAPI application was implemented using `Jinja2Templates`. The `/` route calculates the current date and time using Python's `datetime` module and formats it as `DD-MM-YYYY HH:MM:SS`. This value is passed to `home.html` and rendered using the Jinja2 `{{ now }}` expression. The application is configured to run with Uvicorn on `127.0.0.1:8000`.

### Code Location

- [Task 3 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8/Task3)
- [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task3/main.py)
- [home.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task3/templates/home.html)

### Screenshot

![Current date and time rendered with FastAPI and Jinja2](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture8/Task3/screenshots/task3-date-time.png)

### Result

The FastAPI application successfully generated a server-side HTML page showing the current date and time.

## Task 4: Express Static CSS Styling

### Task Given

The task required serving a custom CSS file with Express to change the background color and font of the student list page.

### Implementation

An Express.js application was implemented with EJS as the template engine and `express.static()` configured to serve assets from the `public` folder. The `/` route renders a student table using `students.ejs`. The template links to `/css/style.css`, which applies a light blue background, Arial font, table borders, padding, and styled table headers.

### Code Location

- [Task 4 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8/Task4)
- [server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task4/server.js)
- [students.ejs](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task4/views/students.ejs)
- [style.css](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task4/public/css/style.css)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task4/package.json)

### Screenshot

![Student table styled with custom Express CSS](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture8/Task4/screenshots/task4-custom-css.png)

### Result

The Express.js application successfully served the custom CSS file and applied styling to the server-rendered student list page.

## Task 5: FastAPI Static Image

### Task Given

The task required creating a FastAPI app that serves an image from the `static/images/` folder and displays it in a Jinja2 template.

### Implementation

A FastAPI application was implemented using `Jinja2Templates` and `StaticFiles`. The `static` directory is mounted at `/static`, allowing the browser to access files from the static folder. The `home.html` template displays `logo.png` using the path `/static/images/logo.png`.

### Code Location

- [Task 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8/Task5)
- [main.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task5/main.py)
- [home.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task5/templates/home.html)
- [logo.png](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture8/Task5/static/images/logo.png)

### Screenshot

![Static image served with FastAPI](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture8/Task5/screenshots/task5-static-image.png)

### Result

The FastAPI application successfully served a static image and displayed it inside a server-rendered Jinja2 template.

## Project Structure

```text
Theory/Unit1/Lecture8/
+-- Task1/
|   +-- server.js
|   +-- package.json
|   +-- package-lock.json
|   +-- public/css/style.css
|   +-- views/students.ejs
|   +-- screenshots/task1-student-table.png
+-- Task2/
|   +-- server.js
|   +-- package.json
|   +-- package-lock.json
|   +-- views/about.ejs
|   +-- screenshots/task2-about-page.png
+-- Task3/
|   +-- main.py
|   +-- templates/home.html
|   +-- screenshots/task3-date-time.png
+-- Task4/
|   +-- server.js
|   +-- package.json
|   +-- package-lock.json
|   +-- public/css/style.css
|   +-- views/students.ejs
|   +-- screenshots/task4-custom-css.png
+-- Task5/
|   +-- main.py
|   +-- templates/home.html
|   +-- static/images/logo.png
|   +-- screenshots/task5-static-image.png
+-- Report.md
```

## Concepts Used

- Server-side rendering
- Templating engines
- Express.js routing
- EJS template syntax
- Passing backend data to templates
- Loops and dynamic table rendering in EJS
- Static file serving with `express.static()`
- FastAPI HTML responses
- Jinja2 template rendering
- Dynamic data rendering with `{{ now }}`
- Static file mounting with FastAPI `StaticFiles`
- CSS and image asset delivery

## Overall Result

The experiment successfully implemented server-side rendered pages using both Express.js with EJS and FastAPI with Jinja2. It also demonstrated static file serving through CSS in Express and image delivery in FastAPI.

## Observations

- The actual implementation is stored under `Theory/Unit1/Lecture8`.
- No separate `Lab/Exp 8` folder exists in the verified project structure.
- Express tasks use `views/` for EJS templates and `public/` for static CSS.
- FastAPI tasks use `templates/` for Jinja2 HTML files and `static/` for image assets.
- Task 1 uses alternating row CSS classes based on the EJS loop index.
- Task 2 passes backend variables into an EJS template.
- Task 3 dynamically generates the current date and time on the server.
- Task 4 demonstrates custom CSS delivery through Express static middleware.
- Task 5 demonstrates explicit static file mounting in FastAPI.

## Conclusion

This experiment demonstrated how backend servers generate complete HTML pages using server-side rendering. Express.js with EJS was used to render dynamic student and about pages, while FastAPI with Jinja2 was used to render dynamic date/time content and serve a static image. The experiment also showed the importance of organizing templates and static assets separately in backend web applications.

## Experiment Link

GitHub Pages Link: Not published as a GitHub Pages experiment because the implementation requires local Express.js and FastAPI servers.

Complete Experiment Source Code: [Theory/Unit1/Lecture8](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture8)
