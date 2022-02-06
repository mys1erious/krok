use University;

SELECT AVG (Salary), AVG (Rise), SUM (Salary + Rise) 
FROM TEACHER
WHERE LOWER (Dolgnost) = 'assistant' 
HAVING SUM (Salary + Rise)> 2500;
