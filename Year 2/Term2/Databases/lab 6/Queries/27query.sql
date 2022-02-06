use University;

SELECT Name_teacher, Salary + Rise 
FROM TEACHER 
WHERE LOWER (Dolgnost) = 'assistant' 
ORDER BY Salary + Rise;
