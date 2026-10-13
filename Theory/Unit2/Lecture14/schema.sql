CREATE TABLE Author (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    nationality VARCHAR(50)
);

CREATE TABLE Book (
    book_id INT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    ISBN VARCHAR(20) UNIQUE,
    publication_year INT,
    category VARCHAR(50)
);


CREATE TABLE Member (
    member_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    address VARCHAR(200)
);

CREATE TABLE Loan (
    loan_id INT PRIMARY KEY,
    member_id INT NOT NULL,
    book_id INT NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE,
    return_date DATE,
    status VARCHAR(20) DEFAULT 'Borrowed',
    FOREIGN KEY (member_id) REFERENCES Member(member_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);


CREATE TABLE BookAuthor (
    book_id INT,
    author_id INT,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (author_id) REFERENCES Author(author_id)
);
