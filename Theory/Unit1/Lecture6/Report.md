# Experiment 6

## Title

Managing server-side Session, Cookie, and State Management

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

To understand and implement backend state management in an Express.js application using server-side sessions, browser cookies, and URL query strings.

## Software Requirements

- Node.js
- npm
- Express.js
- express-session
- cookie-parser
- Browser
- Visual Studio Code or any code editor

## Problem Statement

HTTP is stateless, so a backend application requires state management techniques to remember user-related data across requests. This experiment demonstrates session handling, cookie creation and deletion, and query string processing using an Express.js server.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Set up the Express server with session and cookie middleware | Implemented an Express.js server using `express-session` and `cookie-parser`. |
| Task 2 | Start and access a user session | Implemented `/login` to create a session and `/profile` to read session data. |
| Task 3 | Destroy the user session | Implemented `/logout` to destroy the active session and verified profile access after logout. |
| Task 4 | Set and read browser cookies | Implemented `/setcookie` and `/getcookie` using `cookie-parser`. |
| Task 5 | Verify and delete cookies | Verified cookie data and implemented `/deletecookie` to clear the stored cookie. |
| Task 6 | Read query string parameters | Implemented `/welcome?user=...&role=...` using `req.query`. |

## Task 1: Express Server Setup

### Task Given

The task required setting up an Express.js backend application capable of managing server-side sessions and cookies.

### Implementation

An Express.js application was created in `app.js`. The server uses `express-session` with a secret key, disabled resave, enabled uninitialized sessions, and a session cookie lifetime of `60000` milliseconds. The application also uses `cookie-parser` middleware to read cookies from incoming requests. The server runs on port `3000`.

### Code Location

- [Lecture 6 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6)
- [app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture6/app.js)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture6/package.json)

### Screenshot

![Express server running for session task](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T2_Server_Running.png)

### Result

The Express.js server started successfully on port `3000` with session and cookie middleware configured.

## Task 2: Session Login and Profile Access

### Task Given

The task required creating a server-side session after login and accessing stored session data from another route.

### Implementation

The `/login` route stores the username `Sehaj` in `req.session.username` and sends a response confirming that the session has started. The `/profile` route checks whether `req.session.username` exists. If the session is active, it displays a welcome message; otherwise, it asks the user to log in first.

### Code Location

- [Lecture 6 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6)
- [app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture6/app.js)

### Screenshots

![Login session started](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T2_Login_Session.png)

![Profile route showing active session](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T2_Profile_Session.png)

### Result

The application successfully created a session during login and retrieved the stored username from the session on the profile route.

## Task 3: Session Logout

### Task Given

The task required destroying an active session and verifying that protected session data is no longer available afterward.

### Implementation

The `/logout` route calls `req.session.destroy()` to remove the active session. If the session is destroyed successfully, the route returns `Session destroyed successfully`. After logout, visiting `/profile` no longer finds `req.session.username`, so the application returns `Please log in first.`

### Code Location

- [Lecture 6 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6)
- [app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture6/app.js)

### Screenshots

![Session destroyed on logout](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T3_Logout_Session_Destroyed.png)

![Profile after logout](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T3_Profile_After_Logout.png)

### Result

The session was successfully destroyed, and the profile route correctly showed that no logged-in session was available after logout.

## Task 4: Set and Read Cookies

### Task Given

The task required setting a browser cookie from the server and reading it back in another route.

### Implementation

The `/setcookie` route creates a cookie named `username` with the value `Sehaj`. The cookie is configured with `maxAge: 3600000`, `httpOnly: true`, and `secure: false`. The `/getcookie` route reads `req.cookies.username` and displays a welcome message if the cookie exists.

### Code Location

- [Lecture 6 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6)
- [app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture6/app.js)

### Screenshots

![Express server running for cookie task](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T4_Server_Running.png)

![Cookie set from server](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T4_Set_Cookie.png)

![Cookie read from request](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T4_Get_Cookie.png)

### Result

The application successfully set a browser cookie and later read the cookie value from the incoming request.

## Task 5: Cookie Verification and Deletion

### Task Given

The task required verifying that the cookie exists and deleting it when requested.

### Implementation

The cookie value was verified through the cookie-reading route. The `/deletecookie` route uses `res.clearCookie("username")` to remove the `username` cookie from the browser. After deletion, the cookie is no longer available for future requests.

### Code Location

- [Lecture 6 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6)
- [app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture6/app.js)

### Screenshots

![Cookie verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T5_Cookie_Verification.png)

![Cookie deleted](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T5_Delete_Cookie.png)

### Result

The cookie was successfully verified and deleted using the Express response cookie utilities.

## Task 6: Query String Handling

### Task Given

The task required reading query string values from the URL and using them in the server response.

### Implementation

The `/welcome` route reads `user` and `role` from `req.query`. For a URL such as `/welcome?user=Sehaj&role=admin`, the route returns a response containing both values.

### Code Location

- [Lecture 6 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6)
- [app.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture6/app.js)

### Screenshot

![Query string response](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture6/screenshots/L6_T6_Query_String.png)

### Result

The application successfully extracted query string parameters from the URL and displayed them in the response.

## Project Structure

```text
Theory/Unit1/Lecture6/
+-- app.js
+-- package.json
+-- package-lock.json
+-- screenshots/
|   +-- L6_T2_Login_Session.png
|   +-- L6_T2_Profile_Session.png
|   +-- L6_T2_Server_Running.png
|   +-- L6_T3_Logout_Session_Destroyed.png
|   +-- L6_T3_Profile_After_Logout.png
|   +-- L6_T4_Get_Cookie.png
|   +-- L6_T4_Server_Running.png
|   +-- L6_T4_Set_Cookie.png
|   +-- L6_T5_Cookie_Verification.png
|   +-- L6_T5_Delete_Cookie.png
|   +-- L6_T6_Query_String.png
+-- Report.md
```

## Concepts Used

- HTTP statelessness
- Server-side session management
- Session ID cookies
- Express middleware
- `express-session`
- `cookie-parser`
- Creating cookies with `res.cookie()`
- Reading cookies with `req.cookies`
- Deleting cookies with `res.clearCookie()`
- Query string handling with `req.query`
- Basic login, profile, and logout flow

## Overall Result

The experiment successfully implemented state management mechanisms in an Express.js backend application. Sessions were used to maintain login state, cookies were created and deleted through server routes, and query strings were processed from URL parameters.

## Observations

- The actual implementation is located under `Theory/Unit1/Lecture6`, not under `Lab/Exp 6`.
- The project uses a single `app.js` file for all session, cookie, and query string routes.
- The session stores the username `Sehaj` on the server side.
- The session cookie has a configured maximum age of `60000` milliseconds.
- The custom `username` cookie uses `httpOnly: true`, which prevents client-side JavaScript access.
- The `secure` option is set to `false`, which is suitable for local HTTP testing but should be changed for HTTPS deployment.
- Query string values are visible in the URL and should not be used for sensitive information.
- The project uses in-memory session storage, so session data is temporary and not suitable for production persistence.

## Conclusion

This experiment demonstrated how backend applications maintain state over stateless HTTP using sessions, cookies, and query strings. The Express.js implementation showed how login state can be stored on the server, how cookies can be set and cleared through responses, and how URL parameters can be read through query strings. The experiment provides a practical foundation for authentication, user preference handling, and request-based state management.

## Experiment Link

GitHub Pages Link: Not published as a GitHub Pages experiment because the implementation requires a local Express.js server.

Complete Experiment Source Code: [Theory/Unit1/Lecture6](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture6)
