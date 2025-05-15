
## To-Do List (Fixes & Updates)

---

### 📅 Date Handling

* In every date column involving **Proposed Emptying Date** and  **Confirmed Emptying Date** , display the  **Flatpickr trips allocated date** .
* Remove the **Next Emptying Date Period** field entirely.
* Set **Next Emptying Date** to be either **1 year **.

---

### 📝 Application & Status Updates

* Ensure **status updates** save correctly in the application on all relevant actions.
* Add a **Ping button** when the user disagrees with the proposed schedule.
* Change the **Disagree icon** from a trash bin 🗑️ to an ❌ (X mark) in Desludging Schedule module

---

### 📤 Export & Query Updates

* Update the **CSV export query** for the **Desludging Schedule module** to include necessary and updated fields.
* Display **Containment ID** properly in the  **Desludging Schedule module** .

---

### ✅ Validation & Constraints

* Add validation to ensure **Trip Capacity Per Day** can never be `0`.
* Remove any **Next Emptying Date Period** field references in code, UI, and database if applicable of site setting.

---

### ⚙️ Site Settings & Sidebar

* Remove fields from the **Site Settings module** that are no longer in use.
* Fix the **Sidebar page open issue** (active state and page load behavior).
* Rearrange the **Schedule** menu in the sidebar according to the new feedback structure, reintegrating after the  **Feedback module** .

---

### 🗒️ Application Form & Supervisory Assessment

* Remove the **Household Details block** from the  **Application form** .
* Fix the date format of **Supervisory Assessment Date** in the  **Applications table** .
* When the user tries to  **save the application form reschedule** , display the selected **date** properly.
* In the  **Supervisory Assessment filter** , add filters for:
  * Holding Number (House Number)
  * Owner Name
  * Bin Number

---

### 🔄 Reschedule Generation Modal

* In the  **Reschedule Generation modal** :

  * Add a new  **Confirm Schedule button** .
  * Remove the  **Next Emptying Date column** .
