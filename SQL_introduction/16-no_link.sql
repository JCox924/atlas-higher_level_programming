-- List all records from second_table
-- Display score and name, ordered by score in descending order
-- Exclude rows without a name value
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
