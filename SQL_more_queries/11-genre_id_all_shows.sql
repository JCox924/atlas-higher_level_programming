-- Specifes database to use
USE hbtn_0d_tvshows;

-- List all shows with their genres from the database hbtn_0d_tvshows
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Include shows without genres (display NULL for genre_id)

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
