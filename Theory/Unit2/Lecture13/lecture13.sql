-- Lecture 13
-- Introduction to Databases
-- PostgreSQL Practical

-- Create database
CREATE DATABASE student_management;

-- Connect to the database
-- \c student_management

-- Create students table
CREATE TABLE students (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    branch VARCHAR(50) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    enrollment_date DATE
);

-- Insert 5 student records
INSERT INTO students (name, branch, email, enrollment_date)
VALUES
    ('Aarav Sharma', 'CSE', 'aarav.sharma@example.com', '2024-01-15'),
    ('Diya Kapoor', 'ECE', 'diya.kapoor@example.com', '2024-02-10'),
    ('Rohan Mehta', 'IT', 'rohan.mehta@example.com', '2023-08-20'),
    ('Priya Singh', 'CSE', 'priya.singh@example.com', '2024-03-05'),
    ('Ananya Joshi', 'CSE', 'ananya.joshi@example.com', '2023-09-12');

-- Retrieve all students in the CSE branch
SELECT * FROM students
WHERE branch = 'CSE';

-- Find students enrolled after January 2024
SELECT * FROM students
WHERE enrollment_date > '2024-01-01';

-- Update a student's branch
UPDATE students
SET branch = 'ECE'
WHERE id = 1;

-- Delete a student record
DELETE FROM students
WHERE id = 3;

-- Final verification
SELECT * FROM students
ORDER BY id;