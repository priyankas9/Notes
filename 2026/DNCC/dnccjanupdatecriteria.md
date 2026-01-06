# **Schedule Desludging QA Roadmap** 

***JIRA Ticket -> [DNCC-2371](https://jira.innovativesolution.com.np/browse/DNCC-2371)***

---

### **1. Building Must Be Active**

* Only buildings that are **active** are considered
* Deleted or inactive buildings must **never** appear in the list

**QA check**

* Deleted buildings should not show up after regeneration

---

### **2. Building Must Have a Linked Containment**

* A building must be **mapped to a containment**
* Buildings without any containment link must be excluded

**QA check**

* Buildings without containment should not appear in the schedule

---

### **3. Containment Must Be Valid**

* Only valid containments are considered
* Containments that are:
  * Rejected
  * Invalid
  * Or explicitly marked as unusable

    must not appear

**QA check**

* Buildings linked to invalid or rejected containments should not appear

---

### **4. Building Must Not Be Under Active Desludging**

* If a building’s containment already has an  **ongoing desludging application** , it must be excluded
* This prevents duplicate or overlapping desludging activities

**QA check**

* Buildings currently under desludging should not appear in the list

---

### **5. Ownership Information Handling**

* If owner details exist, they are shown
* If owner details are missing:
  * Respondent details are shown instead
  * A `*` is displayed to indicate respondent data

**QA check**

* Respondent name/contact shows with `*` when owner is missing

---

### **6. Ward-Based Service Provider Filtering**

* Each service provider is assigned one or more wards
* Only buildings **within those wards** are eligible

**QA check**

* Buildings from wards **outside** the service provider’s service area must not appear

---

### **7. Role-Based Visibility**

* **Super Admin**
  * Can see buildings from **all service providers**
  * Can see the **Service Provider Name** column
* **Service Provider Admin / Other Users**
  * Can see only buildings related to **their own service provider**
  * Service Provider Name column is hidden

**QA check**

* Service Provider Admin must never see data from another provider

---

## 🧪 Additional QA Validation Scenarios

### **Scenario: Building Without Containment**

* A building exists but has no containment mapping
* **Expected:** Building does not appear in schedule

---

### **Scenario: Building With Active Desludging**

* A building has an ongoing desludging application
* **Expected:** Building does not appear in schedule

---

### **Scenario: Invalid Containment**

* Building has containment marked as invalid/rejected
* **Expected:** Building does not appear in schedule

---

### **Scenario: Mixed Ownership Data**

* Building has no owner but has a respondent
* **Expected:** Respondent name & contact shown with `*`

---

### **Scenario: Ward Mismatch**

* Building exists but is outside service provider ward list
* **Expected:** Building does not appear

---

## ✅ Updated Acceptance Criteria (Summary)

* [ ] Only active buildings appear
* [ ] Only buildings with valid containments appear
* [ ] No building under active desludging appears
* [ ] Ward-based filtering is enforced
* [ ] Role-based visibility works correctly
* [ ] Owner/Respondent display rules are followed
* [ ] Filters work correctly in the table
