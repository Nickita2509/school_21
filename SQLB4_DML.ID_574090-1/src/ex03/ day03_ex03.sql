SELECT pizzeria_name 
FROM 
	(SELECT pi.name AS pizzeria_name
	FROM person_visits pv
	JOIN person p ON pv.person_id = p.id
	JOIN pizzeria pi ON pv.pizzeria_id = pi.id
	WHERE p.gender = 'female'
	EXCEPT ALL 
	SELECT pi.name AS pizzeria_name
	FROM person_visits pv
	JOIN person p ON pv.person_id = p.id
	JOIN pizzeria pi ON pizzeria_id = pi.id
	WHERE p.gender = 'male') AS t1
UNION ALL 
SELECT pizzeria_name 
FROM 
	(SELECT pi.name AS pizzeria_name
	FROM person_visits pv
	JOIN person p ON pv.person_id = p.id
	JOIN pizzeria pi ON pv.pizzeria_id = pi.id
	WHERE p.gender = 'male'
	EXCEPT ALL 
	SELECT pi.name AS pizzeria_name
	FROM person_visits pv
	JOIN person p ON pv.person_id = p.id
	JOIN pizzeria pi ON pizzeria_id = pi.id
	WHERE p.gender = 'female') AS t2
ORDER BY pizzeria_name;