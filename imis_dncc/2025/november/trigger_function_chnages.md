### **Update Summary (Informal)**

Updated the building structure types in the system because the old categories (RCC, Load Bearing, Wooden/Mud, CGI) are no longer relevant.

We now use the new structure list:

* Pucca (1)
* Tin (2)
* Kutcha (3)
* Semi Pucca (4)
* Other (5)
* N/A (6)

To support this, we added new columns in both **grids** and  **wards** :

* `no_pucca`
* `no_tin`
* `no_kutcha`
* `no_semi_pucca`
* `no_other_structure`
* `no_na_structure`

And we removed the old columns that didn’t match the new structure types.

The trigger function (`fnc_set_buildings`) was rewritten so it now calculates counts based on the new structure IDs.

Everything else—population served, HH served, sewerage system counts—stays the same.

So basically:

* New structure names → new columns
* Old structure columns → removed
* Trigger function → updated to use new IDs
* Aggregations for grids + wards → now correct with the new structure list
