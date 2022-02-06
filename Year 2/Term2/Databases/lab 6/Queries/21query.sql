use University;

SELECT AVG (MIN (Salary)) AS AVG_MIN, 
AVG (MAX (Salary)) AS AVG_MAX, 
MIN (AVG (Salary)) AS MIN_AVG, 
MAX (AVG (Salary)) AS MAX_AVG 
FROM TEACHER 
GROUP BY Dolgnost;
