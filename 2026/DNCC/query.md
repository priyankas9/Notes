# Queries

---

## 04.Jan

Alter table fsm.service_providers
Add column service_area character varying;

CREATE TABLE IF NOT EXISTS fsm.desludging_schedule_temp
(
    id bigint NOT NULL DEFAULT nextval('fsm.desludging_schedule_temp_id_seq'::regclass),
    service_provider_id bigint NOT NULL,
    service_provider_name character varying(255) COLLATE pg_catalog."default",
    bin character varying(50) COLLATE pg_catalog."default" NOT NULL,
    ward integer,
    containment_id character varying COLLATE pg_catalog."default" NOT NULL,
    fstp_distance numeric,
    owner_name character varying(255) COLLATE pg_catalog."default",
    owner_contact character varying(50) COLLATE pg_catalog."default",
    owner_gender character varying(20) COLLATE pg_catalog."default",
    respondent_name character varying(255) COLLATE pg_catalog."default",
    respondent_contact character varying(50) COLLATE pg_catalog."default",
    status integer,
    generated_by bigint,
    generated_at timestamp without time zone DEFAULT now(),
    house_number character varying COLLATE pg_catalog."default",
    house_locality character varying COLLATE pg_catalog."default",
    road_code character varying COLLATE pg_catalog."default",
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    priority integer,
    CONSTRAINT desludging_schedule_temp_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

CREATE SEQUENCE IF NOT EXISTS fsm.desludging_schedule_temp_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
    OWNED BY desludging_schedule_temp.id;

ALTER SEQUENCE fsm.desludging_schedule_temp_id_seq
    OWNER TO postgres;

## 22.jan MultiTrip query

---

ALTER TABLE fsm.applications

RENAME COLUMN emptying_status TO emptying_status_old;

ALTER TABLE fsm.applications
RENAME COLUMN feedback_status TO feedback_status_old;

ALTER TABLE fsm.applications
RENAME COLUMN sludge_collection_status TO sludge_collection_status_old;

Alter table fsm.applications
add column trip_count integer,
add column    emptying_status integer,
add column   sludge_collection_status integer,
add column   feedback_status integer;

UPDATE fsm.applications
SET
    emptying_status = CASE
                        WHEN emptying_status_old = 'true' THEN 2
                        WHEN emptying_status_old = 'false' THEN 0
                        ELSE emptying_status
                     END,
    feedback_status = CASE
                        WHEN feedback_status_old = 'true' THEN 1
                        WHEN feedback_status_old = 'false' THEN 0
                        ELSE feedback_status
                     END,
    sludge_collection_status = CASE
                                WHEN sludge_collection_status_old = 'true' THEN 2
                                WHEN sludge_collection_status_old = 'false' THEN 0
                                ELSE sludge_collection_status
                               END;

Alter table fsm.emptyings
add column trip_no integer,
add column total_time integer;

alter table fsm.emptyings
drop column no_of_trips ;

alter table fsm.sludge_collections
add column total_time integer

CREATE TABLE fsm.sludge_collections_log (
    id SERIAL PRIMARY KEY,
    application_id INTEGER REFERENCES fsm.applications(id),
    treatment_plant_id INTEGER REFERENCES fsm.treatment_plants(id),
    volume_of_sludge NUMERIC,
    date DATE,
    entry_time TIME,
    exit_time TIME,
    desludging_vehicle_id INTEGER REFERENCES fsm.desludging_vehicles(id),
    user_id INTEGER REFERENCES auth.users(id),
    service_provider_id INTEGER REFERENCES fsm.service_providers(id),
    tipping_fee_amount NUMERIC,
    tipping_fee_receipt_no VARCHAR,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP WITHOUT TIME ZONE
);

Alter table fsm.sludge_collections
add column trip_no integer,
add column tipping_fee_amount numeric,
add column tipping_fee_receipt_no character varying;

alter table fsm.sludge_collections
drop column no_of_trips ;

**nOTICE module**
Alter table pdf_body_data
ADD column  digital_signature text ,
ADD column  signatory_name character varying(255) ,
ADD column  signatory_position character varying(255) ,
ADD column  footer text;


ALTER TABLE FSM.APPLICATIONS
DROP COLUMN  emptying_status_old ,
DROP COLUMN  feedback_status_old ,
DROP COLUMN  sludge_collection_status_old

**NOTICE GENERATION & IMPROVEMENT PLAN TABLE**

CREATE SEQUENCE IF NOT EXISTS public.generatednotice_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

    CREATE TABLE IF NOT EXISTS public.generatednotice
(
    id integer NOT NULL DEFAULT nextval('generatednotice_id_seq'::regclass),
    user_id integer,
    notice_generation_date timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    filters text COLLATE pg_catalog."default",
    pdf_generation_id integer,
    updated_at timestamp without time zone,
    created_at timestamp without time zone,
    pdf_path text COLLATE pg_catalog."default",
    status character varying(20) COLLATE pg_catalog."default" DEFAULT 'pending'::character varying,
    error_message text COLLATE pg_catalog."default",
    CONSTRAINT generatednotice_pkey PRIMARY KEY (id)
)

CREATE SEQUENCE IF NOT EXISTS public.improvement_plans_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE TABLE IF NOT EXISTS public.improvement_plans
(
    id bigint NOT NULL DEFAULT nextval('improvement_plans_id_seq'::regclass),
    plan_details character varying(255) COLLATE pg_catalog."default" NOT NULL,
    deadline character varying(255) COLLATE pg_catalog."default" NOT NULL,
    cost_load character varying(255) COLLATE pg_catalog."default" NOT NULL,
    support_dncc character varying(255) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp(0) without time zone,
    updated_at timestamp(0) without time zone,
    bin bigint NOT NULL,
    deleted_at timestamp without time zone
)

NEW + UPDATED CATEGORY FUNCTION [CATEGORY UPDATE QUERY](C:\xampp\htdocs\notes\Notes\2026\DNCC\Catergorybuildingupdate.md "QUERY ")
