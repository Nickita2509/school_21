SELECT p.name
FROM person p 
JOIN person_order po ON po.person_id = p.id
JOIN menu m ON po.menu_id = m.id
WHERE 
	p.gender = 'female' 
	AND
	(m.pizza_name = 'cheese pizza' OR m.pizza_name = 'pepperoni pizza')
GROUP BY p.name 
HAVING COUNT(DISTINCT m.pizza_name) = 2
ORDER BY name;