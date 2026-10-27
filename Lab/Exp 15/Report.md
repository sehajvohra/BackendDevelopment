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

To develop a task management web application using Django and SQLite,
demonstrating the Django project and app structure, the Model View
Template architecture, database migrations, CRUD operations, Django
Admin, reusable templates, static assets, responsive styling, and basic
browser based verification.

## Software Requirements

-   Python 3.x
-   Django 6.1.2
-   SQLite
-   Visual Studio Code or another code editor
-   A web browser
-   Python virtual environment

The project dependency is recorded in
[`requirements.txt`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/requirements.txt).

## Problem Statement

Build a Django To Do application that allows users to create tasks, view
the task list, mark tasks as completed or incomplete, and delete tasks.
Extend the application with Django Admin configuration, reusable
templates, CSS, JavaScript, a logo image, and a responsive page layout.

## Task Summary

  -----------------------------------------------------------------------
  Task                    Description             Implementation
  ----------------------- ----------------------- -----------------------
  Task 1                  Project setup and       Created the Django
                          configuration           project and `todo`
                                                  application, registered
                                                  the app, and configured
                                                  project URL routing.

  Task 2                  Task model and database Defined the `Task`
                          setup                   model and applied
                                                  Django migrations to
                                                  create its database
                                                  table.

  Task 3                  Task management CRUD    Implemented task
                                                  listing, task creation,
                                                  completion toggling,
                                                  and deletion through
                                                  Django views and URL
                                                  routes. POST forms
                                                  include CSRF tokens.

  Task 4                  Django Admin            Registered `Task` with
                                                  list display,
                                                  completion filtering,
                                                  title search, and
                                                  editable completion
                                                  status.

  Task 5                  Reusable templates      Added a shared base
                                                  template, reusable
                                                  header and footer, and
                                                  page templates that use
                                                  template inheritance.

  Task 6                  Static assets and       Added CSS, JavaScript,
                          responsive styling      and a logo image. The
                                                  CSS includes a narrow
                                                  screen media query.

  Task 7                  Application             Tested CRUD behaviour,
                          verification            the admin interface,
                                                  static file delivery,
                                                  mobile layout, and
                                                  persistence after
                                                  restarting the
                                                  development server.
  -----------------------------------------------------------------------

## Task 1: Project Setup and Configuration

### Task Given

Create a Django project and application, register the application in the
project settings, and configure the URL routing.

### Implementation

The project was created directly inside `Lab/Exp 15`, with the Django
project package named `todo_project` and the application named `todo`.
The `todo` app was added to `INSTALLED_APPS`. The project URL
configuration includes the application's URL patterns at the root path
and retains the Django Admin route.

### Code Location

-   [`manage.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/manage.py)
-   [`todo_project/settings.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo_project/settings.py)
-   [`todo_project/urls.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo_project/urls.py)
-   [`todo/`](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2015/todo)

### Screenshot

![Task list page showing the Task Tracker
application](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-created.png)

### Result

The Django project and application were created and configured. The
development server was run locally and the task list page was opened in
the browser.

## Task 2: Task Model and Database Migrations

### Task Given

Define a model for tasks and use Django migrations to create the
corresponding database table.

### Implementation

The `Task` model contains three fields: `title`, a character field with
a maximum length of 200; `completed`, a Boolean field that defaults to
`False`; and `created_at`, a date and time field populated automatically
when a record is created. The model defines a string representation
using the task title. Django migration commands were run to create and
apply the model migration. SQLite is used as the project's database.

### Code Location

-   [`todo/models.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/models.py)
-   [`todo/migrations/`](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2015/todo/migrations)
-   [`todo_project/settings.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo_project/settings.py)

### Screenshot

![Task list containing a created
task](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-created.png)

### Result

The task model and its database migrations were created and applied.
Task records were stored in the SQLite database and remained available
after the development server was stopped and restarted.

## Task 3: Task Management CRUD Operations

### Task Given

Implement the Create, Read, Update, and Delete operations required for a
basic task management application.

### Implementation

The application provides the following operations:

-   **Create:** The add task view accepts a POST request, trims the
    submitted title, creates a record when the title is not empty, and
    redirects to the task list.
-   **Read:** The task list view retrieves tasks ordered by creation
    time, newest first, and renders them in the task list template.
-   **Update:** The toggle view changes a task's completion status. The
    view accepts POST requests only.
-   **Delete:** The delete view removes the selected task and redirects
    to the task list. The view accepts POST requests only.

The templates include CSRF tokens in the task creation, completion, and
deletion forms. The list page also displays an empty state when there
are no tasks.

### Code Location

-   [`todo/views.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/views.py)
-   [`todo/urls.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/urls.py)
-   [`todo/templates/todo/task_list.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/task_list.html)
-   [`todo/templates/todo/add_task.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/add_task.html)

### Screenshots

![Task successfully
created](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-created.png)

![Task marked as
completed](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-completed.png)

![Empty task list after deleting the
task](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/empty-task-list.png)

### Result

The task creation, listing, completion toggle, and deletion workflows
were tested in the browser. The empty state was also checked after the
task list was cleared.

## Task 4: Django Admin Configuration

### Task Given

Register the task model in Django Admin and configure the task list
display, filtering, search, and editing options.

### Implementation

The `Task` model is registered using a custom `TaskAdmin` class. The
admin list displays the title, completion status, and creation time. The
completion field can be filtered, task titles can be searched, and the
completion status can be edited directly from the list. A superuser was
created and used to access the Django Admin interface.

### Code Location

-   [`todo/admin.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/admin.py)
-   [`todo/models.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/models.py)

### Screenshots

![Django Admin
dashboard](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/admin-dashboard.png)

![Task records in Django
Admin](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/admin-task-list.png)

### Result

The Django Admin login succeeded, the task model appeared in the admin
interface, and a task created through the application was checked in the
admin task list.

## Task 5: Reusable Templates and Template Inheritance

### Task Given

Reduce repeated page markup by creating a shared base template and
reusable header and footer templates.

### Implementation

The `base.html` template defines the shared document structure, page
title block, content block, stylesheet reference, header include, footer
include, and JavaScript reference. The `header.html` template contains
the Task Tracker logo and navigation links. The `footer.html` template
contains the application footer text. Both `task_list.html` and
`add_task.html` extend the base template and provide page specific
content.

### Code Location

-   [`todo/templates/todo/base.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/base.html)
-   [`todo/templates/todo/header.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/header.html)
-   [`todo/templates/todo/footer.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/footer.html)
-   [`todo/templates/todo/task_list.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/task_list.html)
-   [`todo/templates/todo/add_task.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/add_task.html)

### Screenshot

![Styled add task page with shared header and
footer](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/add-task-page.png)

### Result

The task list and add task pages use the shared layout. The header,
navigation, footer, and page content are rendered through template
inheritance and includes.

## Task 6: Static Assets and Responsive Styling

### Task Given

Separate CSS and JavaScript from the HTML templates, add a logo image,
and style the interface for desktop and narrow mobile screens.

### Implementation

The application uses the following static assets:

-   `style.css` defines page layout, panels, task rows, action buttons,
    form controls, header, footer, and a media query for screens
    narrower than 600 pixels.
-   `app.js` focuses the task title input when it is present and logs a
    message to the browser console when the page loads.
-   `logo.png` is displayed in the header with alternative text and
    explicit dimensions.

The base template loads the assets using Django's static template tag.
Browser developer tools were used to check the JavaScript console and
confirm that the CSS, JavaScript, and logo requests returned HTTP 200
responses. The layout was also inspected at a mobile viewport width.

### Code Location

-   [`todo/static/todo/css/style.css`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/static/todo/css/style.css)
-   [`todo/static/todo/js/app.js`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/static/todo/js/app.js)
-   [`todo/static/todo/images/logo.png`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/static/todo/images/logo.png)
-   [`todo/templates/todo/base.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/base.html)
-   [`todo/templates/todo/header.html`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/templates/todo/header.html)

### Screenshots

![Network panel showing successful static asset
requests](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/static-files-network.png)

![Task Tracker layout at a mobile viewport
width](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/mobile-layout.png)

### Result

The browser loaded the stylesheet, JavaScript file, and logo
successfully. The JavaScript console message was observed, and the
responsive layout was inspected at a narrow viewport.

## Task 7: Application Verification

### Task Given

Run the Django application and verify the principal workflows,
administrative interface, static assets, responsive layout, and data
persistence.

### Implementation

The application was run using Django's development server. Browser
checks covered task creation, marking tasks complete and incomplete,
deletion, the empty task list, and access to Django Admin. Developer
tools were used to inspect the console and network requests. The server
was stopped and restarted to check that stored tasks persisted in
SQLite. The Django system check was also run and reported no issues.

### Code Location

-   [`todo/views.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/views.py)
-   [`todo/urls.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/urls.py)
-   [`todo/models.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/models.py)
-   [`todo/admin.py`](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%2015/todo/admin.py)

### Screenshots

![Task creation
verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/task-created.png)

![Admin task list
verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%2015/screenshots/admin-task-list.png)

### Result

The reported browser tests covered the main CRUD operations, the admin
interface, static asset delivery, mobile layout, and SQLite persistence.
The final Django system check reported
`System check identified no issues (0 silenced).` No automated test
suite was reported for this experiment.

## Project Structure

The following structure represents the files used by the implementation.
The `venv` directory is a local development environment and should not
be committed to the repository.

``` text
Lab/Exp 15/
├── manage.py
├── requirements.txt
├── todo_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todo/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
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
    ├── task-created.png
    ├── task-completed.png
    ├── empty-task-list.png
    ├── admin-dashboard.png
    ├── admin-task-list.png
    ├── add-task-page.png
    ├── static-files-network.png
    └── mobile-layout.png
```

## Concepts Used

-   Django project and application structure
-   Model View Template architecture
-   Django settings and URL routing
-   Django ORM and model fields
-   SQLite database
-   Database migrations
-   Create, Read, Update, and Delete operations
-   HTTP GET and POST handling
-   CSRF protection for POST forms
-   Django Admin registration and customization
-   Template inheritance using `extends` and `block`
-   Template composition using `include`
-   Django static file handling
-   CSS layout and responsive media queries
-   JavaScript DOM event handling and input focus
-   Browser developer tools, Console, and Network inspection
-   Persistence of database records across server restarts

## Overall Result

A Django based Task Tracker application was implemented with task
creation, listing, completion toggling, deletion, Django Admin
integration, reusable templates, CSS styling, JavaScript input focus, a
logo image, and a responsive layout. The reported manual checks covered
the principal user workflows, static asset requests, and persistence of
task records in SQLite.

## Observations

1.  Django separates application data, request handling, URL routing,
    and HTML presentation into models, views, URL configurations, and
    templates.
2.  The `Task` model stores a title, completion state, and creation
    timestamp.
3.  Database migrations connect model definitions to the SQLite schema.
4.  Task state changes and deletion are handled through POST-only views.
5.  CSRF tokens are included in the application's POST forms.
6.  The Django Admin interface provides a second way to view and manage
    task records.
7.  Template inheritance and includes reduce duplicated page structure.
8.  Static asset requests returned HTTP 200 during browser inspection.
9.  The CSS media query changes the layout for narrow screens.
10. SQLite data remained available after restarting the development
    server.
11. The final Django system check reported no configuration issues.
12. The report documents manual verification; an automated test suite
    was not reported.

## Conclusion

This experiment demonstrates the development of a small Django web
application using the MVT pattern and SQLite. It combines database
models and migrations with URL routing, views, templates, CRUD
operations, Django Admin, reusable page components, static files, and
responsive CSS. The completed manual checks provide evidence that the
principal application workflows and presentation features operated as
expected.

## Experiment Link

No experiment specific GitHub Pages URL was confirmed for this
application.

## Complete Experiment Source Code

[Experiment 15: Django To Do
Application](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%2015)
