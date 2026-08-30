SELECT DISTINCT p2.name AS pizzeria_name
FROM
	(SELECT *
	FROM person_visits pv
	WHERE visit_date = '2022-01-08') AS t
JOIN person p ON p.id = t.person_id
JOIN menu m ON m.pizzeria_id = t.pizzeria_id
JOIN pizzeria p2 ON p2.id = m.pizzeria_id
WHERE m.price < 800 AND p.name = 'Dmitriy';