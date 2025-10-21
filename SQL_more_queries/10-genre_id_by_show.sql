-- Lists all tv shows that have at least one genre, showing title and genre_id
-- Sorted by tv_shows.title and genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
