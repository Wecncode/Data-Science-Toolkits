-- Query 1: List all movies released in the year 2008.
SELECT title 
FROM movies 
WHERE year = 2008;

-- Query 2: Determine the average rating of all movies directed by Christopher Nolan.
-- Requires joining movies, directors (linking table), people, and ratings.
SELECT AVG(ratings.rating) AS nolan_avg_rating
FROM movies
JOIN ratings ON movies.id = ratings.movie_id
JOIN directors ON movies.id = directors.movie_id
JOIN people ON directors.person_id = people.id
WHERE people.name = 'Christopher Nolan';

-- Query 3: Find the top 5 highest-grossing Sci-Fi movies of the 1990s.
SELECT movies.title, box_office.revenue
FROM movies
JOIN genres ON movies.id = genres.movie_id
JOIN box_office ON movies.id = box_office.movie_id
WHERE genres.genre = 'Sci-Fi' 
  AND movies.year BETWEEN 1990 AND 1999
ORDER BY box_office.revenue DESC
LIMIT 5;

-- Query 4: List the names of actors who starred in both "The Matrix" and "John Wick".
-- Using INTERSECT to find the overlap between two distinct queries.
SELECT people.name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title = 'The Matrix'

INTERSECT

SELECT people.name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title = 'John Wick';
