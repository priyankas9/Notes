# THIS FILE ONY FOCUSES ON UPDATING CATEGORY OF BULDING BASED ON SANITATION AND CONTAINMENT TYPE 

---

## Count 

---



-- WASA Sewerage Connection
SELECT COUNT(*) AS wasasewerageconnection
FROM building_info.build_contains bc
JOIN fsm.containments c ON bc.containment_id = c.id
JOIN building_info.buildings b ON bc.bin = b.bin
WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND (
            b.sanitation_system_id = 1  -- Sewer Network
            OR c.type_id IN (1, 13)     -- Septic Tank / Lined Pit connected to Sewer
          )
  AND deleted_at IS NULL;

-- Directly Connected to Drain
SELECT COUNT(*) AS directlydrain
FROM building_info.build_contains bc
JOIN fsm.containments c ON bc.containment_id = c.id
JOIN building_info.buildings b ON bc.bin = b.bin
WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND b.sanitation_system_id IN (2, 7, 8);

-- Non-Functional Septic Tank
SELECT COUNT(*) AS nonfunctionalseptictank
FROM building_info.build_contains bc
JOIN fsm.containments c ON bc.containment_id = c.id
JOIN building_info.buildings b ON bc.bin = b.bin
WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND (
            b.sanitation_system_id = 4  -- Pit/Holding Tank
            OR c.type_id IN (2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17)
          );

-- Functional Septic Tank
SELECT COUNT(*) AS functionalseptictank
FROM building_info.build_contains bc
JOIN fsm.containments c ON bc.containment_id = c.id
JOIN building_info.buildings b ON bc.bin = b.bin
 WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND c.type_id IN (3);  -- Soak Pit

-- Onsite Treatment
SELECT COUNT(*) AS onsitetreatment
FROM building_info.build_contains bc
JOIN fsm.containments c ON bc.containment_id = c.id
JOIN building_info.buildings b ON bc.bin = b.bin
 WHERE b.bin = bc.bin
      AND (b.category IS NULL OR b.category = '')
      AND b.sanitation_system_id IN (5, 6);  -- Onsite Treatment & Composting


## UPDATE 

---



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
