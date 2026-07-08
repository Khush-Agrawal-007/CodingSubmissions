WITH DailyTotals AS (
    -- Step 1: Combine all individual customer transactions per day
    SELECT 
        visited_on, 
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
),
MovingStats AS (
    -- Step 2: Calculate the rolling 7-day sum and average
    SELECT 
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(AVG(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS average_amount
    FROM DailyTotals
)
-- Step 3: Filter out the first 6 days since they don't have a full 7-day history
SELECT * 
FROM MovingStats
WHERE visited_on >= (
    SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY) FROM Customer
)
ORDER BY visited_on;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna