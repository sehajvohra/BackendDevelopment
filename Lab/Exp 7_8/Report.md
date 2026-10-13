# Experiment 7 and 8

## Title

ES6, DOM Manipulation and Event Handling

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

To practise modern JavaScript features introduced in ES6, manipulate HTML elements through the Document Object Model (DOM), handle browser events, and implement a To Do List application with interactive task operations.

## Software Requirements

1. Visual Studio Code
2. Node.js
3. A modern web browser
4. Live Server extension for Visual Studio Code

## Problem Statement

Develop practical examples demonstrating ES6 syntax and features, DOM selection and manipulation, browser event handling, and an interactive To Do List. The report documents the source files and screenshot evidence visible in the project structure. It describes the implementation that is present in the project rather than assuming additional functionality.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| 1 | ES6 variables and arrow functions | JavaScript example using `const`, `let`, an arrow function, and a template literal. |
| 2 | Spread, rest, and default parameters | Example demonstrating array spread, rest parameters, and a default function argument. |
| 3 | Classes and inheritance | `Student` and `CSEStudent` classes demonstrate constructors, methods, inheritance, and `super()`. |
| 4 | ES6 modules | Separate module files export and import student information and a marks calculation function. |
| 5 | Promises and async/await | Asynchronous student details example using a Promise and `async`/`await`. |
| 6 | Enhanced object literals | Object property shorthand and method shorthand are demonstrated with student marks. |
| 7 | DOM selection and manipulation | HTML page changes text and toggles a CSS class using DOM APIs. |
| 8 | Create and insert DOM elements | Student list items are created dynamically and appended to a list. |
| 9 | Remove elements and traverse the DOM | Example uses parent and child element properties and removes list items. |
| 10 | DOM form validation | Student marks form reads input, validates values, and displays a result. |
| 11 | Basic event handling | Mouse click and keyboard events demonstrate the event object. |
| 12 | Form event handling | Form submission is handled with `preventDefault()` and a success message. |
| 13 | Event bubbling | Parent and child click handlers demonstrate bubbling and stopping propagation. |
| 14 | Event delegation | One list listener handles clicks on existing and dynamically added list items. |
| 15 | Event capturing and bubbling | A parent listener is switched between capture and bubble phases to compare handler order. |
| 16 | To Do List | Interactive list supports adding, completing, deleting, counting, and saving tasks in local storage. |

## Task 1: ES6 Variables and Arrow Functions

### Task Given

Demonstrate variable declarations and arrow function syntax in JavaScript.

### Implementation

The `es6_basics.js` file declares a constant student name and a changeable marks variable. It updates the marks, defines an arrow function that greets a student, and displays the results in the console.

### Code Location

[es6_basics.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/01_ES6/es6_basics.js)

### Screenshot

The screenshot filename was not visible in the supplied folder screenshots, so no image link is included for this task.

### Result

The example demonstrates `const`, `let`, reassignment, arrow function syntax, template literals, and console output.

## Task 2: Spread, Rest, and Default Parameters

### Task Given

Demonstrate the spread operator, rest parameters, and default parameter values.

### Implementation

The `spread_rest.js` file expands an array into a larger array, collects function arguments with a rest parameter to calculate a sum, and uses a default name when a function is called without an argument.

### Code Location

[spread_rest.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/01_ES6/spread_rest.js)

### Screenshot

The screenshot filename was not visible in the supplied folder screenshots, so no image link is included for this task.

### Result

The example demonstrates array expansion, collecting multiple arguments, and default function parameters.

## Task 3: Classes and Inheritance

### Task Given

Demonstrate JavaScript classes, constructors, methods, and inheritance.

### Implementation

The `classes_inheritance.js` file defines a `Student` class with student details and a display method. The `CSEStudent` class extends `Student`, calls the parent constructor through `super()`, and adds a branch property and method.

### Code Location

[classes_inheritance.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/01_ES6/classes_inheritance.js)

### Screenshot

The screenshot filename was not visible in the supplied folder screenshots, so no image link is included for this task.

### Result

The example demonstrates object initialization, class methods, inheritance, and reuse of a parent class constructor.

## Task 4: ES6 Modules

### Task Given

Demonstrate how JavaScript functionality can be exported from one file and imported into another.

### Implementation

The `student.js` file exports a student name, a display function, and a marks calculation function. The `modules_demo.js` file imports and calls these exports. The `package.json` file in `01_ES6` specifies `"type": "module"` for Node.js module support.

### Code Location

- [student.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/01_ES6/student.js)
- [modules_demo.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/01_ES6/modules_demo.js)
- [package.json](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/01_ES6/package.json)

### Screenshot

The screenshot filename was not visible in the supplied folder screenshots, so no image link is included for this task.

### Result

The example separates reusable functions and values into a module and imports them into another JavaScript file.

## Task 5: Promises and async/await

### Task Given

Demonstrate asynchronous JavaScript using a Promise and `async`/`await`.

### Implementation

The `promises_async.js` file defines a function that returns a Promise and resolves with student details after a delay. An asynchronous function awaits the Promise and displays the student information inside a `try` block.

### Code Location

[promises_async.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/01_ES6/promises_async.js)

### Screenshot

The screenshot filename was not visible in the supplied folder screenshots, so no image link is included for this task.

### Result

The example demonstrates Promise resolution and the use of `await` to process asynchronous results.

## Task 6: Enhanced Object Literals

### Task Given

Demonstrate property shorthand and method shorthand in JavaScript object literals.

### Implementation

The `object_literals.js` file creates a student object using shorthand properties and a concise method definition. The method displays student details, joins the marks array into a string, and calculates the total using `reduce()`.

### Code Location

[object_literals.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/01_ES6/object_literals.js)

### Screenshot

The screenshot filename was not visible in the supplied folder screenshots, so no image link is included for this task.

### Result

The example demonstrates concise object syntax and array methods for displaying and calculating marks.

## Task 7: DOM Selection and Manipulation

### Task Given

Select HTML elements and modify their text, attributes, and CSS classes through JavaScript.

### Implementation

The `dom_manipulation.html` file uses `getElementById()` and `querySelector()` to select elements. Its buttons change the heading and paragraph text, set a title attribute, and toggle a CSS class.

### Code Location

[dom_manipulation.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/02_DOM_Manipulation/dom_manipulation.html)

### Screenshots

![DOM content and style changes](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/02_DOM_Manipulation/screenshots/dom-selection-content-style.png)

### Result

The page demonstrates changing text, updating an attribute, and toggling a CSS class through DOM operations.

## Task 8: Create and Insert DOM Elements

### Task Given

Create HTML elements dynamically and insert them into the document in response to a user action.

### Implementation

The `dom_create_elements.html` file listens for a button click, creates a new list item using `document.createElement()`, assigns text, and appends it to the student list.

### Code Location

[dom_create_elements.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/02_DOM_Manipulation/dom_create_elements.html)

### Screenshots

![Dynamically created DOM elements](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/02_DOM_Manipulation/screenshots/dom-create-elements.png)

### Result

Each button click adds another student list item to the page.

## Task 9: Remove Elements and Traverse the DOM

### Task Given

Demonstrate DOM traversal and remove an element from a list.

### Implementation

The `dom_remove_traverse.html` file accesses the parent element and the last child element. It uses `remove()` to delete the last student and displays a message when the list is empty.

### Code Location

[dom_remove_traverse.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/02_DOM_Manipulation/dom_remove_traverse.html)

### Screenshots

![DOM removal and traversal](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/02_DOM_Manipulation/screenshots/dom-remove-traverse.png)

### Result

The example demonstrates parent and child traversal and the removal of list elements.

## Task 10: DOM Form Validation

### Task Given

Read form inputs, validate student details, and display a result without reloading the page.

### Implementation

The `dom_form_validation.html` file reads a student name and marks. It uses required fields and numeric limits in HTML, prevents the normal form submission, checks the entered values in JavaScript, and displays the student's score.

### Code Location

[dom_form_validation.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/02_DOM_Manipulation/dom_form_validation.html)

### Screenshots

![Empty form required field validation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/02_DOM_Manipulation/screenshots/dom-form-empty-validation.png)

![Valid student marks result](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/02_DOM_Manipulation/screenshots/dom-form-valid-result.png)

![Invalid marks validation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/02_DOM_Manipulation/screenshots/dom-form-invalid-marks.png)

### Result

The form accepts valid student details and displays the marks result. HTML constraints and JavaScript checks provide validation.

## Task 11: Basic Event Handling

### Task Given

Demonstrate mouse and keyboard events and inspect event object properties.

### Implementation

The `event_basics.html` file attaches a click listener to a button and a `keydown` listener to a text input. It displays the event type, target text, or key pressed.

### Code Location

[event_basics.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/03_Event_Handling/event_basics.html)

### Screenshots

![Basic mouse and keyboard event handling](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-basics.png)

### Result

The page demonstrates click and keyboard events and uses `event.type`, `event.target`, and `event.key`.

## Task 12: Form Event Handling

### Task Given

Handle form submission and prevent the browser from performing its default submission behavior.

### Implementation

The `form_events.html` file listens for the form's `submit` event, calls `event.preventDefault()`, reads the entered student name, and displays a registration success message.

### Code Location

[form_events.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/03_Event_Handling/form_events.html)

### Screenshots

![Form event handling](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/form-events.png)

### Result

A valid name can be submitted and the success message appears without a page refresh.

## Task 13: Event Bubbling and stopPropagation

### Task Given

Demonstrate event bubbling between a child and parent element and show how `stopPropagation()` prevents the event from continuing upward.

### Implementation

The `event_bubbling.html` file registers click handlers on a parent `div` and its child button. A toggle controls whether the child handler calls `event.stopPropagation()`. The screenshots document the child and parent behavior, stopped bubbling, and restored bubbling.

### Code Location

[event_bubbling.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/03_Event_Handling/event_bubbling.html)

### Screenshots

![Child and parent click handlers](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-bubbling-child-parent.png)

![Bubbling stopped](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-bubbling-stopped.png)

![Bubbling restored](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-bubbling-restored.png)

### Result

The example demonstrates that bubbling normally allows a child click event to reach the parent and that `stopPropagation()` prevents this propagation.

## Task 14: Event Delegation

### Task Given

Use a parent element's event listener to handle clicks on both existing and dynamically created child elements.

### Implementation

The `event_delegation.html` file attaches one click listener to the student list. It checks whether the clicked target is an `LI` element and displays the selected student's name. A button adds a new list item, which is also handled by the same listener.

### Code Location

[event_delegation.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/03_Event_Handling/event_delegation.html)

### Screenshots

![First student selected](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-delegation-first-student.png)

![Second student selected](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-delegation-second-student.png)

![Dynamically added student selected](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-delegation-dynamic-student.png)

### Result

A single parent listener handles clicks on the original list items and the dynamically added item.

## Task 15: Event Capturing and Bubbling

### Task Given

Compare event capturing and event bubbling by observing the order in which parent and child click handlers execute.

### Implementation

The `event_capturing.html` file allows the parent click listener to be registered in capturing or bubbling mode. In capturing mode, the parent handler executes before the child handler. In bubbling mode, the child handler executes before the parent handler.

### Code Location

[event_capturing.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/03_Event_Handling/event_capturing.html)

### Screenshots

![Event capturing order](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-capturing-order.png)

![Event bubbling order](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/03_Event_Handling/screenshots/event-bubbling-order.png)

### Result

The experiment demonstrates the difference between the capturing and bubbling phases of event propagation.

## Task 16: To Do List Application

### Task Given

Create an interactive To Do List that allows users to add tasks, mark tasks as completed, delete tasks, view a task count, and retain tasks using browser storage.

### Implementation

The `todo.html` file provides the task input, add button, task count, and list. The `todo.js` file maintains the task array, renders list items, toggles completion, deletes tasks, updates the task count, and stores task data in `localStorage`. Tasks can be added using the button or the Enter key.

### Code Location

- [todo.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/04_ToDo_List/todo.html)
- [todo.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Lab/Exp%207_8/04_ToDo_List/todo.js)
- [To Do List folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%207_8/04_ToDo_List)

### Screenshots

![To Do List styled interface](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/04_ToDo_List/screenshots/todo-styled-interface.png)

![Adding a task](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/04_ToDo_List/screenshots/todo-add-task.png)

![Task marked complete](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/04_ToDo_List/screenshots/todo-complete-task.png)

![Task deletion](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/04_ToDo_List/screenshots/todo-delete-task.png)

![Successful task deletion](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/04_ToDo_List/screenshots/todo-delete-successful.png)

![Task counter](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/04_ToDo_List/screenshots/todo-task-counter.png)

![Task completion toggle](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/04_ToDo_List/screenshots/todo-toggle-completion.png)

![Local storage evidence](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Lab/Exp%207_8/04_ToDo_List/screenshots/todo-local-storage.png)

### Result

The To Do List provides task creation, completion toggling, deletion, task counting, and persistence using `localStorage`.

## Project Structure

```text
Lab/
└── Exp 7_8/
    ├── 01_ES6/
    │   ├── destructuring.js
    │   ├── template_literals.js
    │   ├── es6_basics.js
    │   ├── spread_rest.js
    │   ├── classes_inheritance.js
    │   ├── student.js
    │   ├── modules_demo.js
    │   ├── promises_async.js
    │   ├── object_literals.js
    │   ├── package.json
    │   └── screenshots/
    ├── 02_DOM_Manipulation/
    │   ├── index.html
    │   ├── app.js
    │   ├── dom_manipulation.html
    │   ├── dom_create_elements.html
    │   ├── dom_remove_traverse.html
    │   ├── dom_form_validation.html
    │   └── screenshots/
    ├── 03_Event_Handling/
    │   ├── event_basics.html
    │   ├── form_events.html
    │   ├── event_bubbling.html
    │   ├── event_delegation.html
    │   ├── event_capturing.html
    │   └── screenshots/
    └── 04_ToDo_List/
        ├── todo.html
        ├── todo.js
        └── screenshots/
```

The tree lists the principal files used in this report. The screenshots folder contents are documented in the relevant task sections.

## Concepts Used

- ES6 `let` and `const`
- Arrow functions and template literals
- Spread syntax, rest parameters, and default parameters
- Classes, constructors, methods, inheritance, and `super()`
- ES modules using `export` and `import`
- Promises, `async`/`await`, and delayed asynchronous operations
- Enhanced object literals
- DOM selection using `getElementById()` and `querySelector()`
- DOM text, attributes, classes, element creation, insertion, removal, and traversal
- Form input handling and validation
- Mouse, keyboard, and submit events
- Event objects and properties
- `preventDefault()` and `stopPropagation()`
- Event capturing, bubbling, and delegation
- Arrays, array methods, and dynamic list rendering
- Browser `localStorage` and JSON serialization

## Overall Result

The practical work demonstrates core ES6 language features, DOM manipulation, event handling, and an interactive To Do List. The examples use separate files organized into ES6, DOM Manipulation, Event Handling, and To Do List folders.

## Observations

1. `const` prevents reassignment of a variable binding, while `let` permits reassignment.
2. ES modules require compatible module configuration when executed through Node.js.
3. DOM changes can be performed in response to user events without reloading the page.
4. Event capturing runs from ancestors toward the target, while bubbling runs from the target toward ancestors.
5. Event delegation lets a parent listener handle dynamically added child elements.
6. `preventDefault()` suppresses a browser's default action, while `stopPropagation()` prevents an event from continuing through the propagation path.
7. `localStorage` can preserve task data between page reloads in the same browser.
8. HTML validation attributes and JavaScript checks can be combined to validate user input.

## Conclusion

This experiment provided practical experience with ES6 JavaScript, DOM operations, browser events, and interactive page behavior. The separate examples demonstrate how JavaScript can modify page content, respond to user actions, and manage client side task data.

## Experiment Link

The experiment is organized in the repository under the `Lab/Exp 7_8` folder.

- [Complete experiment source folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Lab/Exp%207_8)
- [GitHub repository](https://github.com/sehajvohra/BackendDevelopment)

A published GitHub Pages URL for this experiment was not confirmed in the provided material, so no live experiment link is listed.
