// Lecture 13
// MongoDB Practical

// Select database
use("student_management");

// Insert 3 student documents
db.students.insertMany([
  {
    name: "Aarav Sharma",
    branch: "CSE",
    email: "aarav.sharma@example.com",
    enrollment_date: "2024-01-15",
  },
  {
    name: "Diya Kapoor",
    branch: "ECE",
    email: "diya.kapoor@example.com",
    enrollment_date: "2024-02-10",
  },
  {
    name: "Priya Singh",
    branch: "CSE",
    email: "priya.singh@example.com",
    enrollment_date: "2024-03-05",
  },
]);

// Retrieve all students in the CSE branch
db.students.find({ branch: "CSE" }).pretty();

// PostgreSQL vs MongoDB comparison
//
// PostgreSQL:
// Uses tables, rows, and columns.
// Uses SQL queries.
// Uses a fixed schema.
// Supports relationships using foreign keys.
// Suitable for structured data and complex queries.
//
// MongoDB:
// Uses collections and documents.
// Uses MongoDB query methods.
// Uses a flexible document structure.
// Supports embedded documents and references.
// Suitable for flexible and evolving data.
