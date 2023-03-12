-- Script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres
RIGHT JOIN tv_shows ON show_id = tv_shows.id
RIGHT JOIN tv_genres ON genre_id = tv_genres.id
WHERE title IS NOT NULL
ORDER BY title, name ASC;