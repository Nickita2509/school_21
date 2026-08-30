SELECT pizzeria_name 
FROM 
	(SELECT pi.name AS pizzeria_name
	FROM person_order po 
	JOIN menu m ON po.menu_id =m.id
	JOIN person p ON po.person_id = p.id
	JOIN pizzeria pi ON m.pizzeria_id = pi.id
	WHERE p.gender = 'female'
	EXCEPT
	SELECT pi.name AS pizzeria_name
	FROM person_order po 
	JOIN menu m ON po.menu_id =m.id
	JOIN person p ON po.person_id = p.id
	JOIN pizzeria pi ON m.pizzeria_id = pi.id
	WHERE p.gender = 'male') AS t1
UNION
SELECT pizzeria_name 
FROM 
	(SELECT pi.name AS pizzeria_name
	FROM person_order po 
	JOIN menu m ON po.menu_id =m.id
	JOIN person p ON po.person_id = p.id
	JOIN pizzeria pi ON m.pizzeria_id = pi.id
	WHERE p.gender = 'male'
	EXCEPT
	SELECT pi.name AS pizzeria_name
	FROM person_order po 
	JOIN menu m ON po.menu_id =m.id
	JOIN person p ON po.person_id = p.id
	JOIN pizzeria pi ON m.pizzeria_id = pi.id
	WHERE p.gender = 'female') AS t2
ORDER BY pizzeria_name;