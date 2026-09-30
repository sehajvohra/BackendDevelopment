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
  course: "B.Tech CSE",
};

console.log("\nObject Demonstration");
console.log("Original:", student);

student.semester = 5;
console.log("After adding semester:", student);

console.log("Student name:", student.name);

student.course = "Computer Science";
console.log("After updating course:", student);
