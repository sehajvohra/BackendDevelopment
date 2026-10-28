# Lecture 29

## Title

Testing and Debugging Django Applications

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

To practice Django testing and debugging by verifying endpoint
responses, running tests, testing model behavior, mocking external
service calls, and diagnosing an intentionally introduced defect.

## Software Requirements

-   Python 3.13
-   Django 6.1.2
-   `requests` 2.34.2
-   SQLite, as configured by the Django projects
-   Visual Studio Code or another code editor
-   Windows PowerShell
-   Git and GitHub

## Problem Statement

The lecture covers testing and debugging Django applications. The hands
on work includes testing a health endpoint and a parameterized endpoint,
running Django tests, mocking an external service, and diagnosing a
deliberate HTTP status code defect. The PBL activity extends this work
with a Student API, model tests, mocked service success and timeout
tests, and defect diagnosis.

This report documents the implementation in `Theory/Unit3/Lecture29/`.
The separate task folders are not treated as one combined Django
project.

## Task Summary

  -------------------------------------------------------------------------
  Task                    Description             Implementation
  ----------------------- ----------------------- -------------------------
  Task 1                  Test the health         A named health route
                          endpoint                returns JSON status `ok`
                                                  with HTTP 200 and is
                                                  tested with Django's test
                                                  client.

  Task 2                  Test a parameterized    A student detail route
                          endpoint                accepts `student_id` and
                                                  returns the identifier in
                                                  JSON.

  Task 3                  Run Django tests        Test run evidence is
                                                  stored in the task
                                                  folder. It has no
                                                  separate Django project.

  Task 4                  Test a mocked external  `fetch_external_data()`
                          service                 handles a mocked timeout
                                                  and returns a safe error
                                                  result.

  Task 5                  Diagnose an intentional Returning HTTP 201 caused
                          defect                  an assertion failure;
                                                  restoring HTTP 200 made
                                                  the test pass.

  PBL Activity            Test and debug the      A separate Django project
                          Student API             implements health, list,
                                                  and detail endpoints, a
                                                  `Student` model, and
                                                  seven tests.
  -------------------------------------------------------------------------

## Task 1: Test the Health Endpoint

### Task Given

Test the health endpoint using its named URL and verify HTTP 200 and
JSON status `ok`.

### Implementation

The separate project in `Task1_Test_Health_Endpoint/student_system/`
defines a health view, a route named `health-check`, and a test using
Django's test client and `reverse()`. The recorded test passed.

### Code Location

-   [Health endpoint
    view](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task1_Test_Health_Endpoint/student_system/students/views.py)
-   [Health endpoint
    test](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task1_Test_Health_Endpoint/student_system/students/tests.py)
-   [URL
    configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task1_Test_Health_Endpoint/student_system/student_system/urls.py)
-   [Task 1
    folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Lecture29/Task1_Test_Health_Endpoint)

### Screenshot

![Task 1 health endpoint
test](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/Task1_Test_Health_Endpoint/screenshots/task1-health-endpoint-test.png)

### Result

The health endpoint test passed and confirmed the expected HTTP 200
response and JSON status value.

## Task 2: Test a Parameterized Endpoint

### Task Given

Request the student detail endpoint with `student_id` 42 and verify the
HTTP status and returned JSON identifier.

### Implementation

The separate project in
`Task2_Test_Parameterized_Endpoint/student_system/` defines a student
detail view and a route named `student-detail`. The test uses
`reverse()` with `kwargs` and checks for HTTP 200 and `student_id` equal
to 42.

### Code Location

-   [Parameterized endpoint
    view](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task2_Test_Parameterized_Endpoint/student_system/students/views.py)
-   [Parameterized endpoint
    test](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task2_Test_Parameterized_Endpoint/student_system/students/tests.py)
-   [URL
    configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task2_Test_Parameterized_Endpoint/student_system/student_system/urls.py)
-   [Task 2
    folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Lecture29/Task2_Test_Parameterized_Endpoint)

### Screenshot

![Task 2 parameterized endpoint
test](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/Task2_Test_Parameterized_Endpoint/screenshots/task2-parameterized-endpoint-test.png)

### Result

The parameterized endpoint test passed, confirming that the requested
identifier was returned in JSON.

## Task 3: Run Django Tests

### Task Given

Run Django's test runner and use targeted test classes or methods while
debugging.

### Implementation

`Task3_Run_Tests` contains a screenshot rather than its own `manage.py`
or independent Django project. The related Task 2 project contains the
test file and project used for the endpoint testing exercise. The
recorded Task 2 run found and passed one test. No combined test suite
across the Lecture 29 task folders is claimed.

### Code Location

-   [Related Task 2 test
    file](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task2_Test_Parameterized_Endpoint/student_system/students/tests.py)
-   [Related Task 2
    manage.py](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task2_Test_Parameterized_Endpoint/student_system/manage.py)
-   [Task 3 evidence
    folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Lecture29/Task3_Run_Tests)

### Screenshot

![Task 3 test run
evidence](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/Task3_Run_Tests/screenshots/task3-full-test-suite.png)

### Result

The screenshot records a test run. The Task 3 folder itself contains
evidence only, so it is not described as a standalone Django project or
a combined suite for all task folders.

## Task 4: Test a Mocked External Service

### Task Given

Mock an external HTTP request and verify timeout handling without making
a real network request. The timeout result should contain `data: None`
and the error `External service timed out`.

### Implementation

The separate project in `Task4_Test_Mocked_Service/student_system/`
includes `students/utils.py`. Its `fetch_external_data(url)` function
calls `requests.get()` with a timeout, checks the response, and handles
`requests.Timeout`. The test patches `students.utils.requests.get` and
simulates a timeout.

### Code Location

-   [External service
    utility](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task4_Test_Mocked_Service/student_system/students/utils.py)
-   [Mocked service
    test](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task4_Test_Mocked_Service/student_system/students/tests.py)
-   [Task 4
    folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Lecture29/Task4_Test_Mocked_Service)

### Screenshot

![Task 4 mocked service timeout
test](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/Task4_Test_Mocked_Service/screenshots/task4-mocked-service-timeout-test.png)

### Result

The timeout test passed. Mocking the network call made the test
independent of a live external service.

## Task 5: Diagnose an Intentional Defect

### Task Given

Change the health endpoint status from 200 to 201, run its test,
identify the mismatch, restore 200, and rerun the test.

### Implementation

The separate project in `Task5_Diagnose_Defect/student_system/` has a
health test expecting HTTP 200. Changing the view to return 201 produced
`AssertionError: 201 != 200`. The view was restored to status 200, and
the test passed.

### Code Location

-   [Health endpoint
    view](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task5_Diagnose_Defect/student_system/students/views.py)
-   [Defect diagnosis
    test](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task5_Diagnose_Defect/student_system/students/tests.py)
-   [URL
    configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/Task5_Diagnose_Defect/student_system/student_system/urls.py)
-   [Task 5
    folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Lecture29/Task5_Diagnose_Defect)

### Screenshots

![Task 5 health test before the
defect](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/Task5_Diagnose_Defect/screenshots/task5-health-test-before-defect.png)

![Task 5 intentional test
failure](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/Task5_Diagnose_Defect/screenshots/task5-intentional-test-failure.png)

![Task 5 test passed after the
fix](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/Task5_Diagnose_Defect/screenshots/task5-test-passed-after-fix.png)

### Result

The test detected the incorrect status code. After restoring HTTP 200,
the health endpoint test passed.

## Task 6: PBL Activity, Student API Testing and Debugging

### Task Given

Write tests for health, student list, and student detail endpoints. Test
the `Student` model, mock external service success and timeout cases,
and diagnose an intentionally introduced defect.

### Implementation

The PBL activity is a separate Django project in `PBL_Activity/`. It
includes:

-   A `Student` model with `name`, unique `email`, and `age` fields.
-   A health endpoint returning JSON status `ok` with HTTP 200.
-   A student list endpoint returning student records as JSON.
-   A student detail endpoint returning one student's data or HTTP 404
    for an unknown ID.
-   A `fetch_external_data(url)` utility with timeout handling.
-   Tests for health, list, detail, missing student, model string
    representation, external service success, and external service
    timeout.
-   An intentional defect where status 201 caused
    `AssertionError: 201 != 200`; restoring status 200 made the health
    test pass.

The full PBL test run reported seven tests and `OK`. Django created and
destroyed an in memory test database for the run.

### Code Location

-   [Student
    model](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/PBL_Activity/students/models.py)
-   [Student API
    views](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/PBL_Activity/students/views.py)
-   [URL
    configuration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/PBL_Activity/student_system/urls.py)
-   [Automated
    tests](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/PBL_Activity/students/tests.py)
-   [Mocked external service
    utility](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/PBL_Activity/students/utils.py)
-   [Django
    settings](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/PBL_Activity/student_system/settings.py)
-   [Initial Student
    migration](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit3/Lecture29/PBL_Activity/students/migrations/0001_initial.py)
-   [Complete PBL Activity
    folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Lecture29/PBL_Activity)

### Screenshots

![PBL Student model
implementation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/PBL_Activity/screenshots/pbl-student-model.png)

![PBL intentional defect
failure](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/PBL_Activity/screenshots/pbl-intentional-defect-failure.png)

![PBL health test passed after fixing the
defect](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/PBL_Activity/screenshots/pbl-defect-fixed-test-passed.png)

![PBL complete test suite with seven passing
tests](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit3/Lecture29/PBL_Activity/screenshots/pbl-all-tests-passed.png)

### Result

All seven PBL tests passed after the defect was fixed. The tests verify
endpoint behavior, the missing student case, model behavior, and mocked
external service success and timeout outcomes.

## Project Structure

``` text
Theory/
└── Unit3/
    └── Lecture29/
        ├── Task1_Test_Health_Endpoint/
        │   ├── screenshots/
        │   │   └── task1-health-endpoint-test.png
        │   └── student_system/
        │       ├── manage.py
        │       ├── student_system/
        │       │   ├── settings.py
        │       │   └── urls.py
        │       └── students/
        │           ├── tests.py
        │           └── views.py
        ├── Task2_Test_Parameterized_Endpoint/
        │   ├── screenshots/
        │   │   └── task2-parameterized-endpoint-test.png
        │   └── student_system/
        │       ├── manage.py
        │       ├── student_system/
        │       │   ├── settings.py
        │       │   └── urls.py
        │       └── students/
        │           ├── tests.py
        │           └── views.py
        ├── Task3_Run_Tests/
        │   └── screenshots/
        │       └── task3-full-test-suite.png
        ├── Task4_Test_Mocked_Service/
        │   ├── screenshots/
        │   │   └── task4-mocked-service-timeout-test.png
        │   └── student_system/
        │       ├── manage.py
        │       ├── student_system/
        │       │   ├── settings.py
        │       │   └── urls.py
        │       └── students/
        │           ├── tests.py
        │           ├── utils.py
        │           └── views.py
        ├── Task5_Diagnose_Defect/
        │   ├── screenshots/
        │   │   ├── task5-health-test-before-defect.png
        │   │   ├── task5-intentional-test-failure.png
        │   │   └── task5-test-passed-after-fix.png
        │   └── student_system/
        │       ├── manage.py
        │       ├── student_system/
        │       │   ├── settings.py
        │       │   └── urls.py
        │       └── students/
        │           ├── tests.py
        │           └── views.py
        └── PBL_Activity/
            ├── manage.py
            ├── screenshots/
            │   ├── pbl-student-model.png
            │   ├── pbl-intentional-defect-failure.png
            │   ├── pbl-defect-fixed-test-passed.png
            │   └── pbl-all-tests-passed.png
            ├── student_system/
            │   ├── settings.py
            │   └── urls.py
            └── students/
                ├── migrations/
                │   └── 0001_initial.py
                ├── models.py
                ├── tests.py
                ├── utils.py
                └── views.py
```

## Concepts Used

-   Django `TestCase` and test client
-   Named URL resolution with `reverse()`
-   HTTP status assertions and JSON response verification
-   Parameterized URL patterns
-   Django models and migrations
-   Isolated temporary test databases
-   Mocking with `unittest.mock.patch`
-   External service success and timeout handling
-   Regression testing
-   Interpreting assertion failures and tracebacks
-   Defect diagnosis and verification after a fix

## Overall Result

The Lecture 29 task projects and PBL Activity were committed to the
`main` branch of the Backend Development repository. The PBL Student API
includes three endpoints and a Student model. Its seven automated tests
passed after the intentional defect was corrected. Screenshots are
stored in their corresponding task folders.

## Observations

1.  Using `reverse()` keeps tests independent of hard coded URL paths.
2.  Django's test database isolates test records from the development
    database.
3.  Mocking `requests.get` makes external service tests deterministic
    and independent of live network availability.
4.  Changing the health response from HTTP 200 to 201 produced the
    observed assertion failure `201 != 200`, demonstrating regression
    detection.
5.  All seven PBL tests passed after the health endpoint was restored to
    HTTP 200.
6.  Task 3 contains test run evidence rather than a separate Django
    project; it is not represented as an independent application.
7.  The task folders use separate Django projects, so their tests are
    not claimed to have run as one combined suite.

## Conclusion

This practical demonstrated how automated tests verify Django endpoint
behavior, model behavior, and error handling. Mock based service tests
isolated external dependencies, while the intentional defect exercise
showed how assertion failures help locate regressions. The successful
seven test PBL run confirmed the implemented Student API behavior after
the defect was corrected.

## Experiment Link

No GitHub Pages deployment URL for Lecture 29 is evidenced in the
project. The source code and evidence are available at:

-   [Lecture 29 source folder on
    GitHub](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Lecture29)
-   [PBL Activity source folder on
    GitHub](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit3/Lecture29/PBL_Activity)
-   [Backend Development
    repository](https://github.com/sehajvohra/BackendDevelopment)
