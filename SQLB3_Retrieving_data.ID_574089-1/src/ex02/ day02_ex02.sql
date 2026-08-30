SELECT 
	COALESCE 
		(person.name, '-') AS person_name, pv.visit_date,
	COALESCE 
	(pizzeria.name, '-') AS pizzeria_name
FROM (SELECT *
	FROM person_visits
	WHERE person_visits.visit_date BETWEEN '2022-01-01' AND '2022-01-03') AS pv
FULL JOIN pizzeria ON pv.pizzeria_id = pizzeria.id
FULL JOIN person ON pv.person_id = person.id
ORDER BY person_name, pv.visit_date, pizzeria_name;
