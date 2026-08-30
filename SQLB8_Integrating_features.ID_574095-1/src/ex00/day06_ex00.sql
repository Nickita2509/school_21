DROP TABLE IF EXISTS person_discounts CASCADE;

CREATE TABLE person_discounts (
    id bigint PRIMARY KEY,
    person_id bigint,
    pizzeria_id bigint,
    discount numeric(5,2),
    CONSTRAINT fk_person_discounts_person_id
        FOREIGN KEY (person_id) REFERENCES person(id),
    CONSTRAINT fk_person_discounts_pizzeria_id
        FOREIGN KEY (pizzeria_id) REFERENCES pizzeria(id)
);
