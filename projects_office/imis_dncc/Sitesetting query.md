# Sitesetting query

CREATE TABLE sitesettings(
    id SERIAL NOT NULL,
    name varchar(255) NOT NULL,
    "value" varchar(255),
    remarks varchar,
    data_type varchar(255),
    options varchar,
    created_at timestamp without time zone,
    updated_at timestamp without time zone,
    deleted_at timestamp without time zone,
    PRIMARY KEY(id)
);

# insert data query
