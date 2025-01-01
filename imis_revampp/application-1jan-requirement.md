# Application

---

- **Single Containment:**

* If the bin in the application has only one containment:
  * Display the containment ID as uneditable.
* **Multiple Containments:**
  If the bin in the application has multiple containments:
  * Display the containment IDs in a dropdown (single select only).
  * Show only the containment IDs that are not currently in the application process (i.e., `empting_status: false`).
* **Containment ID Display:**
  Ensure that the containment ID is displayed in the application data table.

#### Emptying Form Validation

---

- Previously, we validated by summing up multiple containments associated with a bin.
-  **Update:** Remove the sum validation.
