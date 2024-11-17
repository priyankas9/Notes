# 2024.10.16 Thursday to-do

---

* remove unnecessary column from cwis
  - check the database and code for it
* zip the dynamically used code 😄
* and the database as well

- Fields to be removed  & used (striked removed):

  **table :  cwis.data_cwis**

  ---

| column              | used                       |
| ------------------- | -------------------------- |
| id                  |                            |
| sub_category_id     |                            |
| parameter_id        | y (used for param_list)    |
| assmntmtrc_dtpnt    | y (used for param_details) |
| unit                | y (used for param_details) |
| co_cf               | y (used for param_details) |
| data_value          | y (used for param_details) |
| data_type           | y (used for param_details) |
| sym_no              |                            |
| year                | y                          |
| source_id           |                            |
| heading             |                            |
| label               |                            |
| indicator_code      |                            |
| remark              | y (used for param_details) |
| is_system_generated | y (used for param_details) |
| data_periodicity    | y (used for param_details) |
| formula             |                            |
| answer_type         | y (used for param_details) |
| chart_display       |                            |

**table :  cwis.data_cwis**

---

| column              | used |
| ------------------- | ---- |
| id                  |      |
| category_id         |      |
| sub_category_id     | y    |
| parameter_id        | y    |
| assmntmtrc_dtpnt    | y    |
| unit                | y    |
| sym_no              |      |
| category_title      | y    |
| sub_category_title  |      |
| parameter_title     | y    |
| co_cf               |      |
| data_type           | y    |
| heading             | y    |
| label               | y    |
| indicator_code      | y    |
| parent_id           |      |
| remark              | y    |
| is_system_generated |      |
| data_periodicity    |      |
| formula             |      |
| answer_type         | y    |

---

new minimalist table

| column         | datatype           | description                              |
| -------------- | ------------------ | ---------------------------------------- |
| id             | integer            | unique identifiable number               |
| indicator_code | varchar            | includes codes like eq-1, and vice versa |
| label          | varchar            | main title of each indicator             |
| value          | varchar or integer | stores calculated for each indicator     |
| year           | varchar            | stores different year                    |

# 2024.10.25 Friday To-do

---

- ~~finish making cwis dashboard chart static and cwis generator static finish

# 2024.11.05 Tuesday To-do

---

- ~~cwis add button changes~~
- code clean up like remove the stsically calle j query cdn
- make every iss module same as tax iss
- add sample data in the place of iss module sample import excel file
  **Column to be added
  watersupply iss  -> bin
  swm iss ->tax code**
- runed query : ALTER TABLE swm_info.swmservice_payments
  RENAME COLUMN bin TO tax_code;
- AlterTableswm_info.swmservice_payment_status Add COLUMN tax_code character varying(50)
- 

# 2024.11.14 Thursday To-do

---

- ~~add cwis new indicator in docs,seeder~~
- finish the chart thing
- ~~mobile dev stuff~~
- ~~mobile source code as well~~

# 2024.11.15 Friday To- do

---

- chart finish -> just display above and below  & legend label should be limited
- jira issues fixatiotn

# 2024.11.17 Sunday To-do

---

- chart -> tool tip fixation
- display of chart in infop for buildings
- on load pop up
- cwis -> nan na hunda no percent display
- firday requirement pdf
- cwis pdf
