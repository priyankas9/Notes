current imis-base dev building :


    bin varchar(254) NOTNULL,

    building_associated_to varchar(254),

    ward integer,

    road_code varchar(254),

    house_number varchar,

    house_locality varchar,

    tax_code varchar(254),

    structure_type_id integer,

    surveyed_date date,

    floor_count numeric,

    construction_year date,

    functional_use_id integer,

    use_category_id integer,

    office_business_name varchar(254),

    household_served integer,

    population_served integer,

    male_population integer,

    female_population integer,

    other_population integer,

    diff_abled_male_pop integer,

    diff_abled_female_pop integer,

    diff_abled_others_pop integer,

    low_income_hh boolean,

    lic_id integer,

    water_source_id integer,

    watersupply_pipe_code varchar(255),

    water_customer_id varchar,

    well_presence_status boolean,

    distance_from_well numeric,

    swm_customer_id varchar,

    toilet_status boolean,

    toilet_count integer,

    household_with_private_toilet integer,

    population_with_private_toilet integer,

    sanitation_system_id integer,

    sewer_code varchar(254),

    drain_code varchar(254),

    desludging_vehicle_accessible boolean,

    geom public.geometry,

    verification_status boolean,

    estimated_area numeric(10,2),

    user_id integer,

    created_at timestampwithouttimezone,

    updated_at timestampwithouttimezone,

    deleted_at timestampwithouttimezone,
