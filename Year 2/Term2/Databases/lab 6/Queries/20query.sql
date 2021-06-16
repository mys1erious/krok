use University;

SELECT Salary + Rise, COUNT(*) 
FROM TEACHER 
WHERE Salary + Rise <= 1500 GROUP BY Salary + Rise;
