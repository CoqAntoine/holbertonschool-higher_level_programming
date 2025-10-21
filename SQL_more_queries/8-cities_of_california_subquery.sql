-- Lists all cities in the state of California
-- Results are sorted in ascending order by cities.id.

SELECT cities.id, cities.name, cities.state_id
FROM cities
WHERE states.name = 'California'
ORDER BY cities.id ASC;
