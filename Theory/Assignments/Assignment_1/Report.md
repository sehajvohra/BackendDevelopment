# Assignment 1

## Web Storage API Tutorial and Notes App

**Name:** Sehaj Vohra

**SAP ID:** 590011624

**Course:** Backend Development

**Program:** B.Tech Computer Science and Engineering

**Semester:** 5

---

# Part A: Web Storage API Concepts

## 1. What is Web Storage?

Web Storage is a browser API that allows JavaScript applications to store key value pairs on the client side.

The two main types of Web Storage are:

* `localStorage`
* `sessionStorage`

### localStorage

`localStorage` stores data in the browser and keeps the data available after refreshing the webpage and reopening the browser tab.

Common methods include:

```javascript
localStorage.setItem(key, value);
localStorage.getItem(key);
localStorage.removeItem(key);
localStorage.clear();
```

### sessionStorage

`sessionStorage` provides a similar API, but the stored data is associated with the current browser tab or session.

Both storage mechanisms store values as strings.

---

## 2. The JSON Problem

Web Storage stores values as strings. JavaScript objects cannot be directly stored while preserving their object structure.

For example:

```javascript
const user = {
    name: "Alice",
    age: 25
};
```

To store the object, it must first be converted into a JSON string.

```javascript
JSON.stringify(user);
```

When the data is retrieved, `JSON.parse()` can convert the JSON string back into a JavaScript object.

```javascript
JSON.parse(data);
```

This allows JavaScript applications to store arrays and objects using Web Storage.

---

## 3. JSON.stringify()

`JSON.stringify()` converts a JavaScript value into a JSON string.

Example:

```javascript
const user = {
    name: "Alice",
    age: 25
};

const data = JSON.stringify(user);
```

The resulting value can be stored using:

```javascript
localStorage.setItem("user", data);
```

In the Notes App, `JSON.stringify()` is used to convert the complete notes array into a string before storing it.

---

## 4. JSON.parse()

`JSON.parse()` converts a JSON string back into a JavaScript value.

Example:

```javascript
const data = localStorage.getItem("user");

const user = JSON.parse(data);
```

In the Notes App, `JSON.parse()` is used when retrieving the stored notes array from Local Storage.

---

## 5. localStorage and JSON Round Trip

The Notes App follows the following storage process:

```text
JavaScript Notes Array
        ↓
JSON.stringify()
        ↓
localStorage
        ↓
JSON.parse()
        ↓
JavaScript Notes Array
```

The application therefore uses JSON conversion whenever the notes array is saved or retrieved.

---

# Part B: Hands On Exercise: Notes App

## Task 1: Create the Notes App Interface

### Task Given

Create a frontend Notes App using HTML, CSS, and JavaScript.

The interface should allow the user to enter a note and manage the notes stored by the application.

### Implementation

The project contains an HTML page with:

* Notes App heading
* Text input field
* Add Note button
* Notes display area

CSS is used to create the layout and appearance of the application.

### Code Location

[index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/index.html)

[style.css](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/style.css)

### Screenshot

![Notes App](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment_1/screenshots/assignment1-notes-app.png)

### Result

The Notes App interface was successfully created and displayed in the browser.

---

## Task 2: Store Notes Using localStorage

### Task Given

Use the Web Storage API to store notes in the browser and preserve the stored information after refreshing the webpage.

### Implementation

The application uses the `notes` key in `localStorage`.

The `getNotes()` function retrieves the stored value and converts it from JSON into a JavaScript array.

The `saveNotes()` function converts the notes array into JSON and stores it using `localStorage`.

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/script.js)

### Screenshot

![localStorage Verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment_1/screenshots/assignment1-localstorage.png)

### Result

The `notes` key was successfully created in Local Storage and the stored notes were visible through Chrome Developer Tools.

---

## Task 3: Add Notes

### Task Given

Allow the user to enter a note and add it to the Notes App.

Each note should contain information about the note itself and its creation and update status.

### Implementation

The `addNoteFromInput()` function reads the text entered by the user.

Empty input is rejected.

A note object is created with the following properties:

```text
id
text
completed
createdAt
updatedAt
```

The new note is added to the notes array and the updated array is stored in Local Storage.

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/script.js)

### Screenshot

![Added Notes](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment_1/screenshots/assignment1-notes-app.png)

### Result

Multiple notes were successfully added and displayed in the application with their creation timestamps.

---

## Task 4: Display Saved Notes

### Task Given

Retrieve previously stored notes and display them in the application.

### Implementation

The `renderNotes()` function retrieves the notes using `getNotes()`.

The function generates the required HTML for each stored note and displays it inside the `notesList` container.

The application calls `renderNotes()` when the webpage loads.

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/script.js)

[index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/index.html)

### Screenshot

![Displayed Notes](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment_1/screenshots/assignment1-notes-app.png)

### Result

The stored notes were successfully retrieved and displayed on the webpage.

The notes remained available after refreshing the webpage.

---

## Task 5: Edit Notes

### Task Given

Allow the user to modify an existing note.

### Implementation

The `editNote()` function searches for a note using its ID.

The existing note text is displayed through a prompt and can be replaced with new text.

After editing, the `text` property is updated and the `updatedAt` property is set to the current date and time.

The modified notes array is then saved again to Local Storage.

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/script.js)

### Screenshot

![Edited Note](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment_1/screenshots/assignment1-notes-app.png)

### Result

The first note was successfully edited from `Learn Web Storage` to `Learn Web Storage API`.

The updated timestamp was displayed below the creation timestamp.

---

## Task 6: Delete Notes

### Task Given

Allow the user to delete an individual note.

### Implementation

The `deleteNote()` function receives the ID of the selected note.

The `filter()` method creates a new array without the selected note.

The updated array is saved to Local Storage and the application display is refreshed.

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/script.js)

### Screenshot

![Notes App](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment_1/screenshots/assignment1-notes-app.png)

### Result

Individual notes were successfully deleted from the application.

The deleted notes were also removed from the stored notes array.

---

## Task 7: Mark Notes Complete or Incomplete

### Task Given

Allow the user to change the completion status of a note.

### Implementation

The `toggleComplete()` function locates the selected note using its ID.

The value of the `completed` property is changed between `true` and `false`.

When a note is completed, the `completed` CSS class applies a strikethrough effect to the note text.

The updated state is stored in Local Storage.

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/script.js)

[style.css](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/style.css)

### Screenshot

![Mark Complete](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment_1/screenshots/assignment1-mark-complete.png)

### Result

The second note was successfully marked as complete.

The note displayed a strikethrough effect and the button changed to `Mark Incomplete`.

The completed state remained after refreshing the webpage.

---

## Task 8: Verify Persistent Browser Storage

### Task Given

Use browser Developer Tools to verify that the Notes App data is stored using the Web Storage API.

### Implementation

Chrome Developer Tools were opened and the Application tab was selected.

Under Local Storage, the application origin was selected.

The `notes` key was visible in the storage table.

The stored value contained the JSON representation of the notes array.

The stored objects contained:

```text
id
text
completed
createdAt
updatedAt
```

### Code Location

[script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment_1/script.js)

### Screenshot

![localStorage Verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment_1/screenshots/assignment1-localstorage.png)

### Result

The `notes` key was successfully verified in Local Storage using Chrome Developer Tools.

The stored JSON contained the notes and their associated properties.

---

# Project Structure

```text
Theory
└── Assignments
    ├── Assignment_1
    │   ├── screenshots
    │   │   ├── assignment1-localstorage.png
    │   │   ├── assignment1-mark-complete.png
    │   │   └── assignment1-notes-app.png
    │   ├── index.html
    │   ├── Report.md
    │   ├── script.js
    │   └── style.css
    │
    └── Assignment_2
```

# Concepts Used

* Web Storage API
* `localStorage`
* `sessionStorage`
* `setItem()`
* `getItem()`
* `removeItem()`
* `clear()`
* `JSON.stringify()`
* `JSON.parse()`
* JavaScript objects
* JavaScript arrays
* CRUD operations
* DOM manipulation
* Event handling
* Browser based persistent storage
* Date and time handling
* Chrome Developer Tools
* Local Storage inspection

# Overall Result

The Web Storage API assignment was successfully implemented as a functional Notes App using HTML, CSS, and JavaScript.

The application successfully supports adding notes, displaying saved notes, editing notes, deleting notes, and changing the completion status of notes.

The application stores the notes array in Local Storage using JSON conversion and successfully preserves the stored information after refreshing the webpage.

The stored data was also verified through Chrome Developer Tools.

# Observations

1. `localStorage` stores information using key value pairs.
2. Web Storage values are stored as strings.
3. `JSON.stringify()` is used before storing JavaScript objects or arrays.
4. `JSON.parse()` is used after retrieving JSON data from Local Storage.
5. The Notes App stores all notes under the `notes` key.
6. Each note contains an ID, text, completion status, creation time, and update time.
7. Editing a note updates its text and update timestamp.
8. Completing a note changes its completion state.
9. Deleting a note removes it from the stored notes array.
10. The stored notes remain available after refreshing the webpage.
11. Chrome Developer Tools can be used to inspect the stored Local Storage data.
12. The implementation demonstrates client side persistent data storage without a database.

# Conclusion

The Web Storage API was successfully studied and implemented through a functional Notes App.

The practical demonstrated the use of `localStorage` for persistent browser storage and showed how JSON conversion allows structured JavaScript data to be stored and retrieved.

The application successfully implemented note creation, retrieval, editing, deletion, completion status, timestamp management, and persistent storage.

The Local Storage data was verified using Chrome Developer Tools, confirming the successful implementation of the Web Storage API.

# Experiment Link

## GitHub Pages

[Open Assignment 1 Notes App](https://sehajvohra.github.io/BackendDevelopment/Theory/Assignments/Assignment_1/)

## GitHub Source Code

[Open Assignment 1 Folder](https://github.com/sehajvohra/BackendDevelopment/tree/main/Theory/Assignments/Assignment_1)
