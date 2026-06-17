CREATE SCHEMA IF NOT EXISTS advance;
CREATE EXTENSION IF NOT EXISTS pgcrypto;

DROP TABLE IF EXISTS advance.post_tags;
DROP TABLE IF EXISTS advance.comments;
DROP TABLE IF EXISTS advance.posts;
DROP TABLE IF EXISTS advance.tags;
DROP TABLE IF EXISTS advance.users;

CREATE TABLE advance.users(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_name TEXT NOT NULL ,
    email_id TEXT UNIQUE NOT NULL
);

CREATE TABLE advance.posts(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES advance.users(id),
    title TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'draft'
        CHECK (status IN ('draft','published')),
    view INTEGER NOT NULL DEFAULT 0 CHECK(view>=0)
);

CREATE TABLE advance.comments(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    post_id UUID NOT NULL REFERENCES advance.posts(id),
    body TEXT NOT NULL
);

CREATE TABLE advance.tags(
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL UNIQUE 
);

CREATE TABLE advance.post_tags(
    post_id UUID NOT NULL REFERENCES advance.posts(id),
    tags_id UUID NOT NULL REFERENCES advance.tags(id)
);


-- Users Datas Insertion

INSERT INTO advance.users(user_name,email_id)
VALUES
('Ananya','ananya@gmail.com'),
('Rahul','rahul@gmail.com'),
('Vijay','vijay@gmail.com'),
('priya','priya@gmail.com');


--posts Datas Insertion

INSERT INTO advance.posts(user_id,title,status,view)
SELECT id, 'Postgresql tutorial','published',2000000
FROM advance.users
WHERE user_name='Ananya';

INSERT INTO advance.posts(user_id,title,status,view)
SELECT id, 'Python tutorial','published',4000000
FROM advance.users
WHERE user_name='Ananya';

INSERT INTO advance.posts(user_id,title,status,view)
SELECT id, 'Java with springboot','published',200000
FROM advance.users
WHERE user_name='Rahul';

INSERT INTO advance.posts(user_id,title,status,view)
SELECT id, 'OOPS in Java','published',700000
FROM advance.users
WHERE user_name='Rahul';

INSERT INTO advance.posts(user_id,title,status,view)
SELECT id, 'fast api','published',1234567
FROM advance.users
WHERE user_name='Vijay';


--Comments datas Insertion

INSERT INTO advance.comments(post_id,body)
SELECT id ,'Very clear explanation.'
FROM advance.posts
WHERE title ='Postgresql tutorial';

INSERT INTO advance.comments(post_id,body)
SELECT id ,'the post gave a good depth knowledge'
FROM advance.posts
WHERE title ='OOPS in Java';

INSERT INTO advance.comments(post_id,body)
SELECT id ,'the crud operation implementation was good'
FROM advance.posts
WHERE title ='fast api';

INSERT INTO advance.comments(post_id,body)
SELECT id ,'the post covered every concepts of python clearly'
FROM advance.posts
WHERE title ='Python tutorial';

--tags data insertion
 
INSERT INTO advance.tags(name)
VALUES 
('SQL'),
('Backend'),
('oops'),
('Coding langauge');


--posts tags data insertion 

INSERT INTO advance.post_tags (post_id, tags_id)
SELECT p.id, t.id
FROM advance.posts p, advance.tags t
WHERE p.title = 'Postgresql tutorial'
  AND t.name = 'SQL';

INSERT INTO advance.post_tags (post_id, tags_id)
SELECT p.id, t.id
FROM advance.posts p, advance.tags t
WHERE p.title = 'OOPS in Java'
  AND t.name = 'oops';

INSERT INTO advance.post_tags (post_id, tags_id)
SELECT p.id, t.id
FROM advance.posts p, advance.tags t
WHERE p.title = 'fast api'
  AND t.name = 'Backend';

INSERT INTO advance.post_tags (post_id, tags_id)
SELECT p.id, t.id
FROM advance.posts p, advance.tags t
WHERE p.title = 'Java with springboot'
  AND t.name = 'Backend';

INSERT INTO advance.post_tags (post_id, tags_id)
SELECT p.id, t.id
FROM advance.posts p, advance.tags t
WHERE p.title = 'Java with springboot'
  AND t.name = 'Coding langauge';

INSERT INTO advance.post_tags (post_id, tags_id)
SELECT p.id, t.id
FROM advance.posts p, advance.tags t
WHERE p.title = 'Python tutorial'
  AND t.name = 'Coding langauge';
