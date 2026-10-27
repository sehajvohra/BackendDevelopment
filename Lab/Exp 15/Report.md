# Experiment 15

## Title

Django To Do Application

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

To build a Django To Do application using SQLite and demonstrate task
CRUD operations, Django Admin configuration, reusable templates, static
assets, responsive styling, and basic application verification.

## Software Requirements

-   Python 3.x
-   Django 6.1.2
-   SQLite
-   Visual Studio Code or another code editor
-   A web browser
-   Python virtual environment

Dependency file:
[`requirements.txt`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/requirements.txt)

## Problem Statement

Build a Django To Do application that allows users to create tasks, view
the task list, mark tasks as completed or incomplete, and delete tasks.
Extend the application with Django Admin configuration, reusable
templates, CSS, JavaScript, a logo image, and a responsive page layout.

## Task Summary

  -----------------------------------------------------------------------
  Task                    Description             Implementation
  ----------------------- ----------------------- -----------------------
  Task 1                  Project setup and       Created the
                          configuration           `todo_project` Django
                                                  project and `todo`
                                                  application, registered
                                                  the app, and configured
                                                  URL routing.

  Task 2                  Task model and database Defined the `Task`
                                                  model and applied
                                                  migrations.

  Task 3                  Task management CRUD    Implemented task
                                                  listing, creation,
                                                  completion toggling,
                                                  and deletion. POST
                                                  forms include CSRF
                                                  tokens.

  Task 4                  Django Admin            Registered `Task` with
                                                  list display,
                                                  completion filtering,
                                                  title search, and
                                                  editable completion
                                                  status.

  Task 5                  Reusable templates      Added a shared base
                                                  template, header and
                                                  footer includes, and
                                                  page templates using
                                                  template inheritance.

  Task 6                  Static assets and       Added CSS, JavaScript,
                          responsive styling      a logo image, and a
                                                  narrow screen media
                                                  query.

  Task 7                  Application             Manually checked CRUD
                          verification            workflows, the admin
                                                  interface, static
                                                  assets, mobile layout,
                                                  and persistence after
                                                  restarting the server.
  -----------------------------------------------------------------------

## Task 1: Project Setup and Configuration

### Task Given

Create a Django project and application, register the application in
project settings, and configure URL routing.

### Implementation

The project was created directly inside `Lab/Exp 15`. The Django project
package is `todo_project` and the application is `todo`. The app is
registered in `INSTALLED_APPS`. The project URL configuration includes
the app's URL patterns at the root path and retains the Django Admin
route.

### Code Location

-   [`manage.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/manage.py)
-   [`settings.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo_project/settings.py)
-   [`Project URL configuration`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo_project/urls.py)
-   [`todo application folder`](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2015/todo)

### Screenshot

![Task Tracker home
page](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/home-page.png)

### Result

The project and application were configured, and the development server
was opened in a browser to display the task list page.

## Task 2: Task Model and Database Migrations

### Task Given

Define a task model and use Django migrations to create its database
table.

### Implementation

The `Task` model contains `title`, a character field with a maximum
length of 200; `completed`, a Boolean field defaulting to `False`; and
`created_at`, a timestamp populated automatically when a record is
created. The model's string representation returns the task title.
Migrations were generated and applied. The project uses SQLite.

### Code Location

-   [`models.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/models.py)
-   [`migrations folder`](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2015/todo/migrations)
-   [`settings.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo_project/settings.py)

### Screenshot

![Task created in the
application](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-created.png)

### Result

The model migration was applied, and task records were stored in SQLite.
Persistence was checked by restarting the development server.

## Task 3: Task Management CRUD Operations

### Task Given

Implement Create, Read, Update, and Delete operations for tasks.

### Implementation

-   **Create:** The add task view accepts a POST request, trims the
    title, creates a record when the title is not empty, and redirects
    to the task list.
-   **Read:** The list view retrieves tasks ordered by creation time,
    newest first.
-   **Update:** The toggle view changes the completion status and
    accepts POST requests only.
-   **Delete:** The delete view removes the selected task and accepts
    POST requests only.

The templates include CSRF tokens in POST forms. The list page displays
a helpful message when no tasks exist.

### Code Location

-   [`views.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/views.py)
-   [`todo/urls.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/urls.py)
-   [`task_list.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/task_list.html)
-   [`add_task.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/add_task.html)

### Screenshots

![Task
created](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-created.png)

![Task marked
completed](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-completed.png)

![Empty task list after
deletion](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/empty-task-list.png)

### Result

Task creation, listing, completion toggling, and deletion were manually
tested in the browser. The empty state was checked after removing the
task.

## Task 4: Django Admin Configuration

### Task Given

Register the task model in Django Admin and configure list display,
filtering, searching, and editing.

### Implementation

The `Task` model is registered with a custom `TaskAdmin` class. The
admin list displays the title, completion status, and creation time.
Completion status can be filtered, titles can be searched, and
completion status can be edited directly in the list. A superuser was
created and used to sign in.

### Code Location

-   [`admin.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/admin.py)
-   [`models.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/models.py)

### Screenshots

![Django Admin
dashboard](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/admin-dashboard.png)

![Tasks in Django
Admin](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/admin-task-list.png)

### Result

The admin login succeeded, the task model appeared in Django Admin, and
a task created through the application was checked in the admin task
list.

## Task 5: Reusable Templates and Template Inheritance

### Task Given

Create a shared page layout and reusable header and footer templates to
reduce repeated HTML.

### Implementation

`base.html` defines the shared document structure, title and content
blocks, stylesheet reference, header and footer includes, and JavaScript
reference. `header.html` contains the logo and navigation. `footer.html`
contains the footer text. Both `task_list.html` and `add_task.html`
extend the base template.

### Code Location

-   [`base.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/base.html)
-   [`header.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/header.html)
-   [`footer.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/footer.html)
-   [`task_list.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/task_list.html)
-   [`add_task.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/add_task.html)

### Screenshot

![Styled add task page with shared header and
footer](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/add-task-page.png)

### Result

The list and add task pages use the common layout, shared navigation,
and footer through template inheritance and includes.

## Task 6: Static Assets and Responsive Styling

### Task Given

Add separate CSS and JavaScript files, display a logo, and style the
application for desktop and mobile layouts.

### Implementation

`style.css` defines the page layout, panels, task rows, action buttons,
form controls, header, and footer. It includes a media query for screens
narrower than 600 pixels. `app.js` focuses the task title input when
present and logs a message after the page loads. `logo.png` is displayed
in the header with alternative text and explicit dimensions. The
templates load these assets using Django's static template tag.

The browser developer tools were used to inspect the JavaScript console
and network requests. The CSS, JavaScript, and logo requests were
reported as successful with HTTP 200. The mobile layout was also
inspected at a narrow viewport.

### Code Location

-   [`style.css`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/static/todo/css/style.css)
-   [`app.js`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/static/todo/js/app.js)
-   [`logo.png`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/static/todo/images/logo.png)
-   [`base.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/base.html)
-   [`header.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/header.html)

### Screenshot

![Responsive Task Tracker layout on a mobile
viewport](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/mobile-layout.png)

### Result

The application loaded its CSS, JavaScript, and logo assets. The console
message was observed, and the responsive layout was inspected on a
narrow viewport.

## Task 7: Application Verification

### Task Given

Run the application and verify its main workflows, administration
interface, static assets, responsive layout, and data persistence.

### Implementation

The application was run with Django's development server. Manual browser
checks covered task creation, completion toggling, deletion, the empty
task list, and Django Admin. Developer tools were used to inspect the
console and static asset requests. The server was stopped and restarted
to check task persistence. The final Django system check was reported to
return `System check identified no issues (0 silenced).`

### Code Location

-   [`views.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/views.py)
-   [`todo/urls.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/urls.py)
-   [`models.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/models.py)
-   [`admin.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/admin.py)

### Screenshots

![Task list after creating a
task](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-created.png)

![Task persistence check after restarting the
server](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/persistence-check.png)

### Result

Manual checks covered the main CRUD workflows, Django Admin, static
asset delivery, mobile layout, and persistence in SQLite. The final
Django system check reported no configuration issues. No automated test
suite was reported.

## Project Structure

The following structure describes the main implementation files and the
screenshot files shown in the supplied folder listing. The screenshot
folder listing also includes `home-page.png` and
`persistence-check.png`. The local virtual environment should not be
committed.

``` text
Lab/Exp 15/
├── manage.py
├── requirements.txt
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── todo/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── templates/
│   │   └── todo/
│   │       ├── base.html
│   │       ├── header.html
│   │       ├── footer.html
│   │       ├── task_list.html
│   │       └── add_task.html
│   └── static/
│       └── todo/
│           ├── css/
│           │   └── style.css
│           ├── js/
│           │   └── app.js
│           └── images/
│               └── logo.png
└── screenshots/
    ├── home-page.png
    ├── task-created.png
    ├── task-completed.png
    ├── empty-task-list.png
    ├── admin-dashboard.png
    ├── admin-task-list.png
    ├── add-task-page.png
    ├── mobile-layout.png
    └── persistence-check.png
```

## Concepts Used

-   Django project and app structure
-   Model View Template architecture
-   URL routing and request handling
-   Django ORM and SQLite
-   Database migrations
-   Create, Read, Update, and Delete operations
-   HTTP POST handling and CSRF protection
-   Django Admin customization
-   Template inheritance and includes
-   Django static file handling
-   CSS layout and responsive media queries
-   JavaScript DOM events and input focus
-   Browser developer tools and HTTP status verification
-   Persistence of database records across server restarts

## Overall Result

A Django Task Tracker application was implemented with task creation,
listing, completion toggling, deletion, Django Admin integration,
reusable templates, CSS styling, JavaScript input focus, a logo image,
and a responsive layout. Manual checks covered the principal workflows,
static assets, and SQLite persistence.

## Observations

1.  Django separates data, request handling, routing, and presentation
    through models, views, URL configuration, and templates.
2.  The `Task` model stores a title, completion state, and creation
    timestamp.
3.  Migrations apply model changes to the SQLite schema.
4.  Completion changes and deletion use POST only views.
5.  POST forms include CSRF tokens.
6.  Django Admin provides an additional interface for managing tasks.
7.  Template inheritance and includes reduce repeated page structure.
8.  Static asset requests were reported as HTTP 200 during browser
    inspection.
9.  A CSS media query adapts the layout for narrow screens.
10. Task data remained available after restarting the development
    server.
11. The final Django system check reported no configuration issues.
12. Verification was manual; no automated test suite was reported.

## Conclusion

This experiment demonstrates a Django web application using the MVT
pattern and SQLite. It combines model definition and migrations with URL
routing, views, templates, CRUD operations, Django Admin, reusable page
components, static assets, and responsive CSS. The reported manual
checks indicate that the main application workflows and presentation
features operated as expected.

## Experiment Link

No experiment specific GitHub Pages URL was provided for this
application.

## Complete Experiment Source Code

[Experiment 15: Django To Do
Application](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2015)
