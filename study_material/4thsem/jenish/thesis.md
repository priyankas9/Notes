## Mobile app features (React Native)

### 1) Auth + onboarding

* Register / login
* Email verification (OTP code)
* Create profile: name + photo (optional)
* Logout

### 2) Session / matching

Pick the simplest MVP:

* **Create session** (Passenger) → generates a **join code / QR**
* **Join session** (Driver) → enters code / scans QR
* Show “Connected with X” screen
* Session status: active / ended

### 3) In-app calling (WebRTC)

* “Call” button (audio only for MVP)
* Incoming call UI: accept / reject
* In-call screen: mute, speaker, end
* Handle reconnect / call ended events
* Optional: show call timer

### 4) Notifications (nice to have, but important)

* Push notification for incoming call (harder)
* Minimum MVP alternative: keep app foreground, use websocket ringing screen

### 5) Basic safety UX

* Block calling when session ended
* Report user / block user (optional for later)

---

## Backend features (Laravel)

### 1) Auth API (Sanctum)

* Register (send email code)
* Verify email (issue token)
* Login (only if verified)
* Logout
* Me/Profile endpoints

### 2) Roles & permissions (Spatie) — minimal

* Roles: `admin`, `driver`, `passenger`
* Permissions (MVP):
  * `session.create` (passenger)
  * `session.join` (driver)
  * `call.initiate`
  * `call.accept`
  * `call.end`
  * `admin.manage_users` (admin)

*(You can still enforce “ownership” with Policies.)*

### 3) Session management (core for privacy)

* Create session:
  * `POST /api/sessions` → returns `code`
* Join session:
  * `POST /api/sessions/join` → validates code, attaches driver
* End session:
  * `POST /api/sessions/{id}/end`
* Session validation middleware:
  * ensures only those 2 users can interact

**DB tables**

* `sessions` (id, code, passenger_id, driver_id, status, expires_at)
* optional `session_events` / `call_logs`

### 4) Real-time signaling (WebSockets)

Backend is used for  **signaling** , not the actual audio.

* Websocket channels like:
  * `session.{id}`
* Events:
  * `call.offer`, `call.answer`, `call.ice`
  * `call.ringing`, `call.accepted`, `call.ended`

### 5) TURN/STUN config delivery

Backend can return config to client:

* `GET /api/webrtc-config` → returns STUN/TURN servers

  (You’ll probably need TURN in real networks.)

### 6) Rate limits + security

* Rate limit register/login/verify endpoints
* Rate limit session creation and call attempts
* Block users/admin suspend
* Audit logs (optional)

### 7) Admin basics (optional MVP)

* List users
* Block/unblock
* View session history/call logs

---

## Important distinction (so you design correctly)

### Backend does **NOT** carry the voice

With WebRTC:

* Voice goes **phone-to-phone** (P2P) or through TURN server
* Backend only handles:
  * auth
  * session permission checks
  * signaling messages

---

## MVP feature list (smallest you can ship)

**Mobile**

1. Login/register + verify email
2. Create session code (passenger)
3. Join with code (driver)
4. Audio call + end call

**Backend**

1. Auth endpoints + tokens
2. Sessions endpoints + DB
3. Websocket signaling
4. Basic roles

---

If you tell me which flow you want:

* **Ride booking** (request/accept) OR
* **Session code / QR** (simpler)

…I’ll give you the exact **DB tables + API endpoints list + websocket event names** for both mobile and Laravel.


Diagram Flow 


---

## Visual 1: High-level architecture

<pre class="overflow-visible! px-0!" data-start="165" data-end="1349"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>┌──────────────────────────┐</span><br/><span>│   Passenger App (RN)      │</span><br/><span>│  - Auth UI                │</span><br/><span>│  - Session screen         │</span><br/><span>│  - WebRTC audio call       │</span><br/><span>└───────────┬──────────────┘</span><br/><span>            │ 1) HTTPS REST (Sanctum)</span><br/><span>            │    /register /login /sessions</span><br/><span>            │</span><br/><span>            │ 2) WebSocket (signaling)</span><br/><span>            │    call.offer / call.answer / ICE</span><br/><span>            ▼</span><br/><span>┌──────────────────────────────────────────────┐</span><br/><span>│              Laravel Backend                 │</span><br/><span>│  - Sanctum Auth                              │</span><br/><span>│  - Spatie Roles/Permissions                  │</span><br/><span>│  - Sessions (create/join/end)                │</span><br/><span>│  - WebSocket server (Laravel WebSockets)     │</span><br/><span>│  - Broadcast events                          │</span><br/><span>└───────────┬──────────────────────────────────┘</span><br/><span>            │</span><br/><span>            │ (Optional) STUN/TURN creds/config</span><br/><span>            ▼</span><br/><span>┌──────────────────────────┐</span><br/><span>│ STUN/TURN Server          │</span><br/><span>│  - Helps connect WebRTC   │</span><br/><span>│  - TURN relays if needed  │</span><br/><span>└──────────────────────────┘</span><br/><br/><span>┌──────────────────────────┐</span><br/><span>│     Driver App (RN)       │</span><br/><span>│  - Auth UI                │</span><br/><span>│  - Join session            │</span><br/><span>│  - WebRTC audio call       │</span><br/><span>└──────────────────────────┘</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

**Key point:** Laravel  **does not carry audio** . Audio flows via **WebRTC** between phones (or via TURN).

---

## Visual 2: Backend ↔ Mobile communication types

### A) REST API (HTTPS)

Used for “normal” actions:

* register/login/verify-email
* create session / join session / end session
* fetch profile / session details

<pre class="overflow-visible! px-0!" data-start="1676" data-end="1779"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Mobile App  ─────── HTTPS JSON ───────>  Laravel API</span><br/><span>           <────── HTTPS JSON ────────</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### B) WebSockets (Real-time signaling + status)

Used for instant messages/events:

* incoming call ringing
* exchange WebRTC offer/answer
* exchange ICE candidates
* call ended, user left session

<pre class="overflow-visible! px-0!" data-start="1978" data-end="2049"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Mobile App  <──── WebSocket Events ────> Laravel WebSockets</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### C) WebRTC (Actual voice)

This is the real “call”. Laravel doesn’t hear it.

<pre class="overflow-visible! px-0!" data-start="2131" data-end="2240"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Passenger Phone  <──── WebRTC Audio ────> Driver Phone</span><br/><span>            (P2P)        OR via TURN relay</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## Visual 3: Sequence diagram (how a call happens)

### Step 1 — Both users are in the same session

<pre class="overflow-visible! px-0!" data-start="2347" data-end="2831"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Passenger App         Laravel API             Driver App</span><br/><span>    | POST /sessions       |                      |</span><br/><span>    |--------------------->|                      |</span><br/><span>    |   {code, session_id} |                      |</span><br/><span>    |<---------------------|                      |</span><br/><span>    |                      | POST /sessions/join  |</span><br/><span>    |                      |<---------------------|</span><br/><span>    |                      |   {ok}               |</span><br/><span>    |                      |--------------------->|</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### Step 2 — WebRTC signaling over WebSocket

<pre class="overflow-visible! px-0!" data-start="2878" data-end="4062"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Passenger App         Laravel WebSocket         Driver App</span><br/><span>    | connect ws            |                      |</span><br/><span>    |---------------------->|                      |</span><br/><span>    |                      |<----------------------|</span><br/><span>    | tap Call              |                      |</span><br/><span>    | send "call.ringing"   |                      |</span><br/><span>    |---------------------->|  broadcast to driver |</span><br/><span>    |                       ---------------------> |</span><br/><span>    |                      |     incoming call UI  |</span><br/><span>    |                      |<----------------------|</span><br/><span>    | create WebRTC OFFER   |                      |</span><br/><span>    | send offer            |                      |</span><br/><span>    |---------------------->|  broadcast offer      |</span><br/><span>    |                       ---------------------> |</span><br/><span>    |                      |  driver creates ANSWER|</span><br/><span>    |                      |<----------------------|</span><br/><span>    |                      |  broadcast answer      |</span><br/><span>    |<---------------------|---------------------- |</span><br/><span>    | exchange ICE candidates (both sides)          |</span><br/><span>    |---- ICE --->          |          <--- ICE ----|</span><br/><span>    |                      |                      |</span><br/><span>    | ✅ WebRTC connects and audio starts ✅       |</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### Step 3 — End call / end session

<pre class="overflow-visible! px-0!" data-start="4100" data-end="4436"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-6 bottom-6"><div class="sticky z-1!"><div class="bg-token-bg-elevated-secondary sticky"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼs ͼ16"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Passenger App         Laravel WebSocket         Driver App</span><br/><span>    | end call              |                      |</span><br/><span>    | send "call.ended"     |                      |</span><br/><span>    |---------------------->|  broadcast to driver  |</span><br/><span>    |                       ---------------------> |</span><br/><span>    | close WebRTC          |                      |</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## What endpoints your backend will have (simple MVP)

### Auth

* `POST /api/register`
* `POST /api/verify-email`
* `POST /api/login`
* `GET /api/me` (auth:sanctum)
* `POST /api/logout` (auth:sanctum)

### Session

* `POST /api/sessions` (passenger creates, returns `code`)
* `POST /api/sessions/join` (driver joins using code)
* `POST /api/sessions/{id}/end` (either ends)
* `GET /api/sessions/{id}` (get session info)

### WebRTC config (optional)

* `GET /api/webrtc-config` (returns STUN/TURN list)

---

## What WebSocket events you’ll use (names you can copy)

* `session.joined`
* `call.ringing`
* `call.offer`
* `call.answer`
* `call.ice_candidate`
* `call.ended`
* `session.ended`

---

## Quick mental model (super simple)

* **REST** = “save things in DB / do official actions”
* **WebSocket** = “tell the other phone instantly”
* **WebRTC** = “actual call audio”

---

If you tell me which WebSocket approach you’re using:

1. **Laravel WebSockets (Pusher protocol)** or
2. **Socket.io server**
