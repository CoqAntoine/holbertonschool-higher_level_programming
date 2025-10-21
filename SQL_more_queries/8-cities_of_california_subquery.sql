-- Lists all cities in the state of California
-- Results are sorted in ascending order by cities.id.

SELECT cities.id, cities.name 
 FROM cities 
 WHERE cities.state_id = (SELECT id FROM states WHERE name='California') 
 ORDER BY cities.id ASC;"
