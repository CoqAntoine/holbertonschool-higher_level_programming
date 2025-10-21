-- Docstring

SELECT g.name
FROM tv_shows t
JOIN tv_show_genres tg ON t.id = tg.tv_show_id
JOIN genres g ON tg.genre_id = g.id
WHERE t.title = 'Dexter'
ORDER BY g.name ASC;