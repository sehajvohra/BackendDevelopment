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

The objective of this experiment is to develop a basic user management
application using Node.js, Express, Mongoose, and MongoDB. The
application demonstrates MongoDB connectivity, Mongoose schema and model
creation, user registration, user login, retrieval of registered users,
and basic error handling.

## Software Requirements

-   Node.js
-   Express.js
-   Mongoose
-   MongoDB Community Server
-   Visual Studio Code
-   Web browser
-   Git and GitHub

## Problem Statement

Develop a basic user management system using Express, Mongoose, and
MongoDB. The application should allow users to register with a username,
email, and password, log in using their credentials, and view all
registered users. The application should store and retrieve user
information through MongoDB using Mongoose.

## Task Summary

  -----------------------------------------------------------------------
  Task                    Description             Implementation
  ----------------------- ----------------------- -----------------------
  Task 1                  Project Setup           Created the
                                                  `mongoose-demo` Node.js
                                                  project and installed
                                                  Express and Mongoose

  Task 2                  Express and MongoDB     Configured Express
                          Configuration           middleware and
                                                  connected the
                                                  application to the
                                                  local MongoDB database

  Task 3                  User Schema and Model   Created the Mongoose
                                                  user schema and User
                                                  model

  Task 4                  User Management Home    Created the User
                          Interface               Management System
                                                  interface with
                                                  registration, login,
                                                  and user viewing forms

  Task 5                  User Registration       Implemented the
                                                  `/signup` POST route
                                                  for registering users

  Task 6                  User Login              Implemented the
                                                  `/login` POST route for
                                                  authenticating users

  Task 7                  View All Registered     Implemented the
                          Users                   `/users` GET route for
                                                  retrieving users

  Task 8                  Run and Verify the      Started the Express
                          Application             server and verified the
                                                  MongoDB connection

  Task 9                  Test User Registration  Tested registration
                                                  using a sample user

  Task 10                 Test User Login         Tested login using the
                                                  registered user's
                                                  credentials

  Task 11                 Test View All Users     Retrieved and displayed
                                                  the registered user
  -----------------------------------------------------------------------

## Task 1: Project Setup

### Task Given

Create a Node.js project for the Mongoose demonstration and install the
required Express and Mongoose dependencies.

### Implementation

The project was created inside the `mongoose-demo` directory under
Experiment 13 A.

The Node.js project contains the required package files and uses Express
and Mongoose as dependencies.

### Code Location

[Experiment 13 A
Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/package.json)

[package-lock.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/package-lock.json)

### Screenshot

No separate screenshot was required for the project setup.

### Result

The Node.js project was successfully initialized and the required
dependencies were installed.

## Task 2: Express and MongoDB Configuration

### Task Given

Configure Express and establish a connection between the application and
MongoDB.

### Implementation

The application creates an Express instance and enables JSON and URL
encoded form data parsing.

The application connects to the local MongoDB database using:

`mongodb://localhost:27017/userdb`

The Express server is configured to run on port `3000`.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

The successful MongoDB connection and Express server startup are
demonstrated in Task 8.

### Result

The application successfully connected to MongoDB and started the
Express server on port `3000`.

## Task 3: User Schema and Model

### Task Given

Define the structure of user documents and create a Mongoose model for
database operations.

### Implementation

The project defines a Mongoose schema containing the following fields:

-   `username`
-   `email`
-   `password`
-   `createdAt`

The `username` and `email` fields are required and unique.

The `createdAt` field automatically stores the current date and time.

A `User` Mongoose model is created from the schema.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

No separate screenshot was required for the schema and model definition.

### Result

The Mongoose schema and User model were successfully created for
database operations.

## Task 4: User Management Home Interface

### Task Given

Create a web interface that allows users to register, log in, and view
registered users.

### Implementation

The `GET /` route generates the User Management System interface.

The interface contains:

-   Register New User section
-   Login section
-   View All Users section

The page also contains CSS styling for the forms, input fields, buttons,
and status messages.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![User Management System interface running
successfully](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/screenshots/task8-server-running.png)

### Result

The User Management System was successfully displayed in the browser at
`http://localhost:3000`.

## Task 5: User Registration

### Task Given

Implement a POST route that receives username, email, and password
information, creates a user document, saves it to MongoDB, and handles
duplicate user information.

### Implementation

The project implements the following route:

`POST /signup`

The route:

1.  Reads the username, email, and password from the submitted form.
2.  Creates a new `User` document.
3.  Saves the document to MongoDB using `.save()`.
4.  Displays a successful registration message.
5.  Handles duplicate username or email errors using error code `11000`.
6.  Displays other database errors when they occur.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Successful user
registration](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/screenshots/task9-user-registration.png)

### Result

A test user was successfully registered and the application displayed
the registration confirmation.

## Task 6: User Login

### Task Given

Implement a login route that searches for the user using the username,
verifies the password, and displays the appropriate response.

### Implementation

The project implements:

`POST /login`

The route:

1.  Reads the username and password from the request.
2.  Searches for the user using `User.findOne()`.
3.  Displays `User not found` if the username does not exist.
4.  Compares the submitted password with the stored password.
5.  Displays `Incorrect password` when the password does not match.
6.  Displays a successful login response when the credentials are
    correct.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Successful user
login](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/screenshots/task10-login-success.png)

### Result

The registered test user successfully logged in using the stored
credentials.

## Task 7: View All Registered Users

### Task Given

Implement a route that retrieves all registered users from MongoDB and
displays their information.

### Implementation

The project implements:

`GET /users`

The route uses `User.find()` to retrieve all registered users.

The displayed information includes:

-   Username
-   Email
-   Account creation date

The route also handles the case where no users are registered and
includes basic error handling.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Registered users retrieved from
MongoDB](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/screenshots/task11-view-all-users.png)

### Result

The registered test user was successfully retrieved from MongoDB and
displayed on the webpage.

## Task 8: Run and Verify the Application

### Task Given

Start MongoDB, run the Express application, open the application in a
browser, and verify that the application is working.

### Implementation

MongoDB Community Server was installed and configured locally.

The Express application was started using:

`node server.js`

The terminal displayed:

`Server running on http://localhost:3000`

and:

`Connected to MongoDB successfully`

The application was then opened in the browser.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Express server and MongoDB connection running
successfully](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/screenshots/task8-server-running.png)

### Result

The Express application successfully connected to MongoDB and was
accessible through the browser.

## Task 9: Test User Registration

### Task Given

Test the registration functionality by submitting username, email, and
password information through the registration form.

### Implementation

A test user was entered into the Register New User form.

The form submitted the information to the `/signup` route, which created
and saved the user document in MongoDB.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![User registration completed
successfully](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/screenshots/task9-user-registration.png)

### Result

The registration operation was completed successfully and the
application displayed the registration confirmation.

## Task 10: Test User Login

### Task Given

Test the login functionality using the credentials of the registered
user.

### Implementation

The registered user's credentials were entered into the Login form.

The `/login` route retrieved the user from MongoDB and verified the
submitted password.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![User login completed
successfully](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/screenshots/task10-login-success.png)

### Result

The login operation was successful and the application displayed the
welcome message and stored user information.

## Task 11: Test View All Users

### Task Given

Test the functionality for retrieving and displaying all registered
users from MongoDB.

### Implementation

The Show All Registered Users button was used to access the `/users`
route.

The route retrieved the stored users using Mongoose and generated an
HTML response containing the user information.

### Code Location

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

### Screenshot

![Registered users displayed
successfully](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2013A/screenshots/task11-view-all-users.png)

### Result

The registered user was successfully retrieved from MongoDB and
displayed on the webpage.

## Project Structure

```{=html}
<pre>
Lab/
└── Exp 13A/
    ├── mongoose-demo/
    │   ├── package-lock.json
    │   ├── package.json
    │   └── server.js
    │
    ├── screenshots/
    │   ├── task8-server-running.png
    │   ├── task9-user-registration.png
    │   ├── task10-login-success.png
    │   └── task11-view-all-users.png
    │
    └── Report.md
</pre>
```
## Concepts Used

-   Node.js
-   Express.js
-   Express middleware
-   HTTP GET routes
-   HTTP POST routes
-   MongoDB
-   Mongoose
-   Mongoose schemas
-   Mongoose models
-   MongoDB document creation
-   `.save()`
-   `.findOne()`
-   `.find()`
-   Unique fields
-   Asynchronous programming
-   `async` and `await`
-   Promise based MongoDB connection
-   Form data handling
-   JSON request handling
-   Basic error handling
-   Duplicate key error handling

## Overall Result

The Express and Mongoose based User Management System was successfully
implemented and tested.

The application successfully:

-   Connected Express with MongoDB through Mongoose
-   Created a Mongoose User schema and model
-   Registered users
-   Stored users in MongoDB
-   Authenticated users through the login route
-   Retrieved all registered users
-   Displayed the results through a web interface

## Observations

1.  Mongoose provides a schema based structure for MongoDB documents.
2.  The User model provides the interface used by the application for
    database operations.
3.  The `/signup` route creates and saves new user documents using
    `.save()`.
4.  The `/login` route retrieves a user using `.findOne()`.
5.  The `/users` route retrieves all users using `.find()`.
6.  Username and email fields are configured as unique fields.
7.  Duplicate username or email registration produces a duplicate key
    error.
8.  Database operations are asynchronous and are handled using `async`
    and `await`.
9.  The application uses the local MongoDB database `userdb`.
10. The current implementation stores passwords as plain text for
    learning purposes.

## Conclusion

The experiment successfully demonstrated the integration of Express.js,
Mongoose, and MongoDB in a Node.js application. A functional user
management system was created with registration, login, and user
retrieval operations.

The experiment provided practical understanding of Mongoose schemas,
models, MongoDB operations, Express routes, asynchronous programming,
form handling, and basic error handling.

## Experiment Link

The experiment is not published as a GitHub Pages application because it
requires a running Node.js server and MongoDB database.

## GitHub Source Code

[Complete Experiment 13 A
Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A)

[Complete mongoose-demo
Project](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A/mongoose-demo)

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/server.js)

[package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/package.json)

[package-lock.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2013A/mongoose-demo/package-lock.json)

[Screenshots
Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2013A/screenshots)
