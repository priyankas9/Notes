## 🧾 Emptying Form

**Card View :
Same as before** 

> **Form View:**
>
> ---

### 🧩 **Emptying Form Details**

> **Note:** Ignore “Multi Trip” column for now.

| **Field Name**                      | **Action / Behavior**                                                                                     |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Application ID**                  | Identifier for the application*(View Only)*                                                                     |
| **Date**                            | The date when the emptying service was provided*(Date Picker)*                                                  |
| **Service Receiver Name**           | Name of the person who was present at time of emptying*(Prefilled via Application Table → Editable if needed)* |
| **Service Receiver Gender**         | Gender of service receiver*(Dropdown: Male/Female/Other)*                                                       |
| **Service Receiver Contact Number** | Contact number of the service receiver*(Input, numeric)*                                                        |
| **Reason for Emptying**             | The reason for which the containment was emptied*(Dropdown/Free Text)*                                          |
| **Sludge Volume (m³)**             | Volume of sludge emptied*(Numeric, Mandatory)*                                                                  |
| **Desludging Vehicle Number Plate** | Dropdown - Identifier for the desludging vehicle used for emptying*(Fetch from API)*                            |
| **Disposal Place**                  | Dropdown - Treatment plant where sludge will be disposed*(Fetch from API)*                                      |
| **Start Time**                      | Start time of the emptying process*(Time Picker)*                                                               |
| **End Time**                        | End time of the emptying process*(Time Picker)*                                                                 |
| **Receipt Number**                  | Identifier for the receipt generated after emptying*(Input)*                                                    |
| **Total Cost**                      | Total cost of the emptying process*(Numeric)*                                                                   |
| **House Image**                     | Upload Image - of the building/location where sludge was emptied*(Camera/File Upload)*                          |
| **Receipt Image**                   | Upload Image - of the generated receipt*(Camera/File Upload)*                                                   |
| **Driver Name**                     | Dropdown - Select driver of desludging vehicle*(Fetch from Vehicle Table)*                                      |
| **Emptier 1 Name**                  | Dropdown - First person involved in emptying*(Fetch from Staff Table)*                                          |
| **Emptier 2 Name**                  | Dropdown - Second person involved in emptying*(Fetch from Staff Table)*                                         |
| **Comments (if any)**               | Free text input for any additional observations*(Optional)*                                                     |

---

### 🧠 **Validation Logic**

* **Mandatory Fields:**
  * Date
  * Sludge Volume (m³)
  * Desludging Vehicle Number Plate
  * Disposal Place
  * Start Time, End Time
* **Image Upload:** At least one of *House Image* or *Receipt Image* required.
* **Date Validation:** Cannot select future dates.
* **Numeric Fields:** Sludge Volume, Total Cost must accept only positive numeric values.
