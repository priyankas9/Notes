## Script for service delivery data flush

---

-- Update containments table

UPDATE fsm.containments
SET
    status = 0,
    emptied_status = false,
    next_emptying_date = NULL,
    no_of_times_emptied = 0,
    priority = NULL,
    fstp_distance = NULL;

-- Truncate other tables (with CASCADE if there are FK dependencies)
TRUNCATE TABLE fsm.feedbacks RESTART IDENTITY CASCADE;
TRUNCATE TABLE fsm.sludge_collections RESTART IDENTITY CASCADE;
TRUNCATE TABLE fsm.supervisory_assessment RESTART IDENTITY CASCADE;
TRUNCATE TABLE fsm.emtyings RESTART IDENTITY CASCADE;
TRUNCATE TABLE fsm.applications RESTART IDENTITY CASCADE;


## Update application table

---

ALTER TABLE fsm.applications
ALTER COLUMN supervisory_assessment_status SET DEFAULT false;
