-- List all genres by their rating
SELECT genres.name, SUM(rating) AS rating
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genres.name
ORDER BY rating DESC;

