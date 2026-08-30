SELECT m.pizza_name, m.price, p.name AS pizzeria_name
FROM
	(SELECT id AS menu_id
	FROM menu
	EXCEPT 
	SELECT menu_id
	FROM person_order) AS t
JOIN menu m ON t.menu_id = m.id
JOIN pizzeria p ON m.pizzeria_id = p.id
ORDER BY m.pizza_name, m.price;

