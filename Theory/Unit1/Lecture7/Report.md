# Lecture 7

## Title
Web Storage API: localStorage, sessionStorage, and JSON

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
To understand browser side Web Storage, compare localStorage and sessionStorage, serialize and parse JSON data, inspect stored values using browser developer tools, and implement a notes application with localStorage persistence.

## Software Requirements
- Web browser with JavaScript support
- Browser Developer Tools
- Text editor or IDE
- HTML, CSS, and JavaScript

## Problem Statement
Explore the Web Storage API and JSON serialization in browser based exercises. Practice saving, retrieving, removing, and inspecting values in localStorage and sessionStorage; convert JavaScript objects to JSON strings and back; and implement a Notes App that supports basic note management with localStorage persistence.

## Task Summary

| Task | Description | Implementation |
|---|---|---|
| Task1: localStorage Basics | Practice saving, retrieving, and clearing key value data with the browser localStorage API. | The page introduces localStorage and directs the user to test the API through the browser DevTools Console. The included screenshots document stored data and clearing storage. |
| Task2: sessionStorage Basics | Explore sessionStorage and observe its tab scoped lifetime. | The page introduces sessionStorage and directs the user to test it in the DevTools Console. The screenshots document set/get behavior and the tab closing exercise. |
| Task3: The JSON Problem | Observe why a JavaScript object cannot be stored directly as structured data in Web Storage, and use JSON serialization to preserve it. | The page provides a console based exercise for storing objects. The screenshots document the default object string representation and the JSON based fix. |
| Task4: JSON.stringify() Practice | Convert JavaScript values into JSON strings. | The page directs the user to run JSON.stringify() exercises in the console. Screenshots cover basic serialization and different values. |
| Task5: JSON.parse() Practice | Convert JSON strings back into JavaScript values and observe invalid JSON handling. | The page introduces console based JSON.parse() exercises. Screenshots cover parsing an object, a complete serialization round trip, and a parsing error. |
| Task6: JSON Objects Playground | Practice JSON storage with simple objects, nested objects, arrays of objects, and reusable helper functions. | The page introduces JSON object practice in the console. The screenshots document simple and nested objects, arrays of objects, and helper functions. |
| Task7: DevTools Storage Verification | Inspect browser storage using developer tools and verify stored values. | The page directs the user to inspect Local Storage in DevTools. The screenshots show stored entries, editing a value, deleting an entry, and three stored items. |
| Task8: Web Storage Console Practice | Practice common localStorage, sessionStorage, and JSON operations through the browser console. | The page provides a starting point for console exercises. The screenshots document basic localStorage operations, removal, console table output, and JSON round trip behavior. |
| Task9: Notes App | Build a frontend notes application that adds, displays, edits, and deletes notes, validates empty input, and persists notes in localStorage. | The implemented app uses HTML for the input and notes list, CSS for presentation, and JavaScript for storage and CRUD operations. Each note has an id, text, createdAt, and updatedAt. Notes are loaded on page load, empty input is rejected, and users can edit or delete individual notes. |

## Task1: localStorage Basics

### Task Given
Practice saving, retrieving, and clearing key value data with the browser localStorage API.

### Implementation
The page introduces localStorage and directs the user to test the API through the browser DevTools Console. The included screenshots document stored data and clearing storage.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task1/index.html)

### Screenshots
![Task 1 localstorage](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task1/screenshots/task1-localstorage.png)

![Task 1 clear](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task1/screenshots/task1-clear.png)

### Result
The task demonstrates the persistent browser storage API and the effect of clearing stored entries.

## Task2: sessionStorage Basics

### Task Given
Explore sessionStorage and observe its tab scoped lifetime.

### Implementation
The page introduces sessionStorage and directs the user to test it in the DevTools Console. The screenshots document set/get behavior and the tab closing exercise.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task2/index.html)

### Screenshots
![Task 2 set get](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task2/screenshots/task2-set-get.png)

![Task 2 tab close](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task2/screenshots/task2-tab-close.png)

### Result
The task demonstrates reading and writing sessionStorage values and examining their lifetime in a tab.

## Task3: The JSON Problem

### Task Given
Observe why a JavaScript object cannot be stored directly as structured data in Web Storage, and use JSON serialization to preserve it.

### Implementation
The page provides a console based exercise for storing objects. The screenshots document the default object string representation and the JSON based fix.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task3/index.html)

### Screenshots
![Task 3 object problem](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task3/screenshots/task3-object-problem.png)

![Task 3 json fix](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task3/screenshots/task3-json-fix.png)

### Result
The exercise demonstrates that Web Storage stores strings and that JSON.stringify() preserves an object's data in a serializable form.

## Task4: JSON.stringify() Practice

### Task Given
Convert JavaScript values into JSON strings.

### Implementation
The page directs the user to run JSON.stringify() exercises in the console. Screenshots cover basic serialization and different values.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task4/index.html)

### Screenshots
![Task 4 stringify basic](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task4/screenshots/task4-stringify-basic.png)

![Task 4 stringify values](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task4/screenshots/task4-stringify-values.png)

### Result
The task demonstrates serialization of JavaScript values into JSON strings.

## Task5: JSON.parse() Practice

### Task Given
Convert JSON strings back into JavaScript values and observe invalid JSON handling.

### Implementation
The page introduces console based JSON.parse() exercises. Screenshots cover parsing an object, a complete serialization round trip, and a parsing error.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task5/index.html)

### Screenshots
![Task 5 parse object](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task5/screenshots/task5-parse-object.png)

![Task 5 round trip](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task5/screenshots/task5-round-trip.png)

![Task 5 parse error](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task5/screenshots/task5-parse-error.png)

### Result
The exercise demonstrates parsing valid JSON, restoring data types and structures, and the error caused by invalid JSON.

## Task6: JSON Objects Playground

### Task Given
Practice JSON storage with simple objects, nested objects, arrays of objects, and reusable helper functions.

### Implementation
The page introduces JSON object practice in the console. The screenshots document simple and nested objects, arrays of objects, and helper functions.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task6/index.html)

### Screenshots
![Task 6 simple object](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task6/screenshots/task6-simple-object.png)

![Task 6 nested object](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task6/screenshots/task6-nested-object.png)

![Task 6 array objects](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task6/screenshots/task6-array-objects.png)

![Task 6 helper functions](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task6/screenshots/task6-helper-functions.png)

### Result
The task demonstrates serializing and parsing different JSON data structures and using helper functions for storage.

## Task7: DevTools Storage Verification

### Task Given
Inspect browser storage using developer tools and verify stored values.

### Implementation
The page directs the user to inspect Local Storage in DevTools. The screenshots show stored entries, editing a value, deleting an entry, and three stored items.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task7/index.html)

### Screenshots
![Task 7 devtools storage](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task7/screenshots/task7-devtools-storage.png)

![Task 7 devtools edit](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task7/screenshots/task7-devtools-edit.png)

![Task 7 devtools delete](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task7/screenshots/task7-devtools-delete.png)

![Task 7 three items](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task7/screenshots/task7-three-items.png)

### Result
The task demonstrates that stored browser data can be inspected, edited, and deleted through developer tools.

## Task8: Web Storage Console Practice

### Task Given
Practice common localStorage, sessionStorage, and JSON operations through the browser console.

### Implementation
The page provides a starting point for console exercises. The screenshots document basic localStorage operations, removal, console table output, and JSON round trip behavior.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task8/index.html)

### Screenshots
![Task 8 localstorage basic](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task8/screenshots/task8-localstorage-basic.png)

![Task 8 remove item](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task8/screenshots/task8-remove-item.png)

![Task 8 console table](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task8/screenshots/task8-console-table.png)

![Task 8 json round trip](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task8/screenshots/task8-json-round-trip.png)

### Result
The task consolidates common Web Storage and JSON operations using the browser console.

## Task9: Notes App

### Task Given
Build a frontend notes application that adds, displays, edits, and deletes notes, validates empty input, and persists notes in localStorage.

### Implementation
The implemented app uses HTML for the input and notes list, CSS for presentation, and JavaScript for storage and CRUD operations. Each note has an id, text, createdAt, and updatedAt. Notes are loaded on page load, empty input is rejected, and users can edit or delete individual notes.

### Code Location
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task9/index.html)
- [script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task9/script.js)
- [style.css](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Unit1/Lecture7/Task9/style.css)

### Screenshots
![Task 9 add note](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-add-note.png)

![Task 9 edit note](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-edit-note.png)

![Task 9 delete note](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-delete-note.png)

![Task 9 empty validation](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-empty-validation.png)

![Task 9 persistence](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-persistence.png)

![Task 9 delete persistence](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-delete-persistence.png)

![Task 9 localstorage](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-localstorage.png)

![Task 9 update storage](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-update-storage.png)

![Task 9 console table](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Unit1/Lecture7/Task9/screenshots/task9-console-table.png)

### Result
The implemented Notes App supports adding, displaying, editing, and deleting notes. It rejects empty note text and saves changes in localStorage so they remain available after refresh.

## Project Structure

```text
Lecture7/
├── Task1/
│   ├── index.html
│   └── screenshots/
├── Task2/
│   ├── index.html
│   └── screenshots/
├── Task3/
│   ├── index.html
│   └── screenshots/
├── Task4/
│   ├── index.html
│   └── screenshots/
├── Task5/
│   ├── index.html
│   └── screenshots/
├── Task6/
│   ├── index.html
│   └── screenshots/
├── Task7/
│   ├── index.html
│   └── screenshots/
├── Task8/
│   ├── index.html
│   └── screenshots/
└── Task9/
    ├── index.html
    ├── script.js
    ├── style.css
    └── screenshots/
```

## Concepts Used
- Browser Web Storage API
- localStorage key value operations
- sessionStorage and tab scoped storage
- String only storage behavior
- JSON.stringify() serialization
- JSON.parse() deserialization
- Handling invalid JSON and missing values
- Browser Developer Tools for storage inspection
- JavaScript arrays and objects
- CRUD operations for notes
- DOM manipulation and event listeners
- Input validation
- Timestamps using Date
- Persistent client side data

## Overall Result
The lecture exercises cover browser storage operations, JSON serialization and parsing, developer tools verification, and a working frontend Notes App. The Notes App implements add, display, edit, and delete operations with localStorage persistence.

## Observations
- localStorage data remains available across page refreshes until it is removed or cleared, subject to browser storage policies.
- sessionStorage is scoped to a browser tab session.
- Web Storage values are strings, so structured objects require JSON serialization.
- JSON.parse() expects valid JSON and can throw an error for malformed input.
- Developer Tools can be used to inspect and modify browser storage during testing.
- The Notes App stores note records as a JSON array under the `notes` key.
- The Notes App validates empty input and updates `updatedAt` when an existing note is edited.
- The provided implementation is frontend only; it does not connect to a backend API or database.

## Conclusion
The practical exercises demonstrate the basic behavior of browser Web Storage and the role of JSON in preserving structured JavaScript data. The Notes App applies these concepts to implement note creation, display, editing, deletion, input validation, and persistence using localStorage.

## Experiment Link
The supplied material does not establish a published GitHub Pages URL for this lecture, so no live experiment URL is listed.

## Complete Source Code
[Lecture 7 source folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Unit1/Lecture7)

**Path note:** The GitHub links above use `Theory/Unit1/Lecture7/` as the repository location inferred from the lecture folder supplied. Confirm this folder path against the repository before submission if your repository stores Lecture 7 elsewhere.