## Business process: Add Application

### Actors

* **System User** (Admin/Operator) who creates the application
* **System** (IMIS application + database)

---

## 1) Start application creation

1. User opens **Add Application** screen. c4a987b4-bebb-433c-ab69-3396e6e…
2. System displays the form sections:
   * **Address**
   * **Owner Details**
   * **Applicant Details** (with “Same as Owner” checkbox)
   * **Service Provider Details**
   * Buttons:  **Back to List** , **Save** c4a987b4-bebb-433c-ab69-3396e6e…

---

## 2) Select Address (primary decision point)

3. User selects  **Street Name / Street Code** . c4a987b4-bebb-433c-ab69-3396e6e…
4. System filters and loads **House Number / BIN** options based on the selected street/road code. c4a987b4-bebb-433c-ab69-3396e6e…
5. User selects a  **House Number / BIN** . c4a987b4-bebb-433c-ab69-3396e6e…

### System auto-actions after BIN selection

6. System fetches building details and auto-fills:
   * **Containment ID**
   * **Ward Number**
   * **Owner Name / Gender / Contact** (shown disabled/locked in your UI) c4a987b4-bebb-433c-ab69-3396e6e…

**Decision: Is address/BIN available?**

* **If BIN found:** proceed to step 7.
* **If “Address Not Found (ANF)” mode exists:** system switches to manual entry flow (you planned this earlier). In that flow, the user manually enters address/building details and continues (instead of auto-fill).

---

## 3) Confirm Owner details

7. User reviews **Owner Details** (usually read-only if auto-filled). c4a987b4-bebb-433c-ab69-3396e6e…
8. If allowed by your business rules, user may correct owner details; otherwise they remain locked as system-record data.

---

## 4) Enter Applicant details

9. User fills  **Applicant Name, Applicant Gender, Applicant Contact** . c4a987b4-bebb-433c-ab69-3396e6e…
10. If user checks  **Same as Owner** , system copies owner values into applicant fields (auto-fill). c4a987b4-bebb-433c-ab69-3396e6e…

---

## 5) Assign Service Provider

11. User selects  **Desludging Vehicle Size** . c4a987b4-bebb-433c-ab69-3396e6e…
12. System sets/auto-suggests **Service Provider Name** based on rules (your code shows this can be auto-selected by capacity/sequence). c4a987b4-bebb-433c-ab69-3396e6e…

---

## 6) Save application

13. User clicks  **Save** . c4a987b4-bebb-433c-ab69-3396e6e…
14. System validates required fields (e.g., BIN/address mode, applicant details, vehicle size, etc.).
15. If validation passes:

* System creates the application record in the database.
* System shows success message and returns to list or stays on page (depending on your implementation).

16. If validation fails:

* System shows errors and keeps the user on the form to correct inputs.

---

## Optional: Short “ANF” branch to include in your business process

**If Address Not Found (ANF):**

* User selects **ANF**
* System enables **manual address fields** (instead of BIN-based autofill)
* User provides address text + (optional/required) map location
* User completes Applicant + Service Provider and saves
* System stores the application with “ANF” flag and later admin can link it to a formal BIN/Containment

(You can include this as a separate decision branch in your diagram.)

---

If you want, I can convert this into a **flowchart-style numbered diagram** (Start → Select Street → Select BIN → Auto-fill → Applicant → Provider → Save) using your exact labels.
