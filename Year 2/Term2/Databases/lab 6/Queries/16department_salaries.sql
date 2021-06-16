use University;

SELECT Kod_KAFEDRA AS "Department", 
SUM(SALARY) AS "Department salary" 
FROM Teacher GROUP BY Kod_KAFEDRA;
