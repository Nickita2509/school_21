CREATE INDEX idx_person_name
ON person USING btree (UPPER(name));

EXPLAIN ANALYZE
SELECT *
FROM person
WHERE UPPER(name) = 'ANNA';


