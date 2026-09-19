# Experiment 12B

## Title

Using Node.js to Manage Sessions & Cookies

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

The objective of this experiment is to demonstrate session management using Node.js and Express. The experiment implements user registration and login using sessions, protects authenticated routes, destroys sessions during logout, and maintains a separate To Do list for each browser session.

The experiment also uses `cookie-parser` and session cookies as part of the Node.js session management setup.

## Software Requirements

* Node.js
* Express
* express-session
* cookie-parser
* Visual Studio Code
* Web browser
* Git and GitHub

## Problem Statement

HTTP is stateless, so a server does not automatically remember information about a user between different requests. Sessions and cookies can be used to maintain state and support user management.

The experiment contains two tasks:

1. A Simple User Login System using sessions.
2. A Session Based To Do List where To Do items are maintained separately for each session.

## Task Summary

| Task | Description | Implementation |
| --- | --- | --- |
| Task 1 | Simple User Login System | Implemented user registration, login authentication, session based user management, protected dashboard access, and logout functionality. |
| Task 2 | Session Based To Do List | Implemented adding, displaying, deleting, and clearing To Do items using session storage, with separate lists for separate browser sessions. |

# Task 1: Simple User Login System

## Task Given

The task requires a small web application in which a user can register with a username and password, log in using the registered credentials, access a protected dashboard after successful authentication, and log out to end the session.

The user details are stored temporarily in an in memory array, without using a database.

## Implementation

The Task 1 application is implemented using Node.js, Express, `express-session`, and `cookie-parser`.

The implementation contains the following functionality:

* A home page with Register and Login options.
* A registration page that accepts a username and password.
* Duplicate username checking during registration.
* In memory storage of registered users.
* A login page for authentication.
* Session storage of the authenticated username.
* A protected dashboard.
* Authentication middleware that checks whether a session user exists.
* Logout functionality that destroys the active session.
* Redirection to the login page when an unauthenticated user attempts to access the dashboard.

The authenticated user is stored in the session using the `req.session.user` object.

The application runs on port `3000`.

## Code Location

[Task 1 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012B/Task1)

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012B/Task1/server.js)

## Screenshots

### Login Page

![Login Page](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task1/screenshots/SS01_Login_Page.png)

### Registration Page

![Registration Page](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task1/screenshots/SS02_Registration_Page.png)

### Registration Success

![Registration Success](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task1/screenshots/SS03_Registration_Success.png)

### Dashboard After Login

![Dashboard After Login](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task1/screenshots/SS04_Dashboard_After_Login.png)

### Protected Dashboard Access

![Protected Dashboard Access](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task1/screenshots/SS05_Protected_Dashboard_Access.png)

## Result

The Simple User Login System was successfully implemented and tested.

The application successfully allowed a user to register, log in using the registered credentials, access the protected dashboard through session authentication, log out, and lose access to the protected dashboard after the session was destroyed.

# Task 2: Session Based To Do List

## Task Given

The task requires a basic To Do List web application in which users can add, view, and delete To Do items.

The To Do list must be stored per session so that different browser sessions maintain separate lists.

## Implementation

The Task 2 application is implemented separately from Task 1 using its own Node.js server and dependencies.

The implementation contains the following functionality:

* A session based To Do List interface.
* Creation of an empty To Do list when a session does not already contain one.
* Adding new To Do items.
* Displaying all To Do items belonging to the current session.
* Deleting individual To Do items.
* Clearing all To Do items from the current session.
* Maintaining separate To Do lists for separate browser sessions.

The To Do items are stored in `req.session.todos`.

The application runs independently on port `3001`.

The implementation also uses `cookie-parser` and `express-session` for session and cookie related functionality.

No custom theme cookie was implemented in the final Task 2 application.

## Code Location

[Task 2 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2012B/Task2)

[server.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2012B/Task2/server.js)

## Screenshots

### Empty To Do List

![Empty To Do List](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task2/screenshots/SS01_Empty_Todo_List.png)

### To Do Item Added

![To Do Item Added](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task2/screenshots/SS02_Todo_Item_Added.png)

### To Do Item Deleted

![To Do Item Deleted](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task2/screenshots/SS03_Todo_Item_Deleted.png)

### Session Based To Do List

![Session Based To Do List](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task2/screenshots/SS04_Session_Todo_List.png)

### Separate Session

![Separate Session](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2012B/Task2/screenshots/SS05_Separate_Session.png)

## Result

The Session Based To Do List was successfully implemented and tested.

The application successfully allowed To Do items to be added, displayed, deleted, and cleared. The session based implementation also demonstrated that separate browser sessions maintain separate To Do lists.

## Project Structure

<pre>
Exp 12B/
│
├── Task1/
│   ├── screenshots/
│   │   ├── SS01_Login_Page.png
│   │   ├── SS02_Registration_Page.png
│   │   ├── SS03_Registration_Success.png
│   │   ├── SS04_Dashboard_After_Login.png
│   │   └── SS05_Protected_Dashboard_Access.png
│   ├── package-lock.json
│   ├── package.json
│   └── server.js
│
└── Task2/
    ├── screenshots/
    │   ├── SS01_Empty_Todo_List.png
    │   ├── SS02_Todo_Item_Added.png
    │   ├── SS03_Todo_Item_Deleted.png
    │   ├── SS04_Session_Todo_List.png
    │   └── SS05_Separate_Session.png
    ├── package-lock.json
    ├── package.json
    └── server.js
</pre>