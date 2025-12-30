# to-do

---

- export feature add for desludging schedule - Done
- regenrate buttone by hitting the set emptying function
  - button name Regnerate Next Emptying Date
    -- features: page refresh
- check miro and complete the made function now
- pass sql query for site setting table craetion
- add extra buttons for schedule desludgong
- check copy for more details to do for site settings
- db new task ask maharshi
- check miro board

---

## to-do thursday 2024.09.26

---

dncc - site settings - DONE
// error : didnot include all the columns before saving
site settings - validation

## Validation to-do :

working hours : 24 max
Next Emotying Date : 1 - 15

### Issue:::: validation fails but still the success message gets displayed :(

++ changed contain_ward column to ward column in fsm.containment table
miro function - compelete (reject count -- left)
regenrate next emptying data compelete -- done almost
-----------------------------------------------------

## to-do friday 2024.09.27

---

sidebar - placement of sitessettings and removal of cwis setting - Done
++ buttons name:
Confirm for Assessment (done)
Confirm Emptying
Re-schedule Emptying Date
Send Job Order for Emptying
++ button color changed
miro - new functions for dncc schedule desludging

- Button 2
- Changed the button name form regnerate next emptying date to regenerate desludging schedule
  make popup form which has fileds for applicants and application details - Done
  make a route
  make function that saves details to fsm.application table
  Form fields: - ui part done

---

### Applicant Details                               Same as owner (checkbox)

### Applicant Name *                     varchar                     applicant_name

Applicant Gender *                  option:m,f,other      applicant_gender
Applicant Contact Number *   integer                     applicant_contact

### Application Details

### Proposed Emptying Date*    Prefilled (date)          proposed_emptying_date

Service Provider Name*       (select option)           service_provider_id

### (Fetch service provider name where deleted_at is null)

## to-do  Sunday 29.09.2024

---

- ~~make a route to submit the pop up form  (fsm.application) table~~
- ~~make a corresponding form for it~~
- ~~Fetch service provider name where deleted_at is null
  (style should be fixed~~)
- prefill proposed emptying input if there are data
- Make the record not to get displayed in the datatable after the record has been successfully saved 😄 - Ask maharshi about it
  and also ask about the same as owner 😄
- validation of prefill proposed_emptying_date : a user cannot change it after the given next emptying date 😄

---

## to-do 9.30.2024 Monday

- Dncc export - couldn't finish it 😢

---

# to-do 10.01.2024 Tuesday

---

- ##### DNCC export

  NEW FIELDS
- Respondent contact, name and wasa status
  FORMAT OF EXCEL
  ![alt text](image.png)
  BACKEND Mapping

---

##### Zone Name - not found

Ward Number - ward
BIN Number - bin
House Owner Name - owner_name(o)
House owner Mobile Number - owner_contact(o)
Structure type - structure_type_id
Number of Floor - floor_count
Number of Toilet - toilet_count
Functional Use - temp_functional_use_id
Empty Status - emptied_status(c)
Sanitation system - sanitation_system_id (s)
Outlet of Containment Connection - type_id (c)
WASA sewer bill status - wasa_status
WASA Bill number - wasa_bill_no
House Number - house_number
Block Number - block_number
Road Name - road_number
Area Name - area_name

# to-do 10.02.2024 Wednesday

---

- dncc work
- gmis - issue resolved fetched from direct table
- ISSUE : Dont display the issue directly to the swal

# to-do 10.07.2024 Monday

---

- finish confirm emptying

  -- same as owner
  ~~Make a form with owner details as:~~
  Owner Name *             varchar                     customer_name
  Owner Gender *           option:m,f,other      customer_gender
  Owner Contact *           integer                    customer_contact

  The main logic behind this is :
  ***To only show this field if there exists owners data***

  -- ~~prefill validation for proposed emptying dat~~e

  - ~~change the input field as date~~ 😉
    - ~~backend function fixation for saving this also update~~

  -- ~~input date fixation~~
- reschedule logic finish
- ADD processing in the datatable after clicking the button 😄

# to-do 10.08.2024 Tuesday

---

- ~~To only show this field if there exists owners data       prefill?~~
- reschedule logic finish
- ADD processing in the datatable after clicking the button 😄
- ~~add new column in containment table as status~~
  - ~~which holds flag on hwther the schedule is emptied or not and 1 if confirm emptying is done
    2 if disagree- disagree button name: Disagree~~
  - ~~Add button in desludging schedule to delete and when this button gets hit status column will get flagged as 2 and confirm emptying gets hit then flag as 1~~
- query runned : [C:\xampp\htdocs\notes\Notes\imis_dncc\query\query.md]()
- ecport to csv select query fixation/update according to the new datatable query 😄

# to-do 10.09.2024 Wednesday

---

- ~~ecport to csv select query fixation/update according to the new datatable query~~ 😄
- ~~prefilled proposed emptying validation~~

# to-do 10.16.2024 Wednesday

---

- finish dncc as per the requirement :
  - ~~rename the button name from disagree for confirm emptying to remove from desludging schedule~~
  - ~~comment the field form sitesetting : Emptying Date Of Period~~
  - ~~add remarks : same as description available at miro board~~
  - add new feature : multi-value input
    (e.g: user needs to have  a value to get inserted multiple value )
  - ~~proposed emptying date validation : remove the validation of user to only select date after not before~~
  - ~~and fix swal for remove button~~
  - ~~remove non-working buttons for desludging schedule 😄~~
  - ~~display owner details and make it non editable~~
  - ~~display details automatically don't just make it function with the checkbox~~
- push in github
- site setting table creation
- switch the database 😄
  (didn't work cause had the table issue and i think the next emptying date data is not available 😢)

# to-do 10.17.2024 Thursday

---

- add new feature : multi-value input
  (e.g: user needs to have  a value to get inserted multiple value )
- added new table site settings in live db
