-- List the number of records with the same score in second_table
-- Display the score and the number of records for this score with the label number
-- Sort the list by the number of records in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
