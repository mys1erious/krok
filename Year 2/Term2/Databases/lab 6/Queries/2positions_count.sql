use University;

select count(distinct dolgnost)
from Kafedra d, Teacher t
where d.Kod_KAFEDRA = t.Kod_KAFEDRA and
lower(d.NAME_KAFEDRA) = 'Department1';