
## 📑 QA Test Plan: **Desludging Management System**

---

### 📌 **Module: Site Settings**

**Objective:**

Verify site setting configurations are saved and functional for downstream modules.

**Test Steps:**

* Open the **Site Settings** module.
* Fill in all required fields:
  * Trip Capacity Per Day
  * Schedule Desludging Start Date
  * Weekend Days
  * Holiday Dates
  * Multi-select fields for Wards (if applicable)
  * and so

**Expected Outcome:**

* Form should successfully save without errors.
* Multi-select fields should function correctly, allowing multiple values to be selected and saved.

---

### 📌 **Module: Desludging Schedule**

**Objective:**

Validate desludging scheduling based on site settings and system constraints.

**Test Steps:**

* Open **Desludging Schedule** module.
* Confirm visibility of buildings where:
  * `was_sat` = false
  * Containment status is  **null** ,  **not confirmed** ,  **disagreed emptying** , or **rescheduled**
* Confirm the presence of the following buttons:
  * **Regenerate Desludging Schedule**
  * **Export CSV**

**Expected Outcomes:**

**1️⃣ Regenerate Desludging Schedule:**

* On click, a loading indicator appears.
* Containments get scheduled based on priority and:
  * **Trip Capacity Per Day** from Site Settings.
  * **Start Date** from Site Settings.
  * Weekends and holidays (as per Site Settings) are excluded.
* System generates and displays a new schedule in the datatable.

**2️⃣ Export CSV:**

* Exports a CSV containing the same number of records currently displayed in the datatable.

**3️⃣ Datatable Actions:**

| Action                        | Expected Outcome                                                                                                                                                                                                                                                                                         |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Confirm Emptying**    | Navigates to the**Application Add**page with all inputs prefilled and disabled except required fields. <br />Proposed Emptying Date is non-editable.<br /> Supervisory Assessment Date must be ≤ Proposed Emptying Date.                                                                          |
| **Reschedule Emptying** | Navigates to**Application Add**view. Inputs prefilled and disabled except **Proposed Emptying Date** .<br /> Calendar should show: <br />Trip availability (with color codes)<br />Weekends and holidays highlighted <br /> Supervisory Assessment Date should be ≤ Proposed Emptying Date. |
| **Disagree Emptying**   | On first click, a confirmation (Swal) appears. <br />If confirmed, record remains. <br />On second click, record is removed from**Desludging Schedule**datatable.                                                                                                                                  |

---

### 📌 **Module: Desludging Schedule Reintegration**

**Objective:**

Verify listing and reintegration of containments marked as ‘Disagree Emptying’.

**Test Steps:**

* Open  **Desludging Schedule Reintegration** .
* Confirm visibility of all previously disagreed containments.

**Expected Outcome:**

* All disagreed records appear irrespective of the number of times actioned.

---

### 📌 **Module: Application Add Page**

**Objective:**

Verify correct display of the trip availability calendar and form submission.

**Test Steps:**

* Open the **Application Add** page.
* Confirm calendar view:
  * Displays trip availability per day.
  * Highlights weekends and holidays distinctly.
* Verify form save functionality.

**Expected Outcome:**

* Calendar displays available slots with color-coded indicators.
* Weekends and holidays are highlighted.
* Form saves correctly with all constraints validated.

---

### 📌 **Module: Application Datatable**

**Objective:**

Verify the new supervisory assessment fields and action workflows.

**Test Steps:**

* Open  **Application Datatable** .
* Confirm presence of:
  * Supervisory Assessment Date
  * Supervisory Assessment Status (with action button)

**Expected Outcomes:**

* Values display as saved in the Application form.
* **Supervisory Assessment Status** :
* Initially shown as a cross icon.
* On click, navigates to **Supervisory Assessment Add** page.
* User fills form and saves.
* Post-save, icon updates to a tick and button gets disabled.
* Only after this, the **Emptying Status** button is enabled for action.
