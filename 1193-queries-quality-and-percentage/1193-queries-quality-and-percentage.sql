select
    query_name ,
    round(avg(rating/position),2) quality,
    round(avg(rating<3)*100,2) poor_query_percentage
from
    queries
where query_name is not null
group by query_name;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna