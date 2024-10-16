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
| sub_category_id     |      |
| parameter_id        |      |
| assmntmtrc_dtpnt    |      |
| unit                |      |
| sym_no              |      |
| category_title      |      |
| sub_category_title  |      |
| parameter_title     |      |
| co_cf               |      |
| data_type           |      |
| heading             |      |
| label               |      |
| indicator_code      |      |
| parent_id           |      |
| remark              |      |
| is_system_generated |      |
| data_periodicity    |      |
| formula             |      |
| answer_type         |      |
