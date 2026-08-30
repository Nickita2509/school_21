INSERT INTO person_order (id, person_id, menu_id, order_date)
SELECT
    gs.new_id,
    p.id AS person_id,
    (SELECT id FROM menu WHERE pizza_name = 'greek pizza') AS menu_id,
    DATE '2022-02-25' AS order_date
FROM person p
JOIN generate_series(
    (SELECT MAX(id) + 1 FROM person_order),
    (SELECT MAX(id) + (SELECT COUNT(*) FROM person) FROM person_order)
) AS gs(new_id)
    ON gs.new_id = (SELECT MAX(id) FROM person_order) + p.id;
