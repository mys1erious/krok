use University;

SELECT NUM_KORPUSA AS "Housing", 
COUNT(*) AS "Amount of departments" 
FROM KAFEDRA GROUP BY NUM_KORPUSA;
