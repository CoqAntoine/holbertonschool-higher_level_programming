-- Script that lists the number of records with the same score
-- from the table second_table sorted by number (descending)
-- The result displays:
--   score
--   number of records for this score (as 'number')

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
