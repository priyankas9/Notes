# to-do 

- export feature add for desludging schedule - Done
- regenrate buttone by hitting the set emptying function 
  - button name Regnerate Next Emptying Date
  --features: page refresh
- check miro and complete the made function now  
- pass sql query for site setting table craetion 
- add extra buttons for schedule desludgong 
- check copy for more details to do for site settings 
- db new task ask maharshi 
- check miro board
------------------------------------------------------------------------------------------
## to-do thursday 2024.09.26
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
--------------------------------------------------------------------------------------
## to-do friday 2024.09.27
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
-------------
Applicant Details                               Same as owner (checkbox)
----------------------------------------------------------------------------------------------
Applicant Name *             varchar                applicant_name
Applicant Gender *           option:m,f,other       applicant_gender
Applicant Contact Number *   integer                applicant_contact
Application Details
-----------------------------------------------------------------------------------------------
Proposed Emptying Date*    Prefilled (date)          proposed_emptying_date
Service Provider Name*      (select option)          service_provider_id
(Fetch service provider name where deleted_at is null)
-----------------------------------------------------------------------------------------------
## to-do  Sunday 29.09.2024
- make a route to submit the pop up form  (fsm.application) table  - Done
- make a corresponding form for it  - Done
- Fetch service provider name where deleted_at is null -Done 
  (style should be fixed) - Done
- prefill proposed emptying input if there are data
- Make the record not to get displayed in the datatable after the record has been successfully saved :) - Ask maharshi about it 
 and also ask about the same as owner :)