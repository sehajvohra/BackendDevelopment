const express = require("express");
const { MongoClient, ObjectId } = require("mongodb");

const app = express();
const PORT = 3000;

// MongoDB connection details
const mongoURL = "mongodb://127.0.0.1:27017";
const client = new MongoClient(mongoURL);

let notesCollection;

// EJS configuration
app.set("view engine", "ejs");

// Read form data
app.use(express.urlencoded({ extended: true }));

// Serve CSS files
app.use(express.static("public"));

// Connect to MongoDB
async function connectDB() {
  await client.connect();

  const database = client.db("notes_lab");

  notesCollection = database.collection("notes");

  console.log("Connected to MongoDB");
}

// Home page
app.get("/", async (req, res) => {
  const notes = await notesCollection.find().toArray();

  res.render("index", { notes: notes });
});

// Add note form
app.get("/notes/new", (req, res) => {
  res.render("new");
});

// Add note
app.post("/notes", async (req, res) => {
  const { title, content, category } = req.body;

  // Validate title and content
  if (!title || !content) {
    return res.send("Title and content are required");
  }

  await notesCollection.insertOne({
    title: title,
    content: content,
    category: category,
    createdAt: new Date(),
  });

  res.redirect("/");
});

// Delete note
app.post("/notes/:id/delete", async (req, res) => {
  await notesCollection.deleteOne({
    _id: new ObjectId(req.params.id),
  });

  res.redirect("/");
});

// Start server after connecting to MongoDB
connectDB()
  .then(() => {
    app.listen(PORT, () => {
      console.log(`Server running at http://localhost:${PORT}`);
    });
  })
  .catch((error) => {
    console.log("MongoDB connection error:", error);
  });
