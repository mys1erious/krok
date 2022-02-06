use University;

SELECT SUM(Salary) as salary_sum
FROM TEACHER WHERE 
LOWER (DOLGNOST) = 'assistant';
