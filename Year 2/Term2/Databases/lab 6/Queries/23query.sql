use University;

SELECT d.NAME_KAFEDRA, Count (*), SUM (t.salary + t.Rise)
 FROM FACULTET f, KAFEDRA d, TEACHER t 
WHERE f.KOD_FACULTETA = d.KOD_FACULTETA AND 
d.Kod_KAFEDRA = t.Kod_KAFEDRA AND 
LOWER (f. Name_faculteta) = 'Faculty1' AND 
LOWER (t.Dolgnost) = 'teacher' 
GROUP BY d.NAME_KAFEDRA;