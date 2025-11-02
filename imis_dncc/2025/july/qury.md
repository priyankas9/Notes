-- WASA Sewerage Connection
SELECT COUNT(*) AS wasasewerageconnection
FROM building_info.buildings
WHERE category = 'WASA Sewerage Connection'
  AND deleted_at IS NULL;

-- Directly Connected to Drain
SELECT COUNT(*) AS directlydrain
FROM building_info.buildings
WHERE category = 'Directly Connected to Drain'
  AND deleted_at IS NULL;

-- Non-Functional Septic Tank
SELECT COUNT(*) AS nonfunctionalseptictank
FROM building_info.buildings
WHERE category = 'Non-Functional Septic Tank'
  AND deleted_at IS NULL;

-- Functional Septic Tank
SELECT COUNT(*) AS functionalseptictank
FROM building_info.buildings
WHERE category = 'Functional Septic Tank'
  AND deleted_at IS NULL;

-- Onsite Treatment
SELECT COUNT(*) AS onsitetreatment
FROM building_info.buildings
WHERE category = 'Onsite Treatment'
  AND deleted_at IS NULL;

ALTER TABLE building_info.buildings
RENAME COLUMN "toilet_category" TO category;

ALTER TABLE building_info.buildings
DROP COLUMN containment_category

CREATE OR REPLACE FUNCTION update_toilet_categories()
RETURNS void AS $$
BEGIN
    -- Sewer Network
    UPDATE building_info.buildings b
    SET toilet_category = 'WASA Sewerage Connection'
    WHERE sanitation_system_id = 1
      AND (toilet_category IS NULL OR toilet_category = '');

    -- Drain Network, Water Body, Open Ground
    UPDATE building_info.buildings b
    SET toilet_category = 'Directly Connected to Drain'
    WHERE sanitation_system_id IN (2, 7, 8)
      AND (toilet_category IS NULL OR toilet_category = '');

    -- Non-Functional Septic Tank
    UPDATE building_info.buildings b
    SET toilet_category = 'Non-Functional Septic Tank'
    WHERE sanitation_system_id = 4
      AND (toilet_category IS NULL OR toilet_category = '');

    -- Onsite Treatment
    UPDATE building_info.buildings b
    SET toilet_category = 'Onsite Treatment'
    WHERE sanitation_system_id IN (5, 6)
      AND (toilet_category IS NULL OR toilet_category = '');

    -- For others, keep existing toilet_category, so no NULL overwrite
END;

$$
LANGUAGE plpgsql;
$$

CREATE OR REPLACE FUNCTION update_toilet_categories_from_sanitation_and_containment()
RETURNS void AS $$
BEGIN
    -- 1. WASA Sewerage Connection
    UPDATE building_info.buildings b
    SET category = 'WASA Sewerage Connection'
    FROM building_info.build_contains bc
    JOIN fsm.containments c ON bc.containment_id = c.id
    WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND (
            b.sanitation_system_id = 1  -- Sewer Network
            OR c.type_id IN (1, 13)     -- Septic Tank / Lined Pit connected to Sewer
          );

    -- 2. Directly Connected to Drain
    UPDATE building_info.buildings b
    SET category = 'Directly Connected to Drain'
    FROM building_info.build_contains bc
    JOIN fsm.containments c ON bc.containment_id = c.id
    WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND b.sanitation_system_id IN (2, 7, 8);  -- Drain, Water Body, Open Ground

    -- 3. Functional Septic Tank
    UPDATE building_info.buildings b
    SET category = 'Functional Septic Tank'
    FROM building_info.build_contains bc
    JOIN fsm.containments c ON bc.containment_id = c.id
    WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND c.type_id IN (3);  -- Soak Pit

    -- 4. Non-Functional Septic Tank
    UPDATE building_info.buildings b
    SET category = 'Non-Functional Septic Tank'
    FROM building_info.build_contains bc
    JOIN fsm.containments c ON bc.containment_id = c.id
    WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND (
            b.sanitation_system_id = 4  -- Pit/Holding Tank
            OR c.type_id IN (2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17)
          );

    -- 5. Onsite Treatment
    UPDATE building_info.buildings b
    SET category = 'Onsite Treatment'
    FROM building_info.build_contains bc
    JOIN fsm.containments c ON bc.containment_id = c.id
    WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND b.sanitation_system_id IN (5, 6);  -- Onsite Treatment & Composting

END;


$$
LANGUAGE plpgsql;

SELECT update_toilet_categories_from_sanitation_and_containment();
$$
