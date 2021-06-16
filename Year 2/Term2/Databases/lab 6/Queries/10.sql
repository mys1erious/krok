use University;

SELECT SUM(Salary) * 100 / SUM(Rise) AS "% from salary to salary", 
	   SUM(Rise) * 100 / SUM(Salary) AS "% from salary to rate" 
FROM TEACHER;
