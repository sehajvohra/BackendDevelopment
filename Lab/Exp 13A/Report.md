# Experiment 13 A

## Title

Express + Mongoose User Management Tutorial

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

The objective of this experiment is to develop a basic user management application using Node.js, Express, Mongoose, and MongoDB. The application demonstrates MongoDB connectivity, Mongoose schema and model creation, user registration, user login, retrieval of registered users, and basic error handling.

## Software Requirements

* Node.js
* Express.js
* Mongoose
* MongoDB Community Server
* Visual Studio Code
* Web browser
* Git and GitHub

## Problem Statement

Develop a basic user management system using Express, Mongoose, and MongoDB. The application should allow users to register with a username, email, and password, log in using their credentials, and view all registered users. The application should store and retrieve user information through MongoDB using Mongoose.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Create and initialize the Node.js project | Created the `mongoose-demo` project and installed Express and Mongoose |
| Task 2 | Configure Express and MongoDB | Added Express middleware and connected the application to the local MongoDB database |
| Task 3 | Define the user schema and model | Created a Mongoose `userSchema` and `User` model |
| Task 4 | Create the home interface | Implemented the User Management System page with registration, login, and user viewing forms |
| Task 5 | Implement user registration | Added the `/signup` POST route to create and save users |
| Task 6 | Implement user login | Added the `/login` POST route to verify user credentials |
| Task 7 | Implement user retrieval | Added the `/users` GET route to retrieve and display registered users |
| Task 8 | Run and verify the application | Started MongoDB and the Express server and verified the database connection |
| Task 9 | Test user registration | Registered a test user and verified the successful registration response |
| Task 10 | Test user login | Logged in using the registered credentials and verified the successful login response |
| Task 11 | Test user retrieval | Retrieved and displayed the registered user using the `/users` route |

## Task 1: Project Setup

### Task Given

Create a Node.js project for the Mongoose demonstration and install the required Express and Mongoose dependencies.

### Implementation

The project was created inside:

`Lab/Exp 13A/mongoose-demo/`

The Node.js project contains `package.json` and `package-lock.json`, with Express and Mongoose installed as dependencies.

### Code Location

[Experiment 13A Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/package.json)

[package-lock.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/package-lock.json)

### Screenshot

No separate screenshot was required for the project setup.

### Result

The Node.js project was successfully initialized and the required Express and Mongoose packages were installed.

## Task 2: Express and MongoDB Configuration

### Task Given

Configure Express, enable JSON and form data parsing, and establish a connection between the application and MongoDB.

### Implementation

The application creates an Express instance and enables JSON request parsing and URL encoded form data parsing.

The application connects to the local MongoDB database using:

`mongodb://localhost:27017/userdb`

The server is configured to use port `3000`.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

The successful server startup and MongoDB connection are demonstrated in Task 8.

### Result

The application successfully connected to MongoDB and started the Express server on port `3000`.

## Task 3: User Schema and Model

### Task Given

Define the structure of the user documents and create a Mongoose model for database operations.

### Implementation

The project defines a Mongoose schema containing:

* `username`
* `email`
* `password`
* `createdAt`

The username and email fields are required and unique. The `createdAt` field automatically receives the current date and time.

A `User` Mongoose model is created from the schema.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

No separate screenshot was required for the schema and model definition.

### Result

A Mongoose schema and `User` model were successfully created for interacting with the MongoDB users collection.

## Task 4: User Management Home Interface

### Task Given

Create a web interface through which users can register, log in, and view registered users.

### Implementation

The `GET /` route returns an HTML page titled **User Management System**.

The page contains:

* Register New User form
* Login form
* View All Users form

The interface also includes CSS styling for the containers, input fields, buttons, and success and error messages.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![User Management System running with registration, login, and user viewing interfaces](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/mongoose-demo/screenshots/task8-server-running.png)

### Result

The User Management System interface was successfully displayed in the browser at `http://localhost:3000`.

## Task 5: User Registration

### Task Given

Implement a POST route that receives username, email, and password information, creates a new user document, saves it to MongoDB, and handles duplicate username or email errors.

### Implementation

The project implements:

`POST /signup`

The route:

1. Reads username, email, and password from the request body.
2. Creates a new `User` document.
3. Saves the document using Mongoose.
4. Displays a successful registration response.
5. Handles duplicate key errors using error code `11000`.
6. Displays other database errors when they occur.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Successful user registration](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/mongoose-demo/screenshots/task9-user-registration.png)

### Result

A test user was successfully registered and the application displayed the user registration confirmation.

## Task 6: User Login

### Task Given

Implement a login route that searches for the user using the username, verifies the password, and displays an appropriate response.

### Implementation

The project implements:

`POST /login`

The route:

1. Reads the username and password from the request.
2. Searches MongoDB using `User.findOne()`.
3. Displays `User not found` when the username does not exist.
4. Checks the submitted password against the stored password.
5. Displays `Incorrect password` when the password does not match.
6. Displays a successful login message with the user's email and account creation date when the credentials match.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Successful user login](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/mongoose-demo/screenshots/task10-login-success.png)

### Result

The registered test user successfully logged in using the stored credentials.

## Task 7: View All Registered Users

### Task Given

Implement a route that retrieves all registered users from MongoDB and displays their stored information.

### Implementation

The project implements:

`GET /users`

The route uses `User.find()` to retrieve all users. It displays the username, email, and account creation date for each registered user.

If no users exist, the application displays an appropriate message. Basic error handling is also included.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Registered users displayed from MongoDB](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/mongoose-demo/screenshots/task11-view-all-users.png)

### Result

The registered test user was successfully retrieved from MongoDB and displayed through the application.

## Task 8: Run and Verify the Application

### Task Given

Start MongoDB, run the Express application, open the application in a browser, and verify the main functionality.

### Implementation

MongoDB Community Server was configured locally and the Express application was started using:

`node server.js`

The application successfully reported:

* Server running on `http://localhost:3000`
* Connected to MongoDB successfully

The browser successfully displayed the User Management System.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Express server and MongoDB connection successfully running](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/mongoose-demo/screenshots/task8-server-running.png)

### Result

The Express application successfully connected to MongoDB and became accessible through the local browser.

## Task 9: Test User Registration

### Task Given

Test the registration functionality by submitting username, email, and password information through the registration form.

### Implementation

A test user was submitted through the **Register New User** form. The application processed the form using the `/signup` route and stored the user in MongoDB.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![User registration result](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/mongoose-demo/screenshots/task9-user-registration.png)

### Result

The registration operation completed successfully and the application displayed the registration confirmation.

## Task 10: Test User Login

### Task Given

Test the login functionality using the credentials of the registered user.

### Implementation

The credentials of the registered test user were entered into the Login form. The `/login` route retrieved the corresponding user and verified the submitted password.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![User login result](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/mongoose-demo/screenshots/task10-login-success.png)

### Result

The login operation was successful and the application displayed the welcome message and stored user information.

## Task 11: Test View All Users

### Task Given

Test the functionality for retrieving and displaying all registered users from MongoDB.

### Implementation

The **Show All Registered Users** button was used to access the `/users` route. The route retrieved the stored users through Mongoose and generated an HTML response containing the user information.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![View all registered users result](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/mongoose-demo/screenshots/task11-view-all-users.png)

### Result

The registered user was successfully retrieved from MongoDB and displayed on the webpage.

## Project Structure

```text
Lab/
└── Exp 13A/
    └── mongoose-demo/
        ├── node_modules/
        ├── package-lock.json
        ├── package.json
        ├── server.js
        └── screenshots/
            ├── task8-server-running.png
            ├── task9-user-registration.png
            ├── task10-login-success.png
            └── task11-view-all-users.png