# Experiment 5

## Title

Programs to Demonstrate JavaScript Arrays, Objects and Functions

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

To demonstrate the use of JavaScript arrays, objects and functions through basic programs, execute JavaScript using Node JS, integrate JavaScript with HTML, and implement a simple library management utility using arrays, objects and functions.

## Software Requirements

1. Visual Studio Code
2. JavaScript
3. Node JS
4. Web Browser
5. Live Server

## Problem Statement

The experiment requires demonstration of JavaScript arrays, objects and functions. The implementation also includes string, array and object manipulation, HTML integration, Node JS execution, and a practical library management activity using an array of book objects.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task 1 | Basic JavaScript | Arrays, objects and functions |
| Task 2 | Advanced JavaScript Methods | String, array and object manipulation |
| Task 3 | HTML Integration | JavaScript integrated with an HTML page |
| Task 4 | Node JS Execution | JavaScript files executed using Node JS |
| PBL Activity | Library Management | Books stored as objects and searched using functions |

## Task 1: Basic JavaScript

### Task Given

Create a JavaScript program to demonstrate arrays, objects and functions.

### Implementation

The implementation creates an array containing three fruits and adds another fruit using the `push()` method.

A student object is created containing the name, age and course of Sehaj Vohra. The object properties are accessed using dot notation.

A `greet()` function is created and called with the student name to display a greeting message.

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%205/Task1_Basic_JavaScript/script.js)

### Screenshot

![Task 1 Node JS output](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%205/screenshots/task1-node-output.png)

### Result

The program successfully demonstrated array creation, adding an array element, object creation, accessing object properties and function execution. The terminal output shows the expected results for all three concepts.

## Task 2: Advanced JavaScript Methods

### Task Given

Create a JavaScript program to demonstrate string, array and object manipulation methods.

### Implementation

The implementation uses string methods to convert text into uppercase and lowercase and to split a string into separate words.

An array containing JavaScript and Node JS is created. MongoDB is added to the array, an element is accessed using its index, and the first element is updated.

A student object is created with name and course properties. A semester property is added, the student name is accessed, and the course property is updated.

### Code Location

[script2.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%205/Task2_Advanced_JavaScript/script2.js)

### Screenshot

![Task 2 Advanced JavaScript output](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%205/screenshots/task2-advanced-output.png)

### Result

The program successfully demonstrated string conversion, string splitting, array insertion, array access, array updating, object property insertion, object property access and object property updating.

## Task 3: HTML Integration

### Task Given

Create an HTML page to load and execute the JavaScript program in a browser.

### Implementation

An HTML page named `index.html` was created with a heading and a paragraph instructing the user to open the browser console.

The JavaScript file from Task 1 is loaded using the `script` element. The page was executed in a browser and the JavaScript output was viewed through the browser console.

### Code Location

[index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%205/Task3_HTML_Integration/index.html)

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%205/Task1_Basic_JavaScript/script.js)

### Screenshot

![Task 3 HTML integration and browser console](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%205/screenshots/task3-html-console.png)

### Result

The HTML page was successfully opened in the browser and the JavaScript output was displayed in the browser console.

## Task 4: Node JS Execution

### Task Given

Execute the JavaScript programs using Node JS through the terminal.

### Implementation

The Task 1 JavaScript program was executed from the Task 4 terminal using Node JS.

The Task 2 JavaScript program was also executed using Node JS.

No separate source file was created for Task 4. The task uses the JavaScript files implemented in Task 1 and Task 2.

### Code Location

[Task 1 JavaScript file](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%205/Task1_Basic_JavaScript/script.js)

[Task 2 JavaScript file](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%205/Task2_Advanced_JavaScript/script2.js)

[Task 4 folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%205/Task4_Node_Execution)

### Screenshot

![Task 4 Node JS execution](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%205/screenshots/task4-node-execution.png)

### Result

The JavaScript program from Task 1 was successfully executed using Node JS from the Task 4 terminal. The terminal displayed the array, object and function output successfully.

## PBL Activity: Library Management

### Task Given

Create a simple library management utility using an array of books and functions to add and search for books.

### Implementation

An empty `library` array is created to store book objects.

The `addBook()` function creates a book object containing a title and author and adds it to the library.

The `findBook()` function searches the library by comparing the requested title with the title of each stored book.

Three books are added to the library:

1. The Alchemist by Paulo Coelho
2. Wings of Fire by A. P. J. Abdul Kalam
3. Clean Code by Robert Martin

The program searches for `Wings of Fire` and displays the matching book details.

The program also searches for `Harry Potter`, which is not present in the library, and displays `Book not found`.

### Code Location

[library.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%205/PBL_Library/library.js)

### Screenshot

![PBL library management output](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%205/screenshots/pbl-library-output.png)

### Result

The library management program successfully stored three book objects in an array.

The search operation successfully returned the details of `Wings of Fire`.

The search for `Harry Potter` correctly returned no matching book and displayed `Book not found`.

## Project Structure

```text
Exp 5
│
├── PBL_Library
│   └── library.js
│
├── Task1_Basic_JavaScript
│   └── script.js
│
├── Task2_Advanced_JavaScript
│   └── script2.js
│
├── Task3_HTML_Integration
│   └── index.html
│
├── Task4_Node_Execution
│
├── screenshots
│   ├── pbl-library-output.png
│   ├── task1-node-output.png
│   ├── task2-advanced-output.png
│   ├── task3-html-console.png
│   └── task4-node-execution.png
│
└── Report.md
```

## Concepts Used

1. JavaScript arrays
2. JavaScript objects
3. JavaScript functions
4. Array `push()` method
5. Array indexing
6. Object property access
7. Object property insertion
8. Object property updating
9. String `toUpperCase()` method
10. String `toLowerCase()` method
11. String `split()` method
12. JavaScript `for` loop
13. Conditional statements
14. Node JS execution
15. HTML and JavaScript integration
16. Browser console
17. Array of objects
18. Searching objects using a function

## Overall Result

The experiment was successfully implemented using JavaScript arrays, objects and functions.

The practical work demonstrated basic data manipulation, string methods, array operations, object operations, browser integration and Node JS execution.

The PBL activity successfully implemented a simple library management utility using an array of book objects and functions for adding and searching books.

## Observations

1. Arrays can store multiple values and can be modified during program execution.
2. Objects store related information using properties and values.
3. Functions allow reusable program logic to be defined and executed when required.
4. String methods can be used to transform and divide text.
5. Array elements can be added, accessed and updated using JavaScript operations.
6. Object properties can be added, accessed and updated during program execution.
7. JavaScript programs can be executed directly using Node JS.
8. JavaScript can be connected to an HTML page using the `script` element.
9. An array of objects can be used for simple in memory data management.
10. A search function can return an object when a matching property value is found.

## Conclusion

The experiment successfully demonstrated the practical use of JavaScript arrays, objects and functions.

The implemented tasks provided experience with data manipulation, string methods, array operations, object properties, HTML integration and Node JS execution.

The library management activity further demonstrated how arrays, objects, functions and search logic can be combined to implement a simple data management utility.

## Experiment Link

[Experiment 5 GitHub Pages Report](https://sehajvohra.github.io/BackendDevelopment/Lab/Exp%205/Report.html)

## GitHub Source Code

[Complete Experiment 5 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%205)
