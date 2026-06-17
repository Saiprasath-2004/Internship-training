SELECT  advance.users.user_name AS authors_name,
        advance.posts.title AS post_title,
        advance.posts.status,
        advance.posts.view
FROM advance.posts
INNER JOIN advance.users
    ON advance.posts.user_id = advance.users.id

WHERE advance.posts.status ='published'
ORDER BY advance.posts.view DESC;

SELECT  advance.users.user_name AS authors_name,
        advance.posts.title AS post_title,
        advance.posts.status,
        advance.posts.view
FROM advance.users
LEFT JOIN advance.posts
    ON advance.users.id = advance.posts.user_id

ORDER BY advance.posts.view DESC;

