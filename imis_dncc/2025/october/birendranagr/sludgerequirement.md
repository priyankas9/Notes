## 🚚 Sludge Collection Service

> **Form View:**
>
> **Card Box Name:** Sludge Collection Service
>
> **Card Icon:** *(Recommended — truck or sludge-tank-related icon)*
>
> **Purpose:**
>
> This module lists sludge collection (emptying) details for each service, allowing operators to view essential information and fill out the **Sludge Disposal Form** for each application.

---

### 📋 **Application List Card Displays Following Information:**

when emptying_status = 1 or 2 and when sludge_collection_status is 0

**UI Sample :**
![1760525018083](image/sludgerequirement/1760525018083.png)

| **Field Name**                      | **Description / Behavior**                                                                     |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Application ID **                      | Unique identifier for the sludge emptying record*(Collapsible/Expandable)* (same like emptying card) |
| **House Number**                    | Display from building information linked to the application*(View Only)*                             |
| **BIN**                             | Building Identification Number*(View Only)*                                                          |
| **Ward**                            | Ward number*(View Only)*                                                                             |
| **Service Provider Contact Number** | Phone number of service provider*(Clickable → opens dialer)*                                        |
| **Vehicle Plate Number**            | Desludging vehicle plate number used*(Prefilled from Emptying Form)*                                 |
| **Sludge Volume (m³)**             | Volume of sludge emptied*(Prefilled from Emptying Form)*                                             |
| **Emptied Date**                    | Date when the sludge was collected*(Prefilled)*                                                      |
| **Action (Only Form)**              | Button → Opens**Sludge Disposal Form**for this record*(Disposal Icon preferred: 🏭 or ♻️)*  |

---

### 🧾 **Sludge Disposal Form (Inside the Card)**

> **Card Box Name:** Sludge Disposal Form
>
> **Parent Card:** Sludge Collection Service

| **Field Name**                | **Action / Behavior**                                                               | Required | State    |
| ----------------------------------- | ----------------------------------------------------------------------------------------- | -------- | -------- |
| **Application ID**            | Prefilled, View Only , Input hidden                                                       | TRUE     | Disabled |
| **Treatment Plant Name**      | Prefilled, View Only                                                                      | TRUE     | Disabled |
| **Sludge Volume (m³)**       | Prefilled, View Only                                                                      | TRUE     | Dsabled  |
| **Date**                      | Date Picker – Date of sludge disposal*(Cannot select future dates)*                      | TRUE     |          |
| **Entry Time**                | Time Picker – Entry time of vehicle into treatment plant*(Mandatory)*                    | TRUE     |          |
| **Exit Time**                 | Time Picker – Exit time of vehicle from treatment plant*(Mandatory)*                     | TRUE     |          |
| **Tipping Fee Receipt No.**   | Input – Identifier for tipping fee receipt*(Optional)*                                   | TRUE     |          |
| **Tipping Fee Amount**        | Auto-fetched backend field*(Read-only)*                                                   | TRUE     |          |
| **Tipping Fee Receipt Image** | Upload Image*(Camera/File Upload)*                                                        | TRUE     |          |
| **Last Trip?**                | Toggle (Yes/No) – Indicates if more trips are expected for this application*(Mandatory)* | TRUE     |          |

---

### ⚙️ **Action Buttons**

| **Button**                           | **Functionality**                                    |
| ------------------------------------------ | ---------------------------------------------------------- |
| **📞 Call Provider**                 | Opens dialer using service provider’s contact number.     |
| **🚛 Fill Disposal Form**            | Opens the Sludge Disposal Form under selected application. |
| **💾 Save / Submit Disposal Record** | Validates required fields and submits disposal details.    |

---

### 🧠 **Validation Logic**

* **Mandatory Fields:**
  * Treatment Plant Name
  * Sludge Volume (m³)
  * Date
  * Entry Time, Exit Time
  * Last Trip?
* **Date Validation:** Future dates not allowed.
* **Numeric Fields:** Sludge Volume must be a positive number.
* **Tipping Fee Amount:** Auto-filled (read-only).
* **Image Upload:** Optional but recommended.

---

### 🧱 **UI/UX Notes**

* Two Levels of Cards:
  1. **Sludge Collection Service Card (🚚)** – lists collection details
  2. **Sludge Disposal Form Card (🏭)** – accessible via Action button
* **Use consistent icons** for navigation clarity:
  * 🚚 Sludge Collection
  * 🏭 Disposal
  * 💾 Save
  * 📞 Call
* **Expandable Card Behavior:**
  * Application ID row collapses/expands to show full details.
  * Inside expansion, action button “Fill Disposal Form” appears.
* On successful submission, show toast/snackbar:
  > ✅ *Disposal details saved successfully.*
  >
