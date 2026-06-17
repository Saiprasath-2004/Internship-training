CREATE SCHEMA IF NOT EXISTS basics;

CREATE EXTENSION IF NOT EXISTS pgcrypto;

DROP TABLE IF EXISTS basics.employee;

CREATE TABLE basics.employee(
    id UUID  PRIMARY KEY DEFAULT gen_random_uuid(),
    employee_name VARCHAR(100) NOT NULL,
    email_id TEXT NOT NULL UNIQUE,
    salary NUMERIC(10,2) NOT NULL,
    is_present BOOLEAN NOT NULL,
    created_at TIMESTAMP DEFAULT NOW() 
);

INSERT INTO basics.employee(employee_name,email_id,salary,is_present)
VALUES
('Sai','sai@gmail.com',90000.00,TRUE),
('Shantha','Shantha@gmail.com',100000.90,TRUE),
('Deepa','deepa@gmail.com',50000.00,TRUE),
('sri harisah','sriharsha@gmail.com',45000.00,False);




SELECT employee_name AS EMP_NAME,salary AS Salary,is_present FROM basics.employee 
WHERE salary>=50000 AND is_present = TRUE
ORDER BY salary DESC;

SELECT employee_name , salary FROM basics.employee
WHERE salary between 48000 AND 98000;