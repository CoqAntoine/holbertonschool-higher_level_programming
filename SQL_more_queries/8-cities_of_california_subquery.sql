-- Lists all cities in the state of California
-- Results are sorted in ascending order by cities.id.

SELECT c.id, c.name, c.state_id
FROM cities c, states s
WHERE c.state_id = s.id
  AND s.name = 'California'
ORDER BY c.id ASC;