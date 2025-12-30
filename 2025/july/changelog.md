### Rename column from next emtying date to proposed emptying date in desludging schedule

### Application Module :

### 🆕 Feature: Service Provider Auto-Assignment with Rotating Sequence

**Added:**

* Implemented **automatic assignment of service providers** based on a rotating sequence.
* Introduced method `calculateSequence()` to generate a non-repetitive, fair round-robin order of active service providers.
* Sequence is stored in `ServiceProviderSequence` table with:
  * `service_provider_id`
  * `sequence_order` (ensures unique ordering)
  * `current_sequence` (tracks the active provider)

**Modified:**

* In the `create()` form, the service provider field is:
  * **Disabled and pre-filled** if auto-assignment setting is enabled.
  * **Selectable manually** if auto-assignment is disabled.
* Updated `ApplicationService::createApplication()` to **rotate the provider sequence** after each new application is created.

**Added Blade logic** to show:

* Hidden input with service provider ID and name when auto-assignment is on.
* Dropdown menu when auto-assignment is off.

---

### ✅ Usage Summary:

* Sequence is initialized only once if missing.
* Each application assigns the **current provider** and then **rotates** to the next one.
* Ensures fair load balancing across all active service providers.

### Dashboard : Main and Building

---

Added new countbox named as category

### Supervisory Module

---

- All the columned should be named as confirmed not confirm
