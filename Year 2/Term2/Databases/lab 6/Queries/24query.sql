use University;

SELECT MIN (Salary), MAX (Rise), SUM (Salary + Rise) 
FROM TEACHER 
HAVING SUM (Salary + Rise)> 15000;
