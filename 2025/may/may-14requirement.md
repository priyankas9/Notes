## To-Do List (Fixes & Updates)

---

### 📅 Date Handling

* [X] In every date column involving **Proposed Emptying Date** and  **Confirmed Emptying Date** , display the  **Flatpickr trips allocated date** .
* [X] Add new date picker in application edit
* [X] Remove the **Next Emptying Date Period** field entirely.
* [X] Set **Next Emptying Date** to be either **1 year **.

---

### 📝 Application & Status Updates

* [X] Ensure **status updates** save correctly in the application on all relevant actions.
* [X] Add a **Ping button** when the user disagrees with the proposed schedule.
* [X] Change the **Disagree icon** from a trash bin 🗑️ to an ❌ (X mark) in Desludging Schedule module

---

### 📤 Export & Query Updates

* [X] Update the **CSV export query** for the **Desludging Schedule module** to include necessary and updated fields.
* [X] Display **Containment ID** properly in the  **Desludging Schedule module** .

---

### ✅ Validation & Constraints

* [X] Add validation to ensure **Trip Capacity Per Day** can never be `0`.
* [X] Remove any **Next Emptying Date Period** field references in code, UI, and database if applicable of site setting.
* [X] Form validation b y not letting it accept any special charcters and negative vale and vice versa
* [ ] Even if the error is dispalying the form is getting saved . Fix it

---

### ⚙️ Site Settings & Sidebar

* [X] Remove fields from the **Site Settings module** that are no longer in use.
* [X] Fix the **Sidebar page open issue** (active state and page load behavior).
* [X] Rearrange the **Schedule** menu in the sidebar according to the new feedback structure, reintegrating after the  **Feedback module** .

---

### 🗒️ Application Form & Supervisory Assessment

* [X] Remove the **Household Details block** from the  **Application form** .
* [X] Fix the date format of **Supervisory Assessment Date** in the  **Applications table** .
* [X] When the user tries to  **save the application form reschedule** , display the selected **date** properly.
* [X] In the  **Supervisory Assessment filter** , add filters for:
  * [X] Holding Number (House Number)
  * [X] Owner Name
  * [X] Bin Number/Application ID

---

 🔄 Reschedule Generation Modal

* [X] In the  **Reschedule Generation modal** :
  * [X] Add a new  **Confirm Schedule button that leads to application form page** .
  * [X] Remove the  **Next Emptying Date column** .
