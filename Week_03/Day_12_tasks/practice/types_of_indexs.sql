-- ============================================================
-- PostgreSQL INDEXES REFERENCE FILE
-- Purpose:
-- Learn all important index types with examples
-- ============================================================


-- ============================================================
-- 1. SINGLE COLUMN INDEX
-- Used when queries filter on one column
-- ============================================================

-- Example Query:
-- SELECT * FROM users WHERE email='sai@gmail.com';

CREATE INDEX idx_users_email
ON users(email);

-- Why?
-- Faster lookup on exact email search

-- Good for:
-- WHERE email=
-- WHERE age>
-- ORDER BY created_at



-- ============================================================
-- 2. UNIQUE INDEX
-- Prevent duplicate values
-- ============================================================

CREATE UNIQUE INDEX idx_unique_email
ON users(email);

-- Equivalent to:
-- email TEXT UNIQUE

-- Example:
-- INSERT INTO users(email)
-- VALUES('sai@gmail.com');

-- If duplicate inserted → ERROR



-- ============================================================
-- 3. COMPOSITE INDEX
-- Index multiple columns together
-- Order matters
-- ============================================================

-- Query:
-- SELECT * FROM posts
-- WHERE status='published'
-- ORDER BY views DESC;

CREATE INDEX idx_posts_status_views
ON posts(status, views DESC);

-- Why?
-- Step 1 → Filter status
-- Step 2 → Already sorted by views descending

-- Leftmost prefix rule:
-- status                     → works
-- status + views            → works
-- views only                → does NOT work efficiently



-- ============================================================
-- 4. COMPOSITE INDEX (E-COMMERCE EXAMPLE)
-- ============================================================

-- Query:
-- SELECT * FROM products
-- WHERE category='electronics'
-- AND price < 50000;

CREATE INDEX idx_products_category_price
ON products(category, price);

-- Why?
-- First filter category
-- Then range filter price

-- Good:
-- category                  → works
-- category + price         → works

-- Bad:
-- price only               → usually not efficient



-- ============================================================
-- 5. PARTIAL INDEX
-- Index only specific rows
-- Saves memory
-- ============================================================

-- Suppose 90% queries ask only published posts

CREATE INDEX idx_published_posts
ON posts(status)
WHERE status='published';

-- Query:
-- SELECT * FROM posts
-- WHERE status='published';

-- Index stores ONLY rows where status=published

-- Faster than indexing all rows



-- ============================================================
-- 6. HASH INDEX
-- Optimized for exact equality comparisons
-- ============================================================

CREATE INDEX idx_hash_email
ON users USING HASH(email);

-- Good:
-- WHERE email='abc@gmail.com'

-- Bad:
-- WHERE email > 'abc@gmail.com'

-- Hash cannot handle ranges



-- ============================================================
-- 7. BRIN INDEX
-- Best for huge tables with naturally ordered data
-- Example: timestamps, logs, analytics
-- ============================================================

CREATE INDEX idx_orders_brin
ON orders USING BRIN(created_at);

-- Query:
-- SELECT * FROM orders
-- WHERE created_at > '2026-01-01';

-- Good for:
-- Large tables (millions of rows)



-- ============================================================
-- 8. GIN INDEX
-- Used for JSONB, arrays, full text search
-- ============================================================

-- Example table:
-- CREATE TABLE articles(
--     id SERIAL,
--     tags TEXT[]
-- );

CREATE INDEX idx_articles_tags
ON articles USING GIN(tags);

-- Query:
-- SELECT * FROM articles
-- WHERE tags @> ARRAY['python'];



-- ============================================================
-- 9. EXPRESSION INDEX
-- Index computed expressions
-- ============================================================

CREATE INDEX idx_lower_email
ON users(LOWER(email));

-- Query:
-- SELECT * FROM users
-- WHERE LOWER(email)='sai@gmail.com';

-- Normal email index may NOT work
-- Expression index solves that



-- ============================================================
-- 10. CHECK IF INDEX IS USED
-- EXPLAIN ANALYZE
-- ============================================================

EXPLAIN ANALYZE
SELECT *
FROM users
WHERE email='sai@gmail.com';

-- Output possibilities:

-- Seq Scan
-- Means:
-- PostgreSQL scanned entire table

-- Index Scan
-- Means:
-- PostgreSQL used index



-- ============================================================
-- 11. BAD INDEX EXAMPLE
-- Too many indexes slow writes
-- ============================================================

-- Every INSERT/UPDATE/DELETE
-- must update indexes

-- Example:

INSERT INTO users(name,email)
VALUES('Rahul','rahul@gmail.com');

-- Database work:

-- Insert row
-- Update idx_users_email
-- Update idx_unique_email
-- Update other indexes

-- More indexes = slower writes



-- ============================================================
-- 12. LEFTMOST PREFIX RULE (VERY IMPORTANT)
-- ============================================================

-- Index:
CREATE INDEX idx_emp
ON employees(department, salary, experience);

-- Query A
-- WHERE department='IT'
-- FULLY USED

-- Query B
-- WHERE department='IT' AND salary>50000
-- FULLY USED

-- Query C
-- WHERE salary>50000
-- NOT USED

-- Query D
-- WHERE department='IT' AND experience>3
-- PARTIALLY USED

-- Query E
-- WHERE department='IT' ORDER BY salary DESC
-- FULLY USED



-- ============================================================
-- RULES TO REMEMBER
-- ============================================================

-- INDEXES SPEED UP:
-- SELECT

-- INDEXES SLOW DOWN:
-- INSERT
-- UPDATE
-- DELETE

-- DO NOT INDEX EVERY COLUMN

-- CREATE INDEX ON:
-- Frequently searched columns
-- Foreign keys
-- Columns used in JOIN
-- Columns used in WHERE
-- Columns used in ORDER BY

-- AVOID INDEX ON:
-- Small tables
-- Frequently updated columns
-- Low cardinality columns (few unique values)