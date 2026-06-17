CREATE INDEX IF NOT EXISTS idx_posts_status
ON advance.posts(status);

SELECT 
    title,
    status,
    view
FROM advance.posts
WHERE status = 'published'
ORDER BY view DESC;