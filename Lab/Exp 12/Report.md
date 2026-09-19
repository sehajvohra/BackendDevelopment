# Experiment 12

## Title

Node.js, Express.js, and EJS Templating

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

To understand and implement server side JavaScript using Node.js, build RESTful APIs with Express.js, handle HTTP requests and responses, work with URL parameters and POST data, implement EJS templating, and use development tools like Nodemon.

## Software Requirements

1. Visual Studio Code
2. Node.js
3. NPM
4. Express.js
5. EJS
6. Nodemon
7. Postman
8. Google Chrome
9. Git and GitHub

## Problem Statement

The experiment focuses on developing a Node.js and Express.js application that demonstrates server creation, HTTP request and response handling, URL parameters, query parameters, POST data processing, EJS based dynamic web pages, and automatic server restarting using Nodemon.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Node.js Script | Created and executed a basic Node.js script |
| Task 2 | Basic Express Server | Created an Express server and configured the application |
| Task 3 | Express Responses | Implemented plain text, HTML, and JSON responses |
| Task 4 | URL Parameters | Implemented a route using a dynamic user ID |
| Task 5 | Query Parameters and Calculator API | Implemented search and calculator routes using query parameters |
| Task 6 | POST Data | Implemented registration and login POST routes |
| Task 7 | EJS Home Page | Rendered a dynamic home page using EJS |
| Task 8 | EJS Users Page | Rendered a list of users using EJS |
| Task 9 | EJS Profile Page | Rendered a dynamic user profile using EJS |
| Task 10 | Nodemon | Configured and tested automatic server restarting |
| Task 11 | Endpoint Listing | Displayed the available application endpoints in the terminal |

## Task 1: Node.js Script

### Task Given

Create and execute a basic Node.js program to demonstrate JavaScript execution outside the browser.

### Implementation

The `script.js` file was created using Node.js. The program prints a welcome message, displays the name and course, and calculates the sum of numbers using the `reduce()` method.

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/script.js)

### Screenshot

![Node.js Script](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task1-nodejs-script.png)

### Result

The Node.js script executed successfully and displayed the expected output in the terminal.

## Task 2: Basic Express Server

### Task Given

Create a basic Express.js server and handle a request using an Express route.

### Implementation

Express.js was installed and configured. The application listens on port 3000 and provides a welcome route at `/`.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

### Screenshot

![Basic Express Server](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task2-basic-express-server.png)

### Result

The Express server started successfully and returned the welcome message at the root route.

## Task 3: Express Response Methods

### Task Given

Demonstrate different types of HTTP responses using Express.js.

### Implementation

Three routes were implemented.

The `/text` route returns a plain text response.

The `/html` route returns an HTML response.

The `/json` route returns a JSON response containing a message, status, and data.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

### Screenshots

![Text Response](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task3-text-response.png)

![HTML Response](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task3-html-response.png)

![JSON Response](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task3-json-response.png)

### Result

The application successfully returned plain text, HTML, and JSON responses through separate Express routes.

## Task 4: URL Parameters

### Task Given

Demonstrate the use of URL parameters in Express.js.

### Implementation

The `/user/:id` route was created to receive a dynamic user ID through the URL. The value is accessed using `req.params.id` and returned as JSON.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

### Screenshot

![URL Parameters](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task4-url-parameters.png)

### Result

The application successfully received and displayed the user ID supplied through the URL.

## Task 5: Query Parameters and Calculator API

### Task Given

Demonstrate query parameters and perform calculations based on values supplied through a URL.

### Implementation

The `/search` route reads `q`, `page`, and `limit` from `req.query`.

The `/calculate` route reads `num1`, `num2`, and `operation` from the query string. The implemented operations are addition, subtraction, multiplication, and division. Division by zero is handled by returning an error result, while unsupported operations return an invalid operation message.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

### Screenshots

![Query Parameters](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task5-query-parameters.png)

![Calculator API](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task5-calculator-api.png)

### Result

The application successfully processed query parameters and returned calculated results in JSON format.

## Task 6: POST Data

### Task Given

Handle POST requests and process data submitted by the client.

### Implementation

The application uses `express.json()` and `express.urlencoded()` middleware to process request data.

The `/register` route accepts username, email, and password data and returns a registration success response containing the username and email.

The `/login` route checks the supplied email and password against the credentials defined in the application. A successful login returns a success message and a sample token. Invalid credentials return an HTTP 401 response.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

### Screenshots

![POST Registration](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task6-post-registration.png)

![POST Login](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task6-post-login.png)

### Result

The application successfully received POST data through Postman and returned the appropriate JSON responses.

## Task 7: EJS Home Page

### Task Given

Configure EJS as the view engine and render dynamic content.

### Implementation

EJS was configured as the Express view engine. The `/home` route renders `home.ejs` and passes a title, heading, and message to the template.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

[home.ejs](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/views/home.ejs)

### Screenshot

![EJS Home Page](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task7-ejs-home.png)

### Result

The EJS home page was rendered successfully with dynamic values supplied by the Express route.

## Task 8: EJS Users Page

### Task Given

Use EJS to display multiple user records dynamically.

### Implementation

The `/users` route creates an array containing user IDs, names, and email addresses and passes the array to `users.ejs`.

The implemented users are Sehaj Vohra, Himadri Barman, and Rahul Chauhan.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

[users.ejs](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/views/users.ejs)

### Screenshot

![EJS Users Page](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task8-ejs-users.png)

### Result

The users page was successfully generated using EJS and displayed the supplied user records.

## Task 9: EJS Profile Page

### Task Given

Render a dynamic profile page using a URL parameter and EJS.

### Implementation

The `/profile/:id` route receives a user ID through the URL and creates a user object containing the ID, name, email, age, and city. The object is passed to `profile.ejs` for rendering.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

[profile.ejs](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/views/profile.ejs)

### Screenshot

![EJS Profile Page](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task9-ejs-profile.png)

### Result

The profile page was successfully rendered using EJS and displayed the user information.

## Task 10: Nodemon

### Task Given

Use Nodemon as a development tool to automatically restart the Node.js application when source files change.

### Implementation

Nodemon was installed and configured through the `dev` script in `package.json`.

The development server was started using:

`npm run dev`

A `nodemon.json` file was also used to configure watched files, file extensions, ignored directories, and restart delay.

### Code Location

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/package.json)

[nodemon.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodemon.json)

### Screenshot

![Nodemon](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task10-nodemon.png)

### Result

Nodemon successfully started the Express application and monitored the project files for changes.

## Task 11: Available Endpoints

### Task Given

Display the available Express application endpoints in the terminal.

### Implementation

The `app.listen()` callback contains console statements listing the implemented routes and their purpose.

The endpoint list includes the welcome route, text response, HTML response, JSON response, user route, search route, calculator route, registration route, login route, EJS home page, users page, and profile page.

### Code Location

[app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012/nodejs-express-lab/app.js)

### Screenshot

![Complete Endpoints](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012/screenshots/task11-complete-endpoints.png)

### Result

The terminal successfully displayed the available endpoints when the server started.

## Project Structure

```text
Exp 12
│
├── nodejs-express-lab
│   ├── node_modules
│   ├── views
│   │   ├── home.ejs
│   │   ├── profile.ejs
│   │   └── users.ejs
│   ├── app.js
│   ├── package.json
│   ├── package-lock.json
│   └── script.js
│
├── screenshots
│   ├── task1-nodejs-script.png
│   ├── task2-basic-express-server.png
│   ├── task3-json-response.png
│   ├── task3-text-response.png
│   ├── task4-url-parameters.png
│   ├── task5-calculator-api.png
│   ├── task5-query-parameters.png
│   ├── task6-post-login.png
│   ├── task6-post-registration.png
│   ├── task7-ejs-home.png
│   ├── task8-ejs-users.png
│   ├── task9-ejs-profile.png
│   ├── task10-nodemon.png
│   └── task11-complete-endpoints.png
│
└── nodemon.json