# 2025.04.10 To-do till next week mid

---

### ✅ Confirm Emptying → Application Form Flow

* [X] When clicking on the **Confirm Emptying** button in  *Reschedule* :
  * [X] Trigger **Add Application Form** submission.
  * [X] In the Application Form, add new fields:
    * [X] `supervisory_assessment_date`
    * [X] `proposed_emptying_date` (if not already present)
    * [X] `emergency_desludging` (optional, not required field)

---

### 📅 Reschedule Calendar (New UI Needed)

* [X] Search for a new **calendar component** (e.g., Flatpickr, FullCalendar) that:
  * [X] Displays **available slots**
  * [X] Shows **available dates** (based on site logic)
  * [X] **Disables holidays and weekends**
  * [X] **Highlights important dates**
  * [X] Uses values from **site settings** (`holiday_list`, `weekends`, etc.)

---

### 🗓️ Desludging Schedule Module

* [X] Display the **day of the week** in brackets next to the date

  Example: `2025-04-12 (Saturday)`

---

### 📄 Application Module Logic

* [X] Disable the **Emptying button** if the user is eligible to use **Supervisory Assessment**
* [ ] Disable **edit access** to the application if the user **cannot use** Supervisory Assessment

---

### 🧑‍💼 Supervisory Assessment Role

* [ ] Create a new role: `Municipality Conservancy Inspector`
* [ ] Assign proper permissions for supervisory assessment actions

---

### 🚨 Final Checklist

* [X] Ensure **date picker or calendar** is fully functional with:
  * Site setting validations (weekends, holidays)
  * Slot logic
* [ ] All **form validations** in Application Form are in place
* [X] All **role restrictions** (enable/disable UI) are enforced
* [ ] Test everything thoroughly — QA before mid-week next week
* [ ] Fix bugs immediately and re-test

# 2025.04.21 Code changes

---

* [ ] application -> add application -> flat pickr for dates
* [ ] data table dates -> editable and deletable
* [ ] display of holiday and weekend ( in calender and schedule desludging datatable 😄
