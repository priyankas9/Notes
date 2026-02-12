## 🎟️ JIRA TICKET: Role-Based Access Control (RBAC) – Routes & Sidebar

**Type:** Story / Task

**Priority:** High

**Component:** Frontend (Auth, Navigation)

**Environment:** Web (React + React Router)

---

### **Title**

Implement Role-Based Access Control for Pages and Sidebar Navigation

---

### **Description**

Implement role-based access control (RBAC) in the frontend so that users only see and access pages permitted for their assigned role. This includes:

1. Role-based login landing pages
2. Route protection using role guards
3. Sidebar navigation filtered by user role

This is currently implemented using a **mock login** (frontend-only). Backend integration will be added later.

---

### **Roles Defined**

| Role            | Description                |
| --------------- | -------------------------- |
| `super_admin` | Full access                |
| `data_entry`  | Limited to Cold Chain data |
| `viewer`      | Read-only map access       |

---

### **Role → Page Access Matrix**

| Page / Route   | super_admin | data_entry | viewer |
| -------------- | ----------- | ---------- | ------ |
| `/dashboard` | ✅          | ❌         | ❌     |
| `/map`       | ✅          | ❌         | ✅     |
| `/coldchain` | ✅          | ✅         | ❌     |
| `/users`     | ✅          | ❌         | ❌     |
| `/settings`  | ✅          | ❌         | ❌     |

---

### **Role → Sidebar Visibility**

| Sidebar Item      | super_admin | data_entry | viewer |
| ----------------- | ----------- | ---------- | ------ |
| Dashboard         | ✅          | ❌         | ❌     |
| Map               | ✅          | ❌         | ✅     |
| Cold Chain Points | ✅          | ✅         | ❌     |
| Users             | ✅          | ❌         | ❌     |
| Settings          | ✅          | ❌         | ❌     |

👉 Sidebar must **hide** links the user is not allowed to access (not just disable).

---

### **Login Behavior**

After successful login:

* `super_admin` → `/dashboard`
* `data_entry` → `/coldchain`
* `viewer` → `/map`

If the user was redirected to login from a protected page, redirect them back  **only if role allows access** , otherwise redirect to their role landing page.

---

### **Technical Notes**

* Role is stored in `localStorage` as `role`
* Token stored as `access_token`
* Route protection via `RequireAuth` + `RequireRole`
* Sidebar reads role using `getRole()` from `auth.store`
* Unauthorized access redirects to `/unauthorized`

---

### **Acceptance Criteria**

* ✅ Users cannot access routes not allowed for their role
* ✅ Sidebar only displays allowed navigation items
* ✅ Direct URL access to restricted routes redirects to `/unauthorized`
* ✅ Login redirects user to correct role-based landing page
* ✅ No sidebar flash of unauthorized items during load

---

### **Test Accounts (Mock)**

<pre class="overflow-visible! px-0!" data-start="2639" data-end="2778"><div class="w-full"><div class=""><div class=""><div class="min-h-0 min-w-0"><div class="border-token-border-light bg-token-bg-elevated-secondary corner-superellipse/1.1 rounded-3xl border my-4"><div class="pointer-events-none sticky z-40 shrink-0 mx-4 transition-opacity duration-300 opacity-0"><div class="sticky bg-token-border-light"></div></div><div class="relative z-0 flex max-w-full"><div id="0ad8fe34-c9fd-44c6-b37e-10b1668db1e6:0:editor" class="Rx43rG_codemirror z-10 flex h-full w-full flex-col items-stretch"><div class="cm-editor ͼ1 ͼ3 ͼd"><div class="cm-announced" aria-live="polite"></div><div tabindex="-1" class="cm-scroller"><div spellcheck="false" autocorrect="off" autocapitalize="off" writingsuggestions="false" translate="no" contenteditable="false" class="cm-content" role="textbox" aria-multiline="true" aria-readonly="true" aria-label="Edit code" aria-placeholder=""><div class="cm-line">super_admin → admin@example.com / Admin@123</div><div class="cm-line">data_entry  → abc@example.com   / Abc@123</div><div class="cm-line">viewer      → viewer@example.com / Viewer@123</div></div></div></div></div></div></div></div></div></div></div></pre>

---

### **Out of Scope**

* Backend authentication & JWT validation
* Dynamic role updates from API
* Permission management UI

### **Title**

Add download options (PNG/SVG) for dashboard charts

---

### **Type**

Story / Task

---

### **Description**

Users need the ability to download dashboard charts as images for reporting and presentations.

This task adds download functionality to all major chart components, allowing users to export charts with proper titles and styling.

---

### **Scope**

Implement download support for the following D3 charts:

* Bar Chart (Type of Cold Chain Point)
* Pie Chart (Type of CCE)
* Donut Chart (Company of CCE)
* Capacity Bars (Refrigerator vs Deep Freezer)

Each chart should support:

* Download as **PNG**
* Download as **SVG**
* Exported image should include the **chart title**
* Exported image should have a **white background**
* Download triggered via a **download icon button** in the card header

---

### **Acceptance Criteria**

* A download icon is visible in the header of each chart card
* Clicking the icon downloads the chart as a PNG image
* Downloaded image includes:
  * Chart visualization
  * Chart title at the top
  * Proper spacing and no clipping
* SVG export works correctly for all charts
* Export works consistently across supported browsers (Chrome, Edge)
* No impact on existing chart rendering or interactions

---

### **Out of Scope**

* Label toggle issues (to be handled in a separate ticket)
* Chart animations or style redesign
* Data changes or API changes

---

### **Notes for QA**

* Verify PNG and SVG downloads for each chart
* Confirm downloaded image matches on-screen chart
* Check title visibility and alignment in exported images
* Ensure background is not transparent

## 🎫 JIRA Ticket: Add Actions & Filter to Users / Cold Chain Points Table

**Issue Type:** Story

**Priority:** Medium

**Component:** Frontend (React + TanStack Table)

**Sprint:** *(your sprint name)*

---

### 📝 Summary

Add  **Actions column** ,  **advanced filter panel** , and **export to Excel** functionality to the Users / Cold Chain Points data table.

---

### 📌 Description

Currently, the Users / Cold Chain Points table only supports basic listing, sorting, and pagination.

To improve usability and administrative control, the table needs action controls and enhanced filtering.

This ticket implements:

* Row-level actions (Edit, Delete)
* Toggleable advanced filter panel (initially hidden)
* Export of filtered data to Excel

---

### ✅ Acceptance Criteria

#### 1️⃣ Actions Column

* Add a new **“Actions”** column at the end of the table
* Each row must contain:
  * ✏️ **Edit** icon button
  * 🗑️ **Delete** icon button
* Clicking:
  * Edit → triggers edit handler (modal / route placeholder)
  * Delete → shows confirmation before delete action

---

#### 2️⃣ Filter Panel

* Add a **Show Filter / Hide Filter** toggle button
* Filter panel must be:
  * **Closed by default** on initial page load
  * Expand/collapse on toggle click
* Filters included:
  * Name (text input)
  * Email (text input)
  * Role (dropdown: super_admin, admin, viewer)
  * Status (dropdown: active, inactive)
* Add **Reset** button to clear all filters
* Add **Filter** button styled with color `#4E79A7`

---

#### 3️⃣ Global Search

* Global search input filters rows by:
  * Name
  * Email
  * Role
  * Status

---

#### 4️⃣ Export to Excel

* Add **Export to Excel** button
* Export should include:
  * Only **filtered & sorted** data
  * Columns: ID, Name, Email, Role, Status
* Output file name:
  * `cold-chain-points.xlsx`

### **JIRA TICKET**

**Title**

Cold Chain Points: Implement data table with filters, search, actions, and Excel export

---

**Type**

Story

---

**Priority**

Medium

---

**Description**

Implement a Cold Chain Points listing page based on the Identification and Location table schema. The page should display cold chain point records in a paginated, sortable table with advanced filtering, global search, row actions, and Excel export functionality.

---

**Scope / Requirements**

1. **Table Structure**
   * Display the following columns:
     * Cold Chain Point ID
     * Point Name
     * Point Type
     * Province Code
     * District Code
     * Municipality Code
     * Geo Point (Latitude, Longitude)
     * Actions (Edit, Delete)
2. **Global Search**
   * Single search input to search across:
     * Cold chain point ID
     * Point name
     * Point type
     * Province, district, municipality codes
     * Geo point (lat,lng)
3. **Advanced Filters Panel**
   * Toggleable filter panel (Show / Hide)
   * Individual filters for:
     * Cold Chain Point ID (text)
     * Point Name (text)
     * Point Type (dropdown)
     * Province Code (text)
     * District Code (text)
     * Municipality Code (text)
   * Reset button to clear all filters
   * Filters should work in combination with global search
4. **Sorting & Pagination**
   * Column sorting enabled for ID and Point Name
   * Client-side pagination with Previous / Next controls
5. **Row Actions**
   * Edit action button (placeholder for future edit flow)
   * Delete action with confirmation prompt
6. **Excel Export**
   * Export filtered and sorted data (not just current page)
   * Excel columns must include:
     * Cold_chain_point_id
     * Point_name
     * Point_type
     * Province_code
     * District_code
     * Municipality_code
     * Geo_point (lat, lng)

---

**Acceptance Criteria**

* Table layout matches the Cold Chain Points schema
* Filters and global search work together correctly
* Pagination and sorting function as expected
* Edit and Delete buttons are visible and clickable
* Excel export downloads only filtered + sorted records
* UI follows existing design system (ShadCN + Tailwind)

---

**Notes**

* Current implementation uses mock data
* API integration will be handled in a separate ticket
* Geo point currently displayed as text (map preview to be added later)

### **JIRA Ticket: Settings → CCE Types Management Page**

**Issue Type:** Story

**Priority:** Medium

**Module:** Settings / Cold Chain Lookups

**Reporter:** *Your name*

**Assignee:** *Frontend Team*

---

### **Title**

Create Settings Page with CCE Types Management (CRUD)

---

### **Description**

We need to implement a **Settings module** for the Cold Chain system.

As part of this, a **CCE Types** management page should be created under **Settings → Cold Chain Lookups** to allow administrators and data entry users to manage Cold Chain Equipment types (e.g., ILR, Deep Freezer).

This page will act as a **lookup management screen** and will later be reused as a pattern for other lookup entities.

---

### **Scope**

1. Add a **Settings landing page** with grouped tiles:
   * Cold Chain Lookups
   * Assessments
2. Under  **Cold Chain Lookups** , add a tile:
   * **CCE Types**
3. Clicking **CCE Types** should navigate to a dedicated page for managing CCE Types.

---

### **CCE Types Page – Functional Requirements**

* Display a **data table** with columns:
  * ID
  * CCE Type Name
  * Actions (Edit / Delete)
* Provide **search functionality** to filter CCE Types.
* Provide **Add CCE Type** functionality:
  * Open modal dialog
  * Input: CCE Type Name
  * Save action adds new row to table
* Provide **Edit CCE Type** functionality:
  * Open modal dialog pre-filled with selected value
  * Save updates the selected row
* Provide **Delete CCE Type** confirmation:
  * Confirmation dialog before deletion
  * Delete removes the selected row
* Include a **Back to Settings** navigation button.

---

### **Access Control**

* Page accessible only to:
  * `super_admin`
  * `data_entry`

---

### **UI/UX Guidelines**

* Use ShadCN UI components:
  * Table
  * Button
  * Dialog
  * Input
* Follow existing dashboard styling and spacing.
* Maintain consistency with other management pages.

---

### **Acceptance Criteria**

* [ ] Settings page shows grouped tiles correctly
* [ ] Clicking **CCE Types** opens the CCE Types page
* [ ] CCE Types table displays data correctly
* [ ] User can add a new CCE Type
* [ ] User can edit an existing CCE Type
* [ ] User can delete a CCE Type with confirmation
* [ ] Search filters CCE Types correctly
* [ ] Role-based access is enforced
* [ ] No console or runtime errors

---

### **Future Enhancements (Out of Scope)**

* Backend API integration
* Persisting data in database
* Reusable lookup configuration for other entities (Companies, Models, Capacities)

## 1️⃣ JIRA TICKET

**Title**

Add Excel (XLSX) download for D3 charts (Bar, Donut, Pie, Capacity)

**Issue Type**

Story

**Priority**

Medium

**Description**

Currently, D3-based charts (Bar, Donut, Pie, Capacity) support image downloads (PNG/SVG) only.

Users require the ability to download the **underlying chart data** in Excel (.xlsx) format for reporting and analysis purposes.

This ticket adds Excel export functionality for all dashboard charts using the same dataset that is rendered in each chart.

---

### Scope / Changes

* Added a reusable Excel export utility using `xlsx`
* Added Excel download buttons to:
  * Company of CCE (Donut chart)
  * Type of CCE (Pie chart)
  * Capacity (Liters) chart
  * Existing Bar charts
* Ensured exported Excel data exactly matches chart data

---

### Acceptance Criteria

* Each chart displays:
  * PNG download button (existing)
  * Excel download button (new)
* Clicking Excel download:
  * Downloads `.xlsx` file
  * Uses same data shown in chart
* No backend/API changes required
* No impact on existing chart rendering

---

### Technical Notes

* Excel export handled fully on frontend using `xlsx`
* Charts remain presentation-only
* Export logic separated into reusable utility functions

---

### Attachments / Reference

* `exportExcel.ts`
