**Site Settings Module Implementation**

### 1. Creation of the Site Settings Module

The **Site Settings** module consists of the following components:

* **Controller** : Manages the logic for handling site settings.
* **Model** : Defines the database structure and interactions.
* **View** : Provides the UI for managing site settings.
* **Service** : Handles business logic and operations related to site settings.

#### Database Table Creation

The following SQL query creates the `sdm_sitesettings` table to store site settings:

```sql
CREATE TABLE IF NOT EXISTS public.sdm_sitesettings (
    id INTEGER NOT NULL GENERATED BY DEFAULT AS IDENTITY (
        INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1
    ),
    name CHARACTER VARYING(255) COLLATE pg_catalog."default" NOT NULL,
    value CHARACTER VARYING(255) COLLATE pg_catalog."default",
    remarks CHARACTER VARYING COLLATE pg_catalog."default",
    data_type CHARACTER VARYING(255) COLLATE pg_catalog."default",
    options CHARACTER VARYING COLLATE pg_catalog."default",
    created_at TIMESTAMP WITHOUT TIME ZONE,
    updated_at TIMESTAMP WITHOUT TIME ZONE,
    deleted_at TIMESTAMP WITHOUT TIME ZONE,
    CONSTRAINT sitesettings_pkey PRIMARY KEY (id)
) TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.sdm_sitesettings
    OWNER TO postgres;
```

#### Data Import

The initial data for the site settings module is provided in a  **CSV file** .

---

### 2. Schedule Desludging Enhancements

#### **Containments Table (`fsm.containments`)**

```sql
ALTER TABLE fsm.containments 
ADD COLUMN priority INTEGER,
ADD COLUMN fstp_distance NUMERIC,
ADD COLUMN closest_fstp_id INTEGER,
ADD COLUMN status INTEGER;
```

#### **Buildings Table (`building_info.building`)**

```sql
ALTER TABLE building_info.building 
ADD COLUMN block_number CHARACTER VARYING COLLATE pg_catalog."default",
ADD COLUMN wasa_status BOOLEAN;
```

---

### 3. Supervisory Assessment Enhancements

```sql
ALTER TABLE fsm.applications 
ADD COLUMN supervisory_assessment_date DATE,
ADD COLUMN supervisory_assessment_status BOOLEAN;
ALTER COLUMN supervisory_assessment_status SET DEFAULT false;
```

### 4.dynamic pdf - business process 5

---

create table :

```
CREATE TABLE IF NOT EXISTS public.pdf_body_data
(
    id bigint NOT NULL DEFAULT nextval('pdf_body_data_id_seq'::regclass),
    subject character varying(255) COLLATE pg_catalog."default" NOT NULL,
    paragraph text COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp(0) without time zone,
    updated_at timestamp(0) without time zone,
    deleted_at timestamp(0) without time zone,
    date character varying COLLATE pg_catalog."default",
    unique_ref character varying COLLATE pg_catalog."default",
    CONSTRAINT pdf_body_data_pkey PRIMARY KEY (id)
)
CREATE SEQUENCE IF NOT EXISTS public.pdf_body_data_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
```

controller , model ,view
