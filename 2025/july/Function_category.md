CREATE OR REPLACE FUNCTION update_toilet_categories_from_sanitation_only()
RETURNS void AS

BEGIN
    -- WASA Sewerage Connection
    UPDATE building_info.buildings
    SET category = 'WASA Sewerage Connection'
    WHERE (category IS NULL OR category = '')
      AND sanitation_system_id = 1;

    -- Directly Connected to Drain
    UPDATE building_info.buildings
    SET category = 'Directly Connected to Drain'
    WHERE (category IS NULL OR category = '')
      AND sanitation_system_id IN (2, 7, 8);

    -- Non-Functional Septic Tank
    UPDATE building_info.buildings
    SET category = 'Non-Functional Septic Tank'
    WHERE (category IS NULL OR category = '')
      AND sanitation_system_id = 4;

    -- Onsite Treatment
    UPDATE building_info.buildings
    SET category = 'Onsite Treatment'
    WHERE (category IS NULL OR category = '')
      AND sanitation_system_id IN (5, 6);

    -- Uncategorized
    UPDATE building_info.buildings
    SET category = 'Uncategorized'
    WHERE (category IS NULL OR category = '')
      AND sanitation_system_id IN (9, 10, 11, 12);
END;
$$ LANGUAGE plpgsql;

SELECT update_toilet_categories_from_sanitation_only();

SELECT update_toilet_categories_from_sanitation_only();
