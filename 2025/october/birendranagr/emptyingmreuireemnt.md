## 🧾 Emptying Form

**Card View :
Same as before**

> **Form View:**
>
> ---

### 🧩 **Emptying Form Details**

> **Note:** The “Multi Trip” column is not applicable for now.
> Fields marked with **(*)** are mandatory.

| **Field Name**                          | **Description / Behavior**                                                          | **Action Type** | **Validation** | Field display | Trips display fields             | Always fillable |
| --------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------- | -------------------- | ------------- | -------------------------------- | --------------- |
| **Application ID**                      | Unique identifier for the application*(View Only)*                                        | Hidden                | —                   | always        |                                  |                 |
| **Date**                                | Date when the emptying service was provided*(Auto-filled with proposed emptying date)*   | Auto Fill             | —                   | always        |                                  |                 |
| **Reason for Emptying (*)**             | Reason for performing the emptying*(Dropdown or Free Text)*                               | Text Input            | ✅                   | always        |                                  |                 |
| **No. of Trips (*)**                    | Total number of trips made for this emptying service                                      | Numeric Input         | ✅                   | always        |                                  | true            |
| **Sludge Volume (m³) (*)**             | Volume of sludge emptied*(in cubic meters)*                                               | Numeric Input         | ✅                   | always        |                                  | true            |
| **Desludging Vehicle Number Plate (*)** | Vehicle used for desludging*(Dropdown fetched from API)*                                  | Dropdown              | ✅                   | always        |                                  |                 |
| **Disposal Place (*)**                  | Treatment plant / FSTP where sludge is disposed*(Dropdown fetched from API)*              | Dropdown              | ✅                   | always        |                                  |                 |
| **Start Time (*)**                      | Start time of the emptying process                                                        | Time Picker           | ✅                   | always        |                                  | true            |
| **End Time (*)**                        | End time of the emptying process                                                          | Time Picker           | ✅                   | always        |                                  | true            |
| **Receipt Number**                      | Unique receipt number generated after emptying                                            | Text Input            | ✅                   |               | 1 (when the trip s single trip)  |                 |
| **Total Cost (Rs.)**                    | Total cost incurred for the service*(Numeric input)*                                      | Numeric Input         | ✅                   |               | 1 (when the trip s single trip) |                 |
| **House Image**                         | Upload image of the building/location where sludge was emptied*(Camera/File Upload)*      | File Upload           | ✅                   |               | 1 (when the trip s single trip) |                 |
| **Receipt Image**                       | Upload image of the receipt*(Camera/File Upload)*                                         | File Upload           | ✅                   |               | 1 (when the trip s single trip) |                 |
| **Driver Name (*)**                     | Driver of the desludging vehicle*(Dropdown fetched from Vehicle Table)*                   | Dropdown              | ✅                   | always        |                                  |                 |
| **Emptier 1 Name (*)**                  | First emptier involved in the service*(Dropdown fetched from Staff Table)*                | Dropdown              | ✅                   | always        |                                  |                 |
| **Emptier 2 Name**                      | Second emptier involved*(Dropdown fetched from Staff Table)*                              | Dropdown              | —                   | always        |                                  |                 |
| **Comments (if any)**                   | Optional remarks or additional observations                                               | Text Area             | —                   | always        |                                  | true            |
| **Current Trip Count**                  | Always**1** gradually +1 every time in the initial emptying form *(Auto-filled)* | View Only / Auto Fill | —                   | always        |                                  |                 |

**When Current Trip No = No.of Trips**

- Receipt Number
- Total Cost
- House Image
- Receipt Image

---
