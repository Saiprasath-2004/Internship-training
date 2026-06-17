CREATE TABLE test_users(
   id SERIAL,
   email TEXT,
   age INT
);

INSERT INTO test_users(email,age)
VALUES
('a@gmail.com',20),
('b@gmail.com',21),
('c@gmail.com',22);

EXPLAIN ANALYZE
SELECT *
FROM test_users
WHERE email='a@gmail.com';