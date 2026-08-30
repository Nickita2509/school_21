CREATE UNIQUE INDEX idx_person_order_order_date
ON person_order USING btree (person_id, menu_id)
WHERE order_date = DATE '2022-01-01';

SET enable_seqscan = off;

EXPLAIN ANALYZE
SELECT person_id, menu_id
FROM person_order
WHERE person_id = 1
  AND menu_id = 1
  AND order_date = DATE '2022-01-01';

