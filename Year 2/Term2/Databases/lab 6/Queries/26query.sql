use University;

SELECT NAME_TEACHER 
FROM TEACHER 
wheRE LOwER (Dolgnost) = 'teacher' OR 
LOWER (Dolgnost) = 'docent' 
ORDER BY NAME_TEACHER;
