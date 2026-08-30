DROP SEQUENCE IF EXISTS seq_person_discounts CASCADE;

CREATE SEQUENCE seq_person_discounts
START WITH 1;

SELECT setval(
    'seq_person_discounts',
    (SELECT COUNT(*) + 1 FROM person_discounts),
    false
);

ALTER TABLE person_discounts
    ALTER COLUMN id SET DEFAULT nextval('seq_person_discounts');

ALTER SEQUENCE seq_person_discounts
    OWNED BY person_discounts.id;
