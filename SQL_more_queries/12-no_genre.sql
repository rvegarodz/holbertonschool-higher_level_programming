-- Script that lists all shows contained in the database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_show_genres
RIGHT JOIN tv_shows ON show_id = tv_shows.id
WHERE genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
