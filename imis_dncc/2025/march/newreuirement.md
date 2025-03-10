# 2025.03.09 Sunday

---

**Fix this on the Schedule Desludging page:**

* When clicking on the *Confirm Emptying* action, hide the main form initially and display three buttons first.
* When a user selects the *Confirm* button, display the form but first show a message: *"You have selected the proposed emptying date set by the system."*
* If the user clicks on  *Reschedule* , display the form but allow the *Proposed Emptying Date* to be changed.
* If the user selects the *Disagree* button, do not display the form.
* Add a new label,  *Supervisory Assessment Date* , before the  *Proposed Emptying Date* .

In the **Application** table, add new columns: **Supervisory Assessment Date** and **Supervisory Assessment Status** in the **datatable** as well, similar to the **Emptying** table.

In the **Supervisory Assessment Status** column, when clicking on the icon button, display an **edit form** with **pre-filled values** from the  **database** .

# New column added 

---

- **Table : fsm.applications
  supervisory_assessment_date date   Supervisory Assessment Date**
- query : Alter table fsm.applications Add column supervisory_assessment_date date
- Alter table fsm.applications Add column supervisory_assessment_status boolean
