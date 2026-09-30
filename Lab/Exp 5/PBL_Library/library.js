const library = [];

function addBook(title, author) {
  const book = {
    title: title,
    author: author,
  };

  library.push(book);
  console.log("Book added:", title);
}

function findBook(title) {
  for (let i = 0; i < library.length; i++) {
    if (library[i].title === title) {
      return library[i];
    }
  }

  return null;
}

addBook("The Alchemist", "Paulo Coelho");
addBook("Wings of Fire", "A. P. J. Abdul Kalam");
addBook("Clean Code", "Robert Martin");

console.log("\nLibrary Books:");
console.log(library);

console.log("\nSearching for Wings of Fire:");

const result = findBook("Wings of Fire");

if (result !== null) {
  console.log("Book found:", result);
} else {
  console.log("Book not found");
}

console.log("\nSearching for Harry Potter:");

const secondResult = findBook("Harry Potter");

if (secondResult !== null) {
  console.log("Book found:", secondResult);
} else {
  console.log("Book not found");
}
