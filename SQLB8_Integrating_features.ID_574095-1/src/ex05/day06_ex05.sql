COMMENT ON TABLE person_discounts IS
'Stores personal discount percentages for each person in each pizzeria.';

COMMENT ON COLUMN person_discounts.id IS
'Primary key of the personal discount record.';

COMMENT ON COLUMN person_discounts.person_id IS
'Reference to the customer who receives the discount.';

COMMENT ON COLUMN person_discounts.pizzeria_id IS
'Reference to the pizzeria where the discount is applied.';

COMMENT ON COLUMN person_discounts.discount IS
'Personal discount percentage for the customer in the selected pizzeria.';
