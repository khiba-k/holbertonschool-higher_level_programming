-- script lisst records with score >= 10
SELECT score, name
FROM second_table
ORDER BY score ASC
WHERE score >= 10
