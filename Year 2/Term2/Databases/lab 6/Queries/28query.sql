use University;

SELECT Name_teacher, Data_hire 
FROM TEACHER 
WHERE LOWER (Dolgnost) = 'assistant' 
ORDER BY Data_hire ASC;
