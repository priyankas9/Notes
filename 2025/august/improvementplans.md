# Db chnages 

---

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
    bin bigint NOT NULL

)

# Code 

---

php artisan vendor:publish --provider="SimpleSoftwareIO\QrCode\QrCodeServiceProvider"
