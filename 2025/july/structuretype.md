## **Structure Type Update — Checklist**

### 📌 1️⃣ Form Updates

* [X] Add `structure_type` dropdown in **Add Building form**
  * `BuildingController->create()`
* [X] Edit `structure_type` dropdown in **Edit Building form**
  * `BuildingController->edit()`

---

### 📌 2️⃣ DataTable Filter

* [X] Add `structure_type` filter in **Building Datatable**
  * `BuildingController->index()`

---

### 📌 3️⃣ Survey Form

* [ ] Add `structure_type` dropdown in **Building Survey Approve form**
  * `BuildingSurveyController->approve()`

---

### 📌 4️⃣ Database Table Updates

* [ ] Update values in `structure_type` table
  * *Not built yet*
* [X] Create/Update **Seeder for StructureType**
  * `StructureTypeSeeder->run()`
* [ ] Create **Seeder for BuildingType**
  * *Not built yet*

---

### 📌 5️⃣ Validation

* [ ] Add `structure_type` validation message in **Add Building form**
  * `BuildingRequest->store()`, `$messages` array
* [ ] Add `structure_type` validation message in **Edit Building form**
  * `BuildingRequest->update()`, `$messages` array

---

### 📌 6️⃣ GIS / GeoServer

* [X] Make required changes in GeoServer style file
  * Example: `style:<workspace/>:buildings_layer_structure_type`

---

### 📌 7️⃣ Export Functionality

* [ ] Update export in **CSV, KML, Shape File**
  * `BuildingController->export()`
  * `building->index()->export-kml`
  * `export-shp`
