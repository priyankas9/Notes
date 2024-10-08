# desludging schedule requirements

27.09.2024 friday

## For Button 2

~~Should display pop up form -Done~~
~~same as fsm > Application > add form - Done~~
~~Fetch Applicants detail and Application Details - Done~~
Discard Emerging field
~~Prefill : Proposed Next Emptying date~~

- But if the user wants to change the date they can change

+ vALIDATION :  The user cannot select the date after the proposed emptying date.
  Same as owner tick box
  " All the data should be saved in fsm.application table "

---

Application loss bhayeko dekhinu bayyena :D
-------------------------------------------

Confirm bhayeko data haru fsm.application ma save ani should be removed form the datatable

---

Form fields:
------------

Applicant Details                               Same as owner (checkbox)
------------------------------------------------------------------------

Applicant Name *                   varchar                     applicant_name
Applicant Gender *                 option:m,f,other       applicant_gender
Applicant Contact Number *   integer                     applicant_contact

Application Details
-------------------

Proposed Emptying Date*    Prefilled (date)          proposed_emptying_date
Service Provider Name*      (select option)          service_provider_id
(Fetch service provider name where deleted_at is null)

# 2024.10.06 Sunday Requirement

## Confirm Emptying (pop up form)

- When clicked same as owner do fetch all the seleted owners information
  add new column that displays owner details
  They are:
  Owner Name *             varchar                     owner_name
  Owner Gender *           option:m,f,other      owner_gender
  Owner Contact *           integer                    owner_contact
- ***LOGIC : Only display the field when smae as owner checkbox is clicked :)**
  ***Issue : Fix proposed emptying -> date should be displayed as input type and prefilled value vanda before wala date halnu paryo** *
  and do add a loading buffer when trying to reschedule the desludging vehicle# 2024.10.07 Monday Requirement
- add new column in containment
  status varchar
  sample data : 1 if confirm emptying is done
  2 if disagree
  - disagree button name: Disagree
- once the user hits the button we remove the records 😄
