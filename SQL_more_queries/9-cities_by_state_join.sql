-- Lists all cities with their state names, sorted by cities.id
-- Results are sorted in ascending order by cities.id

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
