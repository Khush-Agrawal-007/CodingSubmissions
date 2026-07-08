# Write your MySQL query statement below
(
    -- Part 1: Find the user who rated the most movies
    SELECT u.name AS results
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.name
    ORDER BY COUNT(mr.movie_id) DESC, u.name ASC
    LIMIT 1
)

UNION ALL

(
    -- Part 2: Find the movie with the highest average rating in February 2020
    SELECT m.title AS results
    FROM Movies m
    JOIN MovieRating mr ON m.movie_id = mr.movie_id
    WHERE mr.created_at >= '2020-02-01' AND mr.created_at <= '2020-02-29'
    GROUP BY m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna