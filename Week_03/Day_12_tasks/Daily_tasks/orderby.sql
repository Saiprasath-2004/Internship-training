SELECT
    u.user_name AS author_name,
    COUNT(p.id) AS total_posts,
    SUM(p.view) AS total_views
FROM  advance.users AS u
LEFT JOIN advance.posts AS p
    ON u.id = p.user_id
GROUP BY u.id, u.user_name
HAVING COUNT(p.id) >= 0
ORDER BY total_posts DESC;

SELECT 
    u.user_name AS author_name,
    COUNT(p.id) AS total_posts
FROM advance.users AS u
LEFT JOIN advance.posts AS p
    ON u.id= p.user_id
GROUP BY u.user_name
ORDER BY total_posts DESC;


SELECT 
    p.title as Post_title,
    p.view as post_views,
    t.name as tags_name 
FROM advance.posts AS p
INNER JOIN advance.post_tags AS pt 
    ON p.id=pt.post_id
INNER JOIN advance.tags AS t
    ON t.id =pt.tags_id
ORDER BY p.title,t.name