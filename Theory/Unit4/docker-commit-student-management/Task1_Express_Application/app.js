const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());

// Initial student records stored in memory.
let students = [
  { id: 1, name: "Sehaj Vohra", course: "BTech" },
  { id: 2, name: "Ajay Sah", course: "MTech" },
];

app.get("/", (req, res) => {
  res.send("Welcome to the Student Management API. The server is running.");
});

app.get("/students", (req, res) => {
  res.json(students);
});

app.get("/students/:id", (req, res) => {
  const studentId = Number.parseInt(req.params.id, 10);

  if (Number.isNaN(studentId)) {
    return res.status(400).json({ message: "Student ID must be a number." });
  }

  const student = students.find((item) => item.id === studentId);

  if (!student) {
    return res.status(404).json({ message: "Student not found." });
  }

  return res.json(student);
});

app.post("/students", (req, res) => {
  const { name, course } = req.body;

  if (
    typeof name !== "string" ||
    !name.trim() ||
    typeof course !== "string" ||
    !course.trim()
  ) {
    return res.status(400).json({
      message: "Both name and course are required.",
    });
  }

  const nextId =
    students.length > 0
      ? Math.max(...students.map((student) => student.id)) + 1
      : 1;

  const newStudent = {
    id: nextId,
    name: name.trim(),
    course: course.trim(),
  };

  students.push(newStudent);
  return res.status(201).json(newStudent);
});

app.delete("/students/:id", (req, res) => {
  const studentId = Number.parseInt(req.params.id, 10);

  if (Number.isNaN(studentId)) {
    return res.status(400).json({ message: "Student ID must be a number." });
  }

  const studentIndex = students.findIndex(
    (student) => student.id === studentId,
  );

  if (studentIndex === -1) {
    return res.status(404).json({ message: "Student not found." });
  }

  const deletedStudent = students.splice(studentIndex, 1)[0];
  return res.json({
    message: "Student deleted successfully.",
    student: deletedStudent,
  });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Student Management API running on port ${PORT}`);
});
