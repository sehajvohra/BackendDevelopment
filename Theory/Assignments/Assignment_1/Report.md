# Assignment 1

## Title

Web Storage API Tutorial and Notes App

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

The objective of this assignment is to understand and implement the Web Storage API using JavaScript.

The assignment focuses on `localStorage`, `sessionStorage`, JSON conversion using `JSON.stringify()` and `JSON.parse()`, browser Developer Tools, and persistent client side data storage.

A functional Notes App was developed using HTML, CSS, and JavaScript. The application uses `localStorage` to store notes and preserve the data after refreshing the webpage.

## Software Requirements

- Visual Studio Code
- Web Browser such as Google Chrome
- HTML5
- CSS3
- JavaScript
- Web Storage API
- Chrome Developer Tools

## Problem Statement

Study the Web Storage API and understand the working of `localStorage` and `sessionStorage`. Learn how JavaScript objects can be converted into JSON strings for browser storage and converted back into JavaScript objects using `JSON.stringify()` and `JSON.parse()`.

As the final practical implementation, develop a frontend Notes App that uses `localStorage` for persistent storage of notes.

The Notes App should support adding, displaying, editing, deleting, and completing notes while maintaining note information such as ID, text, creation time, and update time.

## Task Summary

| Task | Description | Implementation |
|------|-------------|----------------|
| Task 1 | Create a Notes App interface | Implemented a frontend Notes App using HTML and CSS |
| Task 2 | Store notes using localStorage | Implemented `getNotes()` and `saveNotes()` functions using `localStorage` and JSON |
| Task 3 | Add notes | Implemented note creation with ID, text, completion status, creation time, and update time |
| Task 4 | Display saved notes | Implemented `renderNotes()` to retrieve and display stored notes |
| Task 5 | Edit notes | Implemented editing of existing notes and updated the `updatedAt` value |
| Task 6 | Delete notes | Implemented deletion of individual notes |
| Task 7 | Mark notes complete or incomplete | Implemented completion status using the `completed` property |
| Task 8 | Verify persistent browser storage | Verified the stored `notes` data using Chrome Developer Tools |

## Task 1: Create the Notes App Interface

### Task Given

Create a frontend Notes App using HTML, CSS, and JavaScript that provides an interface for entering and managing notes.

### Implementation

The project contains an HTML interface with a heading, text input field, Add Note button, and a container for displaying saved notes.

CSS is used to provide the layout, spacing, borders, buttons, note cards, and completed note styling.

The interface is implemented using the following project files:

### Code Location

- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/index.html)
- [style.css](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/style.css)

### Screenshot

![Notes App](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment1_Web_Storage/screenshots/assignment1-notes-app.png)

### Result

The Notes App interface was successfully created and displayed in the browser. The interface provides an input field for entering notes and controls for managing the stored notes.

## Task 2: Store Notes Using localStorage

### Task Given

Use the Web Storage API to store application data in the browser. Since Web Storage stores values as strings, JSON conversion should be used for storing JavaScript objects and arrays.

### Implementation

The application uses the `notes` key in `localStorage` to store the notes array.

The `getNotes()` function retrieves the stored JSON string and converts it into a JavaScript array using `JSON.parse()`.

The `saveNotes()` function converts the notes array into a JSON string using `JSON.stringify()` and stores it using `localStorage.setItem()`.

### Code Location

- [script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/script.js)

### Screenshot

![localStorage Verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment1_Web_Storage/screenshots/assignment1-localstorage.png)

### Result

The notes were successfully stored in browser Local Storage under the `notes` key. Chrome Developer Tools confirmed that the notes were stored as JSON data.

## Task 3: Add Notes

### Task Given

Allow the user to enter a note and add it to the application.

Each note should contain an ID, text, completion status, creation time, and update time.

### Implementation

The `addNoteFromInput()` function retrieves the text entered by the user, removes unnecessary whitespace, checks for empty input, creates a note object, adds the note to the notes array, saves the updated array to `localStorage`, and refreshes the displayed notes.

Each created note contains:

- `id`
- `text`
- `completed`
- `createdAt`
- `updatedAt`

### Code Location

- [script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/script.js)

### Screenshot

![Added Notes](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment1_Web_Storage/screenshots/assignment1-notes-app.png)

### Result

Multiple notes were successfully added and displayed in the Notes App. Each note was stored with its corresponding data fields and creation timestamp.

## Task 4: Display Saved Notes

### Task Given

Display all saved notes when the application is opened and after changes are made.

### Implementation

The `renderNotes()` function retrieves the notes using `getNotes()` and generates the required HTML for every stored note.

The application calls `renderNotes()` when the webpage loads using `window.onload`.

The stored notes therefore remain available after refreshing the webpage.

### Code Location

- [script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/script.js)
- [index.html](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/index.html)

### Screenshot

![Displayed Notes](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment1_Web_Storage/screenshots/assignment1-notes-app.png)

### Result

The stored notes were successfully retrieved from `localStorage` and displayed on the webpage. The notes remained available after refreshing the page.

## Task 5: Edit Notes

### Task Given

Allow the user to modify an existing note and save the updated information.

### Implementation

The `editNote()` function searches for the note using its ID.

The existing text is displayed through a prompt and can be replaced with new text.

After editing, the `text` property is updated and the `updatedAt` property is set to the current date and time.

The modified notes array is then saved back to `localStorage`.

### Code Location

- [script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/script.js)

### Screenshot

![Edited Note](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment1_Web_Storage/screenshots/assignment1-notes-app.png)

### Result

The note was successfully edited. The updated text was displayed and the updated timestamp was recorded.

## Task 6: Delete Notes

### Task Given

Allow the user to delete an individual note from the Notes App.

### Implementation

The `deleteNote()` function uses the note ID to identify the selected note.

The `filter()` method creates an updated notes array without the selected note. The updated array is then stored again in `localStorage` and displayed on the webpage.

### Code Location

- [script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/script.js)

### Screenshot

![Notes App](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment1_Web_Storage/screenshots/assignment1-notes-app.png)

### Result

Individual notes were successfully deleted from the application. Deleted notes were removed from the stored notes array and no longer appeared after refreshing the webpage.

## Task 7: Mark Notes Complete or Incomplete

### Task Given

Provide functionality for changing the completion status of a note.

### Implementation

The `toggleComplete()` function locates a note using its ID and changes the value of its `completed` property.

When a note is completed, the CSS class `completed` is applied to its text, resulting in a strikethrough appearance.

The updated completion state is stored in `localStorage`.

### Code Location

- [script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/script.js)
- [style.css](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/style.css)

### Screenshot

![Mark Complete](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment1_Web_Storage/screenshots/assignment1-mark-complete.png)

### Result

The note was successfully marked as complete. The completed note displayed a strikethrough effect and the control changed to `Mark Incomplete`.

The completed state was preserved after refreshing the webpage.

## Task 8: Verify Persistent Browser Storage

### Task Given

Use browser Developer Tools to verify that the Notes App data is actually being stored using the Web Storage API.

### Implementation

Chrome Developer Tools were opened and the Application tab was used to inspect Local Storage.

The application origin was selected under Local Storage.

The `notes` key was found and its stored JSON data was inspected.

The stored data contained the note objects and properties including:

- `id`
- `text`
- `completed`
- `createdAt`
- `updatedAt`

### Code Location

- [script.js](https://github.com/sehajvohra/BackendDevelopment/blob/main/Theory/Assignments/Assignment1_Web_Storage/script.js)

### Screenshot

![localStorage Verification](https://raw.githubusercontent.com/sehajvohra/BackendDevelopment/main/Theory/Assignments/Assignment1_Web_Storage/screenshots/assignment1-localstorage.png)

### Result

The `notes` key was successfully found in Local Storage and the stored JSON data was verified using Chrome Developer Tools.

## Project Structure

```text
Theory
└── Assignments
    └── Assignment1_Web_Storage
        ├── Report.md
        ├── index.html
        ├── script.js
        ├── style.css
        └── screenshots
            ├── assignment1-localstorage.png
            ├── assignment1-mark-complete.png
            └── assignment1-notes-app.png