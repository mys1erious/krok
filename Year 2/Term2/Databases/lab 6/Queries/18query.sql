use University;

SELECT f.NAME_FACULTETA, s.GROUP_NAME, 
count (s.GROUP_NAME) AS "Amount of students in the group" 
FROM FACULTET f, KAFEDRA d, STUDENT s 
WHERE f.KOD_FACULTETA = d.KOD_FACULTETA AND 
d.Kod_KAFEDRA = s.Kod_KAFEDRA AND 
d.NUM_KORPUSA = '1' 
GROUP BY f.Name_faculteta, s.GROUP_NAME;
