SELECT m.pizza_name, p2.name AS pizzeria_name
FROM person_order AS po
JOIN menu AS m ON m.id = po.menu_id
JOIN person AS p ON p.id = po.person_id
JOIN pizzeria AS p2 ON p2.id = m.pizzeria_id
WHERE p.name = 'Denis' OR p.name = 'Anna'
ORDER BY m.pizza_name, pizzeria_name;
