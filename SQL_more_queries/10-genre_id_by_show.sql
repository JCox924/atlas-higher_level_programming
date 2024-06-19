-- Specifies database to use
USE hbtn_0d_tvshows;

-- List all shows with at least one genre linked
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT show.'title', g.'genre_id'
	FROM 'tv_shows' AS show
		INNER JOIN 'tv_show_genres' AS genre
		ON show.'id' = genre.'show_id'
ORDER BY show.'title', genre.'genre_id';
