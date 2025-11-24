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

| **Field Name**              | **Action / Behavior**                                            | Required | State    |
| --------------------------------- | ---------------------------------------------------------------------- | -------- | -------- |
| **Application ID**          | Prefilled, View Only                                                   | TRUE     | Disabled |
| **Treatment Plant Name**    | Prefilled, View Only                                                   | TRUE     | Disabled |
| **Sludge Volume (m³)**     | Prefilled, View Only                                                   | TRUE     | Dsabled  |
| **Date**                    | Date Picker – Date of sludge disposal*(Cannot select past dates)*    | TRUE     |          |
| **Entry Time**              | Time Picker – Entry time of vehicle into treatment plant*(Mandatory)* | TRUE     |          |
| **Exit Time**               | Time Picker – Exit time of vehicle from treatment plant*(Mandatory)*  | TRUE     |          |
| **Tipping Fee Receipt No.** | Input – Identifier for tipping fee receipt*(Optional)*                | TRUE     |          |
| **Tipping Fee Amount**      | Auto-fetched backend field*(Read-only)*                                | TRUE     |          |

---
