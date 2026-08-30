DELETE FROM person_discounts;

INSERT INTO person_discounts (id, person_id, pizzeria_id, discount)
SELECT
    ROW_NUMBER() OVER () AS id,
    t.person_id,
    t.pizzeria_id,
    CASE
        WHEN t.order_count = 1 THEN 10.5
        WHEN t.order_count = 2 THEN 22
        ELSE 30
    END AS discount
FROM (
    SELECT
        po.person_id,
        m.pizzeria_id,
        COUNT(*) AS order_count
    FROM person_order po
    JOIN menu m ON m.id = po.menu_id
    GROUP BY po.person_id, m.pizzeria_id
) AS t;
