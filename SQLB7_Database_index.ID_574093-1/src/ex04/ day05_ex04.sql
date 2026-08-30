CREATE UNIQUE INDEX idx_menu_unique
ON menu USING btree (pizzeria_id, pizza_name);

SET enable_seqscan = off;

EXPLAIN ANALYZE
SELECT *
FROM menu
WHERE pizzeria_id = 2
  AND pizza_name = 'greek pizza';
