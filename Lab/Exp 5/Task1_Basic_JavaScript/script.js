const fruits = ["Apple", "Banana", "Mango"];

console.log("Array Demonstration");
console.log("Fruits:", fruits);

fruits.push("Orange");

console.log("After adding Orange:", fruits);

const student = {
  name: "Sehaj Vohra",
  age: 20,
  course: "Backend Development",
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
