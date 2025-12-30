# 📱 DNCC - Mobile App Requirements

---



## 🏗 Building Form

---

**Add a new action** after “Add Supervisory” — called  **Update Building Info** .

* It should be  **an exact replica of the website’s building form** .
  🔗 Reference GitHub Resources
* 🔧 **Main Repository:**

  https://github.com/base-imis/web_app/tree/v1.2.0-tools
* 📜 **Building Code Logic:**

  https://github.com/base-imis/web_app/blob/v1.2.0-tools/public/js/functions.js
* 🧩 **Frontend Building Form:**

  [https://github.com/base-imis/web_app/blob/v1.2.0-tools/resources/views/building-info/buildings](https://github.com/dncc-imis/web_app/tree/master/resources/views/building-info/buildings)
* 🚽 **Containment Form + Logic:**

  [https://github.com/dncc-imis/web_app/tree/master/resources/views/fsm/containments](https://github.com/dncc-imis/web_app/tree/master/resources/views/fsm/containments)

### 💻 Backend References

* 🔙 **Building Controller:**

  [https://github.com/base-imis/web_app/blob/v1.2.0-tools/app/Http/Controllers/BuildingInfo/BuildingController.php](https://github.com/dncc-imis/web_app/blob/master/app/Http/Controllers/BuildingInfo/BuildingController.php)
* 🔙 **Containment Controller:**

  [https://github.com/base-imis/web_app/blob/v1.2.0-tools/app/Http/Controllers/Fsm/ContainmentController.php](https://github.com/dncc-imis/web_app/blob/master/app/Http/Controllers/Fsm/ContainmentController.php)
* 🔧 **Building Structure Service:**

  [https://github.com/base-imis/web_app/blob/v1.2.0-tools/app/Services/BuildingInfo/BuildingStructureService.php](https://github.com/dncc-imis/web_app/blob/master/app/Services/BuildingInfo/BuildingStructureService.php)
* 🔧 **Containment Service:**

  [https://github.com/base-imis/web_app/blob/v1.2.0-tools/app/Services/Fsm/ContainmentService.php](https://github.com/dncc-imis/web_app/blob/master/app/Services/Fsm/ContainmentService.php)