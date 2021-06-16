use University;

SELECT 'Name1 worked ' + 
CONVERT(NVARCHAR(20),ROUND(DATEDIFF (month, GETDATE(), DATA_HIRE), 1)) +
' month' AS "Tripod experience"
FROM TEACHER
WHERE NAME_TEACHER LIKE 'Name1%';
