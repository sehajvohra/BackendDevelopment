const express = require("express");
const session = require("express-session");
const cookieParser = require("cookie-parser");

const app = express();
const PORT = 3001;

// Middleware
app.use(cookieParser());
app.use(express.urlencoded({ extended: true }));

// Session middleware
app.use(
  session({
    secret: "todo-secret-key",
    resave: false,
    saveUninitialized: true,
    cookie: {
      maxAge: 600000,
    },
  }),
);

// Home page
app.get("/", (req, res) => {
  if (!req.session.todos) {
    req.session.todos = [];
  }

  const todoItems = req.session.todos
    .map(
      (item, index) => `
            <li>
                ${item}
                <form action="/delete" method="POST" style="display:inline;">
                    <input type="hidden" name="id" value="${index}">
                    <button type="submit">Delete</button>
                </form>
            </li>
        `,
    )
    .join("");

  res.send(`
        <h1>Session Based To Do List</h1>

        <form action="/add" method="POST">
            <input
                type="text"
                name="todoItem"
                placeholder="Enter a to do item"
                required
            >
            <button type="submit">Add To Do</button>
        </form>

        <h2>Your To Do Items</h2>

        ${todoItems ? `<ul>${todoItems}</ul>` : "<p>No to do items yet.</p>"}

        <br>

        <form action="/clear" method="POST">
            <button type="submit">Clear All</button>
        </form>
    `);
});

// Add a to do item
app.post("/add", (req, res) => {
  if (!req.session.todos) {
    req.session.todos = [];
  }

  req.session.todos.push(req.body.todoItem);

  res.redirect("/");
});

// Delete a to do item
app.post("/delete", (req, res) => {
  const id = Number(req.body.id);

  if (req.session.todos) {
    req.session.todos = req.session.todos.filter((item, index) => index !== id);
  }

  res.redirect("/");
});

// Clear all to do items
app.post("/clear", (req, res) => {
  req.session.todos = [];

  res.redirect("/");
});

// Start server
app.listen(PORT, () => {
  console.log(`To Do server running at http://localhost:${PORT}`);
});
