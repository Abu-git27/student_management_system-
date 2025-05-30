CREATE DATABASE IF NOT EXISTS student_db;

USE student_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT,
    course VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15),
    photo VARCHAR(255)
);
