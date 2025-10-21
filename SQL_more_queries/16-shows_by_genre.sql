-- Docstring

SELECT t.title, g.name AS genre
FROM tv_shows t
LEFT JOIN tv_show_genres tg ON t.id = tg.tv_show_id
LEFT JOIN genres g ON tg.genre_id = g.id
ORDER BY t.title ASC, genre ASC;