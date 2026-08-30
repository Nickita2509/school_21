DROP INDEX IF EXISTS idx_1;

CREATE INDEX idx_1
ON pizzeria USING btree (rating);

EXPLAIN ANALYZE
SELECT
    m.pizza_name AS pizza_name,
    max(pz.rating) OVER (
        PARTITION BY pz.rating
        ORDER BY pz.rating
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS k
FROM menu m
INNER JOIN pizzeria pz ON m.pizzeria_id = pz.id
ORDER BY 1, 2;