SELECT m.pizza_name, m.price, p2.name AS pizzeria_name, pv.visit_date
FROM person p
JOIN person_visits pv ON p.id = pv.person_id
JOIN menu m ON pv.pizzeria_id  = m.pizzeria_id 
JOIN pizzeria p2 ON m.pizzeria_id = p2.id
WHERE p.name = 'Kate' AND price >= 800 AND price <= 1000
ORDER BY pizza_name, price, pizzeria_name;