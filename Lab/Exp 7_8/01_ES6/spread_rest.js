console.log("1. Spread Operator");

const numbers = [10, 20, 30];
const moreNumbers = [...numbers, 40, 50];

console.log("Original array:", numbers);
console.log("Copied and extended array:", moreNumbers);

console.log("\n2. Rest Parameters");

const calculateSum = (...values) => {
  let sum = 0;

  for (const value of values) {
    sum += value;
  }

  return sum;
};

console.log("Sum:", calculateSum(10, 20, 30, 40));

console.log("\n3. Default Parameters");

const greet = (name = "Student") => {
  return `Hello ${name}!`;
};

console.log(greet("Sehaj Vohra"));
console.log(greet());
