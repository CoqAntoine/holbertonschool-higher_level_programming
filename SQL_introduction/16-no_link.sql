-- Script that lists all records of the table second_table
-- from the given database
-- Should not list rows where the name column is NULL or empty
-- Records are listed by descending score

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
