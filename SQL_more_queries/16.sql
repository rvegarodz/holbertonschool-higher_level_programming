-- Script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres
RIGHT JOIN tv_shows ON show_id = tv_shows.id
RIGHT JOIN tv_genres ON genre_id = tv_genres.id;