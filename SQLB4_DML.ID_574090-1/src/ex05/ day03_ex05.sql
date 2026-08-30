SELECT pi.name AS pizzeria_name
FROM person_visits pv 
JOIN person p ON pv.person_id = p.id
JOIN pizzeria pi ON pv.pizzeria_id = pi.id
WHERE p.name = 'Andrey'
EXCEPT
SELECT pi.name AS pizzeria_name
FROM person_order po  
JOIN person p ON po.person_id = p.id
JOIN menu m ON po.menu_id = m.id
JOIN pizzeria pi ON m.pizzeria_id = pi.id
WHERE p.name = 'Andrey'
ORDER BY pizzeria_name;
