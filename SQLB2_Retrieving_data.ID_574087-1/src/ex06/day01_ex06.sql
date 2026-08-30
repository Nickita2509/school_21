SELECT t.action_date, person.name AS person_name
FROM (SELECT visit_date AS action_date, person_id 
FROM person_visits
INTERSECT
SELECT order_date AS action_date, person_id 
FROM person_order) AS t
JOIN person ON t.person_id = person.id
ORDER BY action_date, person_name DESC;
