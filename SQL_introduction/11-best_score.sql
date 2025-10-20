-- Script that list all records of the table second_table
-- Results display the score and name, ordered by score
-- When the score is 10 or more.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
