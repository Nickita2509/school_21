INSERT INTO person_visits (id, person_id, pizzeria_id, visit_date)
VALUES
(
    (SELECT MAX(id) + 1 FROM person_visits),
    (SELECT id FROM person WHERE name = 'Dmitriy'),
    (
        SELECT p.id
        FROM pizzeria p
        JOIN menu m ON m.pizzeria_id = p.id
        WHERE m.price < 800
          AND p.name <> (SELECT pizzeria_name FROM mv_dmitriy_visits_and_eats)
        LIMIT 1
    ),
    DATE '2022-01-08'
);

REFRESH MATERIALIZED VIEW mv_dmitriy_visits_and_eats;
