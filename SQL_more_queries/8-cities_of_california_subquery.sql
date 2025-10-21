-- Lists all cities in the state of California
-- Results are sorted in ascending order by cities.id.

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
