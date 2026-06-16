CREATE SCHEMA IF NOT EXISTs basics;

CREATE EXTENSION IF NOT EXISTs pgcrypto;

CREATE TABLE basics.users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INT ,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO basics.users(name,email,age)
VALUES 
('SAI','saiprasath@gmail.com',21),
('Balaji','Balagi@gmail.com',26),
('Chandru','Chandru@gmail.com',24),
('Snegan','Snegan@gmail.com',22),
('Manoj','Manoj@gmail.com',23);

SELECT * FROM basics.users;

SELECT * FROM basics.users WHERE name LIKE 'S%' ORDER BY id;
