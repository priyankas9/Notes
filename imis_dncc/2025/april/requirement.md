# 2025.04.10 To-do till next week mid

---

### ✅ Confirm Emptying → Application Form Flow

* [ ] When clicking on the **Confirm Emptying** button in  *Reschedule* :
  * [ ] Trigger **Add Application Form** submission.
  * [ ] In the Application Form, add new fields:
    * [ ] `supervisory_assessment_date`
    * [ ] `proposed_emptying_date` (if not already present)
    * [ ] `emergency_desludging` (optional, not required field)

---

### 📅 Reschedule Calendar (New UI Needed)

* [ ] Search for a new **calendar component** (e.g., Flatpickr, FullCalendar) that:
  * [ ] Displays **available slots**
  * [ ] Shows **available dates** (based on site logic)
  * [ ] **Disables holidays and weekends**
  * [ ] **Highlights important dates**
  * [ ] Uses values from **site settings** (`holiday_list`, `weekends`, etc.)

---

### 🗓️ Desludging Schedule Module

* [ ] Display the **day of the week** in brackets next to the date

  Example: `2025-04-12 (Saturday)`

---

### 📄 Application Module Logic

* [ ] Disable the **Emptying button** if the user is eligible to use **Supervisory Assessment**
* [ ] Disable **edit access** to the application if the user **cannot use** Supervisory Assessment

---

### 🧑‍💼 Supervisory Assessment Role

* [ ] Create a new role: `Municipality Conservancy Inspector`
* [ ] Assign proper permissions for supervisory assessment actions

---

### 🚨 Final Checklist

* [ ] Ensure **date picker or calendar** is fully functional with:
  * Site setting validations (weekends, holidays)
  * Slot logic
* [ ] All **form validations** in Application Form are in place
* [ ] All **role restrictions** (enable/disable UI) are enforced
* [ ] Test everything thoroughly — QA before mid-week next week
* [ ] Fix bugs immediately and re-test
