ue columns prescreate a doc for teh new project setup

deply in new port

# 16 th feb Sunday

---

-> finish transfer of code in the dncc code base

-> make necessary changes in the query for get all in dncc code

->rename the column name in the get all query

## changed column mapping:

block_number -> house_number ????
area_name -> house_locality
road_number -> road_code
~~status~~

# Added Columns

block number in buildings
fstp distance and priority in containments
status -> containments

# 18th feb Tuesday

---

docs follow garera business process follow docs

# 19th feb Wedneday

---

Follow docs and start completing the business process 1
fields present in old imis dncc table

| **Column Name** | **Data Type** |
| --------------------- | ------------------- |

| `no_hh_shared_toilet` | `integer` |
| ----------------------- | ----------- |

| `population_shared_toilet` | `integer` |
| ---------------------------- | ----------- |

| `toilet_for_security` | `integer` |
| ----------------------- | ----------- |

| `security_guard_count` | `integer` |
| ------------------------ | ----------- |

| `discharge_points` | `integer` |
| -------------------- | ----------- |

| `temp_functional_use_id` | `varchar` |
| -------------------------- | ----------- |

| `temp_use_category_id` | `varchar` |
| ------------------------ | ----------- |

| `remarks` | `text` |
| ----------- | -------- |

| `discharge_line` | `varchar` |
| ------------------ | ----------- |

| `sullage_graywater_outlet` | `varchar` |
| ---------------------------- | ----------- |

| `connected_road_width` | `numeric` |
| ------------------------ | ----------- |

| `building_status` | `varchar` |
| ------------------- | ----------- |

| `owner_representative` | `varchar` |
| ------------------------ | ----------- |

| `address` | `varchar` |
| ----------- | ----------- |

| `house_number_survey` | `varchar` |
| ----------------------- | ----------- |

| `road_number` | `varchar` |
| --------------- | ----------- |

| `area_name` | `varchar` |
| ------------- | ----------- |

| `wasa_status` | `varchar` |
| --------------- | ----------- |

| `water_status` | `varchar` |
| ---------------- | ----------- |

| `wasa_bill_no` | `varchar` |
| ---------------- | ----------- |

| `septic_tank_status` | `varchar` |
| ---------------------- | ----------- |

| `respondent_name` | `varchar` |
| ------------------- | ----------- |

| `respondent_contact` | `bigint` |
| ---------------------- | ---------- |

| `respondent_email` | `varchar` |
| -------------------- | ----------- |

| `respondent_gender` | `varchar` |
| --------------------- | ----------- |

| `respondent_identification` | `varchar` |
| ----------------------------- | ----------- |

# 20.02.2025 Thursday

---

- add the new column in the building table and update the get all function
- added wasa_status varchar for now in new dncc
  ************Task to be done for further days:**
  *Confirmation of the emptying date*
  ***Disagree*
  *Request for reschedule****.
  ****Agree*****

# 21.02.2024 Friday

---

- Disagree

### **UI Implementation:**

* **Cross Icon Behavior:**

  * Normal (default state) → No disagreement
  * **Orange (pending renotification)** → First disagreement
  * **Remove from table (if disagrees again)** → Second disagreement
* **DataTable Handling:**

  * Show all buildings in the desludging schedule, including those that disagreed once (with orange cross).
  * If the owner disagrees again, remove the record from the table dynamically via AJAX.

  **Rough Sketch**
* fetch those with null status and single desludged
* after the user clicks on the disagree button fsm.containments status upgrades to 1 and it displays You will be renotified after some days and the sttaus 1 data should be displayed in different view and the button has that have certain  ping and once again if the user click on the disagree button then the record will get removed with sstas 2 and then the record should be removed form schedule desludging table

# 23.02.2024 Sunday

---

- update the disagree emptying function
  - when user disagrees or clicks the button first the status colmn should store 1
  - when user disagree for the second time here the status column should store 2
- all those record where the status have status 1 there shold be the disagree button with a ping
