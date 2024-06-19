-- List all cities with their state names from the cities table
-- Each record should display: cities.id - cities.name - states.name
-- Sorted in ascending order by cities.id
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
