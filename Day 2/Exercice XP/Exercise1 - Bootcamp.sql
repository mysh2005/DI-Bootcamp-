-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

CREATE DATABASE bootcamp
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE students(
 id SERIAL PRIMARY KEY,
 last_name VARCHAR (50) NOT NULL,
 first_name VARCHAR (100) NOT NULL,
 birth_date DATE NOT NULL
)

INSERT INTO students (last_name, first_name, birth_date)
VALUES('Benichou','Marc','11/02/1998'),
('Cohen','Yoan','12/03/2010'),
('Benichou','Lea','07/27/1987'),
('Dux','Amelia','04/07/1996'),
('Grez','David','06/14/2003'),
('Simpson','Omer','10/03/1980');

INSERT INTO students (last_name, first_name, birth_date)
VALUES ('Ramburrun','Myshti','09/25/2005');

SELECT * FROM students;
SELECT first_name, last_name FROM students;

SELECT first_name, last_name FROM students where id = 2;
SELECT first_name, last_name FROM students where last_name = 'Benichou' and first_name = 'Marc';
SELECT first_name, last_name FROM students where last_name = 'Benichou' or first_name = 'Marc';
SELECT first_name, last_name FROM students where first_name like '%a%';
SELECT first_name, last_name FROM students where first_name like 'A%';
SELECT first_name, last_name FROM students where first_name like '%a';
SELECT first_name, last_name FROM students where first_name like 'a%';
SELECT first_name, last_name FROM students where first_name like '%a_';
SELECT first_name, last_name FROM students where id in (1,3);

SELECT * FROM students where birth_date >='1/01/2000';