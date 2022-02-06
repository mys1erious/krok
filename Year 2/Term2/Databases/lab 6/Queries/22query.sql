use University;

SELECT Kod_KAFEDRA as "Department num", 
Count (*) as "Amount of teachers in the department" 
FROM TEACHER 
WHERE dolgnost = 'teacher' 
GROUP BY Kod_KAFEDRA;