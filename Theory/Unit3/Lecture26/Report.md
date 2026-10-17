# Lecture 26

## Title

Django Framework: Detailed Overview, Architecture, and Setup

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

To install and configure Django in a Python virtual environment, create a Django project and a `students` application, configure URL routing, and implement a basic endpoint that returns a JSON response for the Student Management API.

## Software Requirements

- Python
- Django
- Visual Studio Code
- PowerShell terminal
- Web browser

The implementation uses Django's default project structure and the `JsonResponse` class supplied by Django. No additional API framework is required for the demonstrated endpoint.

## Problem Statement

Set up a Django project for a Student Management API. Create and register a `students` application, configure the root URL to call a view, and return a JSON response containing a message, version, and running status.

## Task Summary

| Task                     | Description                                               | Implementation                                                                                                                                        |
| ------------------------ | --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Task 1: Django Setup     | Create an isolated Python environment and install Django. | A virtual environment was created, Django was installed, and the installed version was checked.                                                       |
| Task 2: Project Creation | Create the Django project structure.                      | The `student_system` project was created with `manage.py` and the inner project configuration package.                                                |
| Task 3: Students App     | Create and register the application.                      | The `students` app was created and added to `INSTALLED_APPS`. Django's system check reported no issues after the configuration was corrected.         |
| Task 4: Basic View       | Configure a basic view and map the root URL.              | The `index` view returned a plain text HTTP response, and the root URL was mapped to that view. The browser displayed the expected welcome message.   |
| Task 5: JSON API         | Return the final API response in JSON format.             | The `index` view was updated to return a JSON object containing `message`, `version`, and `status`. The browser displayed the expected JSON response. |

## Task 1: Django Setup

### Task Given

Create a Python virtual environment, install Django, and verify that Django is available in the environment.

### Implementation

A virtual environment named `venv` was created under `Task1_Django_Setup`. Django was installed in that environment and its version was verified with the Django command line module. During the later app creation step, the terminal was reactivated in the same environment after a `No module named 'django'` error. The command then ran successfully.

The virtual environment is an execution dependency and should not be included in the GitHub source commit.

### Code Location

- [Task1_Django_Setup folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Task1_Django_Setup)
- [Django setup screenshot folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Task1_Django_Setup/screenshots)

### Screenshot

![Django installation and version verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Task1_Django_Setup/screenshots/django_installation.png)

### Result

Django was installed and its version verification was completed in the virtual environment.

## Task 2: Project Creation

### Task Given

Create a Django project named `student_system` and verify that its initial structure and configuration are valid.

### Implementation

The project was created using Django's project creation command. The generated project includes `manage.py` and the inner `student_system` package, which contains the project configuration files. The command `python manage.py check` returned `System check identified no issues (0 silenced).`

The working Django project is located under `Task1_Django_Setup/student_system`; the Task 2 folder contains the evidence screenshot. The project was not duplicated into a second independent Django project.

### Code Location

- [Django project folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Task1_Django_Setup/student_system)
- [manage.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/manage.py)
- [Project settings](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/student_system/settings.py)
- [Project URL configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/student_system/urls.py)

### Screenshot

![Django project structure](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Task2_Project_Creation/screenshots/project_structure.png)

### Result

The `student_system` project was created, and Django's system check passed without reported issues.

## Task 3: Students App

### Task Given

Create a Django application named `students` and register it in the project's `INSTALLED_APPS` setting.

### Implementation

The `students` app was generated with Django's `startapp` command. Its generated files include `admin.py`, `apps.py`, `models.py`, `tests.py`, `views.py`, `__init__.py`, and the `migrations` directory. The app was added to `INSTALLED_APPS` in `student_system/settings.py`.

An initial configuration error occurred because the `students` entry was not separated from `django.contrib.staticfiles`. After correcting the comma and saving the configuration, `python manage.py check` reported no issues.

### Code Location

- [Students app folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Task1_Django_Setup/student_system/students)
- [App configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/students/apps.py)
- [Project settings](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/student_system/settings.py)

### Screenshot

![Students app registration and Django system check](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Task3_Students_App/screenshots/students_app_registered.png)

### Result

The `students` app was created and registered successfully. The corrected project configuration passed Django's system check.

## Task 4: Basic Django View

### Task Given

Create a basic Django view and map the root URL to it so that the application returns a welcome message.

### Implementation

The `index` function in `students/views.py` was first implemented using Django's `HttpResponse`. The root URL in `student_system/urls.py` was mapped to `views.index`. When the development server was running, opening the root URL in a browser displayed the message:

`Welcome to the Student Management API (Django)`

The view was subsequently updated for Task 5 to return JSON. The current `views.py` therefore contains the final JSON implementation rather than the earlier plain text version.

### Code Location

- [Students view](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/students/views.py)
- [Project URL configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/student_system/urls.py)

### Screenshot

![Basic Django view response in the browser](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Task4_Basic_View/screenshots/basic_view_output.png)

### Result

The root URL successfully reached the Django view and displayed the expected plain text welcome message at the time of testing.

## Task 5: JSON API

### Task Given

Update the basic view to return a JSON response for the Student Management API.

### Implementation

The final `index` view uses Django's `JsonResponse` and returns the following fields:

- `message`: `Welcome to the Student Management API`
- `version`: `1.0`
- `status`: `running`

The existing root URL mapping was retained. The development server was run, and the browser displayed the JSON response at the root URL.

### Code Location

- [Final JSON view implementation](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/students/views.py)
- [Root URL configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Task1_Django_Setup/student_system/student_system/urls.py)
- [Task 5 folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Task5_JSON_API)

### Screenshot

![Student Management API JSON response](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Task5_JSON_API/screenshots/student_api_json_response.png)

### Result

The root endpoint returned a JSON response containing the expected message, version, and running status. This verifies the final response implementation shown in the lecture.

## Project Structure

The task folders are located directly under `Theory/Unit3`. The working Django project and virtual environment are under `Task1_Django_Setup`; the remaining task folders contain their corresponding screenshots.

```text
Theory/
└── Unit3/
    ├── Task1_Django_Setup/
    │   ├── screenshots/
    │   │   └── django_installation.png
    │   ├── student_system/
    │   │   ├── manage.py
    │   │   ├── db.sqlite3
    │   │   ├── student_system/
    │   │   │   ├── __init__.py
    │   │   │   ├── settings.py
    │   │   │   ├── urls.py
    │   │   │   ├── asgi.py
    │   │   │   └── wsgi.py
    │   │   └── students/
    │   │       ├── migrations/
    │   │       ├── __init__.py
    │   │       ├── admin.py
    │   │       ├── apps.py
    │   │       ├── models.py
    │   │       ├── tests.py
    │   │       └── views.py
    │   └── venv/
    ├── Task2_Project_Creation/
    │   └── screenshots/
    │       └── project_structure.png
    ├── Task3_Students_App/
    │   └── screenshots/
    │       └── students_app_registered.png
    ├── Task4_Basic_View/
    │   └── screenshots/
    │       └── basic_view_output.png
    └── Task5_JSON_API/
        └── screenshots/
            └── student_api_json_response.png
```

## Concepts Used

- Python virtual environments
- Django installation and version verification
- Django project and application structure
- Application registration through `INSTALLED_APPS`
- Django system checks
- View functions
- URL routing with `path()`
- HTTP responses with `HttpResponse`
- JSON responses with `JsonResponse`
- Running and verifying a Django development server

## Overall Result

A Django project named `student_system` and its `students` application were created. The application was registered in the project settings, the root URL was mapped to the `index` view, and the final view returned the expected JSON response for the Student Management API. The implementation and the five task screenshots were recorded in the project structure.

## Observations

- Django commands must be executed using the Python environment in which Django is installed. An inactive or different environment caused a `ModuleNotFoundError` until the virtual environment was activated.
- The `students` application must be listed as a separate entry in `INSTALLED_APPS`. A missing comma caused Django to interpret two app names as one module path.
- `python manage.py check` reported no issues after the app registration was corrected.
- The same root URL mapping was retained when the view changed from a plain text response to a JSON response.
- The final implementation demonstrates a basic JSON endpoint. It does not implement student CRUD operations, database models for student records, authentication, or Django REST Framework.

## Conclusion

The lecture demonstrated the initial setup of Django and the structure of a Django project and app. A basic view was connected to the root URL and then updated to return JSON using `JsonResponse`. The final browser response confirmed that the Student Management API endpoint was running with the expected message, version, and status fields.

## Experiment Link

This lecture was not confirmed as published on GitHub Pages.

## GitHub Source Code

[Open the complete Lecture 26 task folder collection](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3)

[Open the Django project source folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Task1_Django_Setup/student_system)
