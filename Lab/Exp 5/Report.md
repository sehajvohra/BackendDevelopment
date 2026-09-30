# Lab Experiment 05

## Programs to Demonstrate JavaScript Arrays, Objects and Functions

## Aim

To demonstrate the use of JavaScript arrays, objects and functions and to perform basic data manipulation using JavaScript.

## Objectives

1. To create and manipulate arrays in JavaScript.
2. To create and access objects using properties.
3. To define and use functions.
4. To demonstrate string manipulation methods.
5. To demonstrate array and object manipulation.
6. To execute JavaScript programs using Node JS.
7. To integrate JavaScript with an HTML page.
8. To create a simple library management program using arrays, objects and functions.

## Software and Tools Used

1. Visual Studio Code
2. JavaScript
3. Node JS
4. Web Browser
5. Live Server

## Task 1: Basic JavaScript

### Description

A JavaScript program was created to demonstrate arrays, objects and functions.

An array containing fruit names was created and a new fruit was added using the `push()` method.

A student object containing name, age and course was created. Object properties were accessed using dot notation.

A `greet()` function was created to display a greeting message.

### File Used

`script.js`

### Implementation

```javascript
const fruits = ["Apple", "Banana", "Mango"];

console.log("Array Demonstration");
console.log("Fruits:", fruits);

fruits.push("Orange");

console.log("After adding Orange:", fruits);

const student = {
    name: "Sehaj Vohra",
    age: 20,
    course: "Backend Development"
};

console.log("\nObject Demonstration");
console.log("Student:", student);
console.log("Name:", student.name);
console.log("Course:", student.course);

function greet(name) {
    return "Hello " + name + ", welcome to Backend Development Lab.";
}

console.log("\nFunction Demonstration");
console.log(greet("Sehaj Vohra"));
```

### Result

The program successfully demonstrated array creation, array insertion, object creation, property access and function execution.

### Evidence

`task1-node-output`

## Task 2: Advanced JavaScript Methods

### Description

A JavaScript program was created to demonstrate string, array and object manipulation.

String methods were used to convert text into uppercase and lowercase and to split a string into separate words.

Array methods were used to add, read and update elements.

Object properties were added, read and updated.

### File Used

`script2.js`

### Implementation

```javascript
const course = "Backend Development";

console.log("String Demonstration");
console.log("Original:", course);
console.log("Upper Case:", course.toUpperCase());
console.log("Lower Case:", course.toLowerCase());

const parts = course.split(" ");
console.log("Words:", parts);

let subjects = ["JavaScript", "Node.js"];

console.log("\nArray Demonstration");
console.log("Original:", subjects);

subjects.push("MongoDB");
console.log("After adding:", subjects);

console.log("First subject:", subjects[0]);

subjects[0] = "Express";
console.log("After updating:", subjects);

let student = {
    name: "Sehaj Vohra",
    course: "B.Tech CSE"
};

console.log("\nObject Demonstration");
console.log("Original:", student);

student.semester = 5;
console.log("After adding semester:", student);

console.log("Student name:", student.name);

student.course = "Computer Science";
console.log("After updating course:", student);
```

### Result

The program successfully demonstrated string manipulation, array insertion, array access, array updating, object property insertion, object property access and object property updating.

### Evidence

`task2-advanced-output`

## Task 3: HTML Integration

### Description

An HTML page was created to integrate the JavaScript program with a web page.

The JavaScript file was connected to the HTML page using the `script` element.

The output was checked through the browser console.

### File Used

`index.html`

### Implementation

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Exp 5 JavaScript Demo</title>
</head>
<body>

    <h1>Exp 5 JavaScript Demo</h1>

    <p>Open the browser console to see the output.</p>

    <script src="../Task1_Basic_JavaScript/script.js"></script>

</body>
</html>
```

### Result

The HTML page successfully loaded the JavaScript program and the output was visible in the browser console.

### Evidence

`task3-html-console`

## Task 4: Node JS Execution

### Description

The JavaScript programs created in the earlier tasks were executed using Node JS through the terminal.

The first program was executed using:

```bash
node ../Task1_Basic_JavaScript/script.js
```

The second program was executed using:

```bash
node ../Task2_Advanced_JavaScript/script2.js
```

### Result

Both JavaScript programs executed successfully through the terminal and produced the expected output.

### Evidence

`task4-node-execution`

## PBL Activity: Library Management

### Problem Statement

A simple library management utility was created using an array of objects and functions.

The program allows books to be added to a library and searched using their titles.

### File Used

`library.js`

### Implementation

```javascript
const library = [];

function addBook(title, author) {
    const book = {
        title: title,
        author: author
    };

    library.push(book);
    console.log("Book added:", title);
}

function findBook(title) {
    for (let i = 0; i < library.length; i++) {
        if (library[i].title === title) {
            return library[i];
        }
    }

    return null;
}

addBook("The Alchemist", "Paulo Coelho");
addBook("Wings of Fire", "A. P. J. Abdul Kalam");
addBook("Clean Code", "Robert Martin");

console.log("\nLibrary Books:");
console.log(library);

console.log("\nSearching for Wings of Fire:");

const result = findBook("Wings of Fire");

if (result !== null) {
    console.log("Book found:", result);
} else {
    console.log("Book not found");
}

console.log("\nSearching for Harry Potter:");

const secondResult = findBook("Harry Potter");

if (secondResult !== null) {
    console.log("Book found:", secondResult);
} else {
    console.log("Book not found");
}
```

### Working

The `library` array stores the book objects.

The `addBook()` function creates a book object and adds it to the library.

The `findBook()` function checks the title of every book in the library.

When a matching title is found, the corresponding book object is returned.

If no matching title is found, the function returns `null`.

### Result

The program successfully added three books to the library.

The search for `Wings of Fire` successfully returned the book details.

The search for `Harry Potter` correctly displayed that the book was not found.

### Evidence

`pbl-library-output`

## Learning Outcomes

After completing this experiment, the following concepts were demonstrated:

1. JavaScript array creation and manipulation.
2. JavaScript object creation and property access.
3. JavaScript function creation and execution.
4. String manipulation methods.
5. Array manipulation methods.
6. Object property manipulation.
7. JavaScript execution using Node JS.
8. JavaScript integration with HTML.
9. Searching objects stored inside an array.
10. Basic in memory data management.

## Conclusion

The experiment was successfully completed by implementing JavaScript programs using arrays, objects and functions.

The practical work demonstrated basic data manipulation, function based programming, HTML integration and execution using Node JS.

The library activity further demonstrated how arrays and objects can be combined with functions to create a simple data management utility.
