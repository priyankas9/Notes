### From `containments` table:

1. `id` - The unique identifier for each containment
2. `construction_date` - Used to calculate priority if containment hasn't been emptied before
3. `last_emptied_date` - Used to calculate priority based on when it was last emptied
4. `priority` - The calculated priority level (1, 2, or 3)
5. `fstp_distance` - Distance to the nearest FSTP (Faecal Sludge Treatment Plant)
6. `closest_fstp_id` - ID of the nearest FSTP
7. `emptied_status` - Boolean flag indicating if containment has been emptied
8. `status` - Current status of containment (0, 4, or NULL in your query)
9. `next_emptying_date` - The date when the containment should be emptied
10. `geom` - Spatial data for distance calculations
11. `deleted_at` - Soft delete timestamp

### From `building_info.build_contains` (joined table):

1. `containment_id` - Links to containments table
2. `bin` - Building identification number
3. `deleted_at` - Soft delete timestamp

### From `building_info.buildings` (joined table):

1. `bin` - Building identification number (for joining)
2. `wasa_status` - Boolean indicating if WASA bill is paid
3. `deleted_at` - Soft delete timestamp

### From `treatment_plants` table (used in distance calculations):

1. `id` - Treatment plant identifier
2. `type` - Type of treatment plant (FSTP or Co-Treatment Plant)
3. `status` - Active/inactive status
4. `geom` - Spatial data for distance calculations

### From site settings (public.sdm_sitesettings):

1. `Trip Capacity Per Day` - Maximum trips per day
2. `Weekend` - Days considered weekends
3. `Holiday Dates` - Dates considered holidays
4. `Schedule Desludging Start Date` - Starting date for scheduling
5. `Schedule Regeneration Period` - Period for regenerating schedule

### Other fields used in logic:

* `proposed_emptying_date` from applications table (for checking allocated trips)
* `emptying_status` from applications table (for checking allocated trips)
