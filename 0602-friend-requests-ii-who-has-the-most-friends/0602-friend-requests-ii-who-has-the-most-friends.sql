# Write your MySQL query statement below
WITH AllFriends AS (
    -- Get all IDs that sent a request
    SELECT requester_id AS id 
    FROM RequestAccepted
    
    UNION ALL
    
    -- Combine with all IDs that accepted a request
    SELECT accepter_id AS id 
    FROM RequestAccepted
)

-- Count the occurrences of each ID
SELECT id, COUNT(id) AS num
FROM AllFriends
GROUP BY id
ORDER BY num DESC
LIMIT 1;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna