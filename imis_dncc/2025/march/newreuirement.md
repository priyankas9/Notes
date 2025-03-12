# 2025.03.09 Sunday

---

**Fix this on the Schedule Desludging page:**

* When clicking on the *Confirm Emptying* action, hide the main form initially and display three buttons first.
* When a user selects the *Confirm* button, display the form but first show a message: *"You have selected the proposed emptying date set by the system."*
* If the user clicks on  *Reschedule* , display the form but allow the *Proposed Emptying Date* to be changed.
* If the user selects the *Disagree* button, do not display the form.
* Add a new label,  *Supervisory Assessment Date* , before the  *Proposed Emptying Date* .
* create an enum to store the status

In the **Application** table, add new columns: **Supervisory Assessment Date** and **Supervisory Assessment Status** in the **datatable** as well, similar to the **Emptying** table.

In the **Supervisory Assessment Status** column, when clicking on the icon button, display an **edit form** with **pre-filled values** from the  **database** .
Create new table as supervisory assessment table
Supervisory Assessment Form Data Points

| Field Name                                                                                                                             | Description                                                                                            |  |
| -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | - |
| ID                                                                                                                                     | Identifier for therecord(auto generated)                                                               |  |
| Assessment Request ID                                                                                                                  | Identifier for theassessment request                                                                   |  |
| Holding Number                                                                                                                         | Holding number of building                                                                             |  |
| Owner Name                                                                                                                             | Name of the owner of the building                                                                      |  |
| Owner Gender                                                                                                                           | Gender of the owner                                                                                    |  |
| Owner Contact (Phone)                                                                                                                  | Contact number of the owner                                                                            |  |
| Containment Type                                                                                                                       | Type of containment:i. Septic Tankii. Pitiii. Holding Tank                                             |  |
| Containment OutletConnection                                                                                                           | i. Stormwater Drainii. Underground Piped Drainiii. WASA Networkiv. Open Groundv. Waterbodyvi. Soak Pit |  |
| Containment Volume (Approx)                                                                                                            | Approximate volume of containment                                                                      |  |
| Road Width                                                                                                                             | Width of access road                                                                                   |  |
| Distance fromthe nearestroad to containment                                                                                            | Distance of nearest road to containment                                                                |  |
| If Septic Tank:Length:Length of Septic Tank in metersWidth: Width of Septic Tank in metersDepth: Depth of Septic Tank in meters        |                                                                                                        |  |
| If Pit:Number of pit rings:Number of pit ringsDiameter of pit:Diameter of pit in metersDepth of pit:Approximate depth of pit in meters |                                                                                                        |  |
| AppropriateDesludging VehicleSize                                                                                                      | Appropriate size ofDesludging Vehicletaking into accountroad width and size of containment             |  |
| Number of Trips                                                                                                                        | Number of trips required withDesludging Vehiclesize                                                    |  |
| Confirmed Emptying Date                                                                                                                | Confirmed date of emptying                                                                             |  |
| Advance Paid Amount                                                                                                                    | Advance paid amount for desludging, at least one trip                                                  |  |

# New column added

---

- **Table : fsm.applications
  supervisory_assessment_date date   Supervisory Assessment Date**
- query : Alter table fsm.applications Add column supervisory_assessment_date date
- Alter table fsm.applications Add column supervisory_assessment_status boolean
