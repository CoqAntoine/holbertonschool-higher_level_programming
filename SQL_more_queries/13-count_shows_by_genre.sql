-- Docstring

SELECT genres.name AS genre, COUNT(tg.tv_show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres tg ON g.id = tg.genre_id
GROUP BY g.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;