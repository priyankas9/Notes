### **API Integration Instructions**

#### **1. Prefill Form Data from `assessedsupervisory-applications` API**

Map these fields from the API response to the form:

* `"customer_name"` → **Owner Name**
* `"customer_gender"` → **Owner Gender**
* `"customer_contact"` → **Owner Contact**
* `"proposed_emptying_date"` → **Confirm Emptying Date**
* `"containment_size"` → **Containment Volume**
* `"tank_length"` → **Septic Tank Length (m)**
* `"tank_width"` → **Septic Tank Width (m)**
* `"depth"` → **Septic Tank Depth (m)**

#### **2. Handling `type_id` for Containment Type**

* The `assessedsupervisory-applications` API provides a `type_id` (e.g., `3`).
  ![1748337879927](image/schedulefields/1748337879927.png)
* **Fetch `containment-types` API** to get the full list of containment types (dropdown options).
  ![1748338025682](image/schedulefields/1748338025682.png)
* **Match** the `type_id` (e.g., `3`) with the `id` in the `containment-types` response.
* **Display** the matched `type` (e.g.,  *“Septic Tank connected to Soak Pit”* ) in the form.

#### **3. Dropdown for Containment Type**

* Use the `containment-types` API response to  **populate the dropdown options** .
* Each dropdown item should show the `type` field (e.g.,  *“Septic Tank connected to Soak Pit”* ).
* When a user selects an option, store its `id` (not the text).

#### **Example Flow**

1. Call `assessedsupervisory-applications` → Get `type_id: 3`.
2. Call `containment-types` → Find `id: 3` → Display `type: "Septic Tank connected to Soak Pit"` in the form.
3. Populate the dropdown with all `type` values from `containment-types`.

#### **Edge Cases**

* If `type_id` has no match, show *“Unknown”* or leave the field blank.
* If the dropdown is empty, ensure `containment-types` API is called first.

---

### **Key Points**

* **Prefill** : Directly map the fields listed above.
* **Dropdown** : Use `containment-types` API to show options.
* **Match Logic** : `type_id` → `id` → `type`.


public function edit($id)
    {
        $supervisoryassessment = SupervisoryAssessment::find($id);

    if ($supervisoryassessment) {$page_title = "Edit Supervisory Assessment";$application = Application::find($supervisoryassessment->application_id);
            $owner_detail = SupervisoryAssessment::where('id', $id)->first();
            $containment = SupervisoryAssessment::where('id', $id)->first();
            $type_id = SupervisoryAssessment::where('id', $id)->first();
            $indexAction = url()->previous();
            return view('fsm.supervisory-assessment.edit',compact('page_title','supervisoryassessment','indexAction',
            'application',
            'owner_detail',
            'containment','type_id'));
        } else {
            abort(404);
        }
    }
