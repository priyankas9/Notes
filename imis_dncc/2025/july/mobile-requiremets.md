# 📱 DNCC - Mobile App Requirements

---

## 📝 Supervisory Assessment

---

> **Form View:**
>
> Card Box Name: Supevisory Assessment
>
> Application List Displays following information:
> Application ID:
> Supervisory Assessment Date:
>
> Owner Information (Name, Gender, Contact)-> iF NULL, SHOW Applicant information
>
> Building Location Information (BIN,Ward, Area Name, Block Number, Road Number, House Number)
>
> Action Buttons
>
> Phone Call Button
>
> View Building Location on Google Map
>
> Update Building Information Button (Building Icon preferred)
>
> Fill Supervisory Assessment Button (Assessment or questionnaire icon preferred))

Supervisory Assessment Form

Fetch the pre-existing form from DNCC for supervisory assessment and  **update the fields as follows** :

Note: Please group all collapsable fields into one card/group

| Field Name                                    | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Area Name                                     | View Only/ Collapsed at First Load and can be expanded if needed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Block Number                                  | View Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Road Number / Road Name                       | View Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Road Code                                     | View Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Building Number                               | View Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Owner Name                                    | View Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Owner Gender                                  | View Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Owner Contact                                 | View Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Toilet Presence*                              | Dropdown based on IMIS/ Prefilled via API can be updated<br />Note: Please follow the logic in Edit Building Page Logic and Structure. <br />If Building has Toilet Presence Yes and Building Toilet Connection as Septic or Pit/Holding, separate card should be present showing info about containment<br />Card should have two actions and one button. <br />Actions: Edit Containment Information/ Delete Containment Connection<br />Button: Add Containment button<br />Containment fields:<br />Containment Type (M)<br />(Sewer Code, Drain Code(NM))<br />Volume (M)<br />Construction Date (M)<br />Location (NM) |
| Building Toilet Connection*                   | Dropdown / Based on IMIS / Prefilled via API                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Containment Type                              | Same logic as "Building Add" form → Prefilled if exists, else blank (in separate card mentioned above for Add/ Edit form)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Containment Volume (m³)                      | Mandatory if containment exists (in separate card mentioned above for Add/ Edit form)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Containment Construction Date*                | Mandatory if containment exists (in separate card mentioned above for Add/ Edit form)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Road Width (m)*                               | Numeric valuses                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Distance from Nearest Road Motorable Road(m)* | Input                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Appropriate Desludging Vehicle Size*          | Dropdown from API (DISTINCT DESLUDGING VEHICLE SIZE)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Confirmed Emptying Date*                      | Same logic as implemented in existing app + backend validation-> not allow selection of dates past today                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Advance Paid Amount*                          | Integer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Advance Payment Receipt*                      | Upload Image                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

***Update Building Information Button (Building Icon preferred)***

*Refer to refereneces provided below.*

Mimic same as Edit Building Form, including the Containment Information Card.

---

## 💰 Emptying Form (update to existing form)

---

Card Information:

Application ID:

BIN:

Application Date:

Confirmed Emptying Date:

Owner Information (Name, Gender, Contact)-> iF NULL, SHOW Applicant information

Building Location Information (BIN,Ward, Area Name, Block Number, Road Number, House Number)

Collapsable Section:

Road Width (m)

*Distance from Nearest Road Motorable Road(m)*

*Appropriate Desludging Vehicle*

Containment Size

Action: Call, View on Map, Fill Emptying Information
***Form Chnages :***

Please **update the "Total Cost" section** to contain the following fields:

* **Advance Paid Amount** : *(Prefilled)*
* **Additional Payment** : *(User input; must not be null. Default to 0 if no additional payment)*
* **Total Paid Amount** : *(Prefilled and auto-calculated as `Advance Paid Amount + Additional Payment`)*

---

## 🏗 Building Form

---

**Add a new action** after “Add Supervisory” — called  **Update Building Info** .

* It should be  **an exact replica of the website’s building form** .
  🔗 Reference GitHub Resources
* 🔧 **Main Repository:**

  [https://github.com/dncc-imis/web_app](https://github.com/dncc-imis/web_app)
* 📜 **Building Code Logic:**

  [https://github.com/dncc-imis/web_app/blob/master/public/js/functions.js](https://github.com/dncc-imis/web_app/blob/master/public/js/functions.js)
* 🧩 **Frontend Building Form:**

  [https://github.com/dncc-imis/web_app/tree/master/resources/views/building-info/buildings](https://github.com/dncc-imis/web_app/tree/master/resources/views/building-info/buildings)
* 🚽 **Containment Form + Logic:**

  [https://github.com/dncc-imis/web_app/tree/master/resources/views/fsm/containments](https://github.com/dncc-imis/web_app/tree/master/resources/views/fsm/containments)

### 💻 Backend References

* 🔙 **Building Controller:**

  [https://github.com/dncc-imis/web_app/blob/master/app/Http/Controllers/BuildingInfo/BuildingController.php](https://github.com/dncc-imis/web_app/blob/master/app/Http/Controllers/BuildingInfo/BuildingController.php)
* 🔙 **Containment Controller:**

  [https://github.com/dncc-imis/web_app/blob/master/app/Http/Controllers/Fsm/ContainmentController.php](https://github.com/dncc-imis/web_app/blob/master/app/Http/Controllers/Fsm/ContainmentController.php)
* 🔧 **Building Structure Service:**

  [https://github.com/dncc-imis/web_app/blob/master/app/Services/BuildingInfo/BuildingStructureService.php](https://github.com/dncc-imis/web_app/blob/master/app/Services/BuildingInfo/BuildingStructureService.php)
* 🔧 **Containment Service:**

  [https://github.com/dncc-imis/web_app/blob/master/app/Services/Fsm/ContainmentService.php](https://github.com/dncc-imis/web_app/blob/master/app/Services/Fsm/ContainmentService.php)
