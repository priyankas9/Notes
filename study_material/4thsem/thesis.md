# What mobile app should do (minimum + thesis-ready)

## Mobile responsibilities (core)

### A) Keep updating location

After login:

* update location every X seconds/minutes (e.g., every 30s or every 1–2 mins)
* or update when user moves 50–100 meters

**POST `/api/location`** regularly.

This is needed so alerts match current location.

---

### B) Fetch alerts meant for that user

Mobile should show a screen like:

**“My Alerts”**

* list of alerts that matched this user (from `alert_deliveries`)
* message + time + alert type
* maybe distance from alert point (optional)

**GET `/api/me/alerts`**

Backend returns alerts joined with deliveries.

---

### C) Show notification (2 options)

You can choose:

✅ **Option 1 (easiest): In-app alerts only**

* Mobile polls `GET /api/me/alerts` every 15–30 seconds OR refresh button
* Shows alerts inside app

✅ **Option 2 (better): Push notifications**

* Use FCM token
* Store token in backend
* When alert created → send push to matched users

For thesis, **Option 1 is totally acceptable** if you explain “notification is simulated / in-app”.

---

# Your exact next build steps (in order)

## Step 1 — Backend: location saving

* Create `user_locations` table + GiST index
* Endpoint `POST /api/location`
* Make sure it overwrites latest location for that user

## Step 2 — Admin: Alert module UI

* Create alert form
* Point picker / polygon draw (Leaflet in admin panel)

## Step 3 — Backend: alert matching logic

When admin submits alert:

* insert into `alerts`
* run GIS query to find users
* insert into `alert_deliveries`

## Step 4 — Mobile: My Alerts screen

* create screen
* call `GET /api/me/alerts`
* display list

## Step 5 — Performance logging (start now)

When you run the matching query, store:

* query time (ms)
* matched users count
* total processing time (ms)

  This becomes your thesis results.

---

# Mini API map

### Mobile → Backend

* `POST /api/login`
* `POST /api/location` ✅
* `GET /api/me/alerts` ✅

### Admin → Backend

* `POST /api/alerts` ✅
* `GET /api/alerts/{id}/deliveries` (optional)


//// 


# 🎯 What Your Mobile App Should Do (Final Feature List)

You only need  **5 real features** .

---

# ✅ 1. Authentication (DONE)

* Register
* Login
* Store token
* Auto-login if token exists

You already have this ✔

---

# ✅ 2. Location Update System (You’re halfway here)

After login:

### Mobile must:

* Request location permission
* Get current lat/lng
* Send to backend (`POST /api/me/location`)
* Optionally update periodically (every 1–2 minutes)

### Why?

Because your whole thesis depends on:

> “Users inside polygon receive alert”

If location is not updated, matching fails.

---

# ✅ 3. “My Alerts” Screen (VERY IMPORTANT)

This is your next feature.

### What it does:

* Calls: `GET /api/me/alerts`
* Displays list of alerts matched to that user

### Screen UI Example:

<pre class="overflow-visible! px-0!" data-start="1004" data-end="1114"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Flood Warning</span><br/><span>Type: Polygon</span><br/><span>Time: 3:45 PM</span><br/><span>-------------------</span><br/><span>Road Closure</span><br/><span>Type: Radius</span><br/><span>Time: 10:12 AM</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

This makes your system complete.

Without this, users can’t see alerts.

---

# ✅ 4. Alert Detail Screen (Small but clean feature)

When user taps alert:

* Show message
* Show alert area on map (optional but impressive)
* Show time received

This makes it look professional.

---

# ✅ 5. Background / Refresh Mechanism

Two options:

### Option A (Simple + enough for thesis)

* Refresh button on "My Alerts"
* Or auto-refresh every 30 seconds

### Option B (Advanced)

* Push notifications (FCM)

For thesis,  **Option A is perfectly acceptable** .

---

# 🚫 What You DO NOT Need

❌ Chat system

❌ User-to-user messaging

❌ Real-time live tracking map

❌ Complex social features

❌ Profile editing system

Keep it focused.

---

# 📱 Final Mobile App Structure

### Screens:

1️⃣ Login

2️⃣ Register

3️⃣ Home (after login)

* Shows current location
* Button: “Update Location”
* Button: “View My Alerts”

4️⃣ My Alerts (List screen)

5️⃣ Alert Details (Optional)

That’s enough.

---

# 🔥 How Your Whole System Connects

Mobile:

* Login
* Send location
* Fetch alerts
* Display alerts

Backend:

* Store location
* Admin draws polygon
* Run GIS query
* Save matched users
* Return alerts to mobile
