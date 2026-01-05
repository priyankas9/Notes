# Queries

---

## 04.Jan 

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
    CONSTRAINT desludging_schedule_temp_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS fsm.desludging_schedule_temp
    OWNER to postgres;

CREATE SEQUENCE IF NOT EXISTS fsm.desludging_schedule_temp_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
    OWNED BY desludging_schedule_temp.id;

ALTER SEQUENCE fsm.desludging_schedule_temp_id_seq
    OWNER TO postgres;
