## 1) Login gives tokens (authentication step)

When you sign in (`components/signin-form.tsx`):

1. Calls `login(email, password)` (`services/auth.service`)
2. On success, it stores tokens using `loginTokenStorage(access, refresh)` (`lib/auth.ts`)

`loginTokenStorage` saves tokens in  **two places** :

* **localStorage** : `access_token`, `refresh_token`
* **cookies** : `access_token`, `refresh_token` (important for middleware)

So after login, your app has tokens available both client-side and server-side.

---

## 2) Middleware blocks/redirects routes (route protection)

`middleware.ts` checks `access_token` from  **cookies** :

* If you **don’t** have `access_token` and you try to access protected pages → it redirects to `/signin`
* If you **do** have `access_token` and you try to access `/` or `/signin` → it redirects to `/dashboard`

So:

✅ **authentication gating** is handled globally by middleware.

**Important:** middleware here does **NOT** check roles/permissions — it only checks “is logged in”.

---

## 3) AuthProvider loads user profile + permissions (RBAC data source)

`providers/auth-provider.tsx` is where RBAC data is managed.

On app load it:

1. Reads `access_token`, `refresh_token`, and `user_profile` from localStorage
2. If they exist:
   * sets `user` from stored profile
   * calls `getRefreshToken(refreshToken)` to refresh access token
   * stores new tokens again
   * calls `fetchUserProfile()`

`fetchUserProfile()` calls `getProfile()` and saves:

* `user` (whole profile)
* `permissions` (very important)
* also stores profile into localStorage

### Key point:

RBAC permissions come from the backend  **profile response** :

Your `User` type includes:

<pre class="overflow-visible! px-0!" data-start="1985" data-end="2033"><div class="w-full my-4"><div class=""><div class="min-h-0 flex-1 relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary border-token-border-light border relative"><div class="absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="absolute inset-x-0 top-0 bottom-54"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼv">permissions</span><span>: </span><span class="ͼt">Permission</span><span>[];</span><br/><span class="ͼv">role</span><span>: </span><span class="ͼt">Role</span><span>;</span></div></div></div></div></div></div></div><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"></div></div></div></div></div></pre>

So RBAC authority is:

✅ backend decides permissions

✅ frontend reads them from profile

✅ frontend uses them to allow/hide parts of UI

---

## 4) `checkPermission()` checks if user has a permission string

`lib/checkPermission.ts` (your code) does:

* Reads `permissions` from `useAuth()`
* Looks for a matching permission object by name
* Returns true/false

So your RBAC check is essentially:

> “Does the user’s `permissions[]` contain `{ name: "<permission>" }`?”

---

## 5) Sidebar is the actual RBAC enforcement you can *see*

In `components/sidebar.tsx`, menu items are filtered using:

* `checkPermission("list-roles")`
* `checkPermission("list-users")`
* etc.

That means:

✅ Users only *see* modules they have permission to list/view.

So the RBAC currently implemented in this repo is primarily:

### **UI-level RBAC (navigation/menu gating)**

---

## What RBAC is NOT doing yet (important)

Even if the sidebar hides links:

* A user could still manually type `/dashboard/users` in the URL **and middleware will allow it** (because they’re authenticated).
* There is no route-level permission guard in middleware.
* There is no per-page permission check shown (like blocking page render if missing permission).

So:

✅ Authentication is enforced globally

✅ Permissions are loaded and used for UI gating

⚠️ Page-level permission enforcement isn’t fully implemented in frontend (unless backend blocks it)

---

## One small code issue to be aware of

Your `checkPermission()` uses `useAuth()` inside a normal function. React hooks are safest when used in:

* React components, or
* custom hooks (functions starting with `use...`)

It works *in practice* if it’s only called during render, but the clean pattern is:

<pre class="overflow-visible! px-0!" data-start="3769" data-end="3939"><div class="w-full my-4"><div class=""><div class="min-h-0 flex-1 relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary border-token-border-light border relative"><div class="absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="absolute inset-x-0 top-0 bottom-54"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">export</span><span></span><span class="ͼn">const</span><span></span><span class="ͼt">useCheckPermission</span><span></span><span class="ͼn">=</span><span> () => {</span><br/><span></span><span class="ͼn">const</span><span> { permissions } </span><span class="ͼn">=</span><span></span><span class="ͼt">useAuth</span><span>();</span><br/><span></span><span class="ͼn">return</span><span> (</span><span class="ͼt">permission</span><span>: </span><span class="ͼt">string</span><span>) => </span><span class="ͼt">permissions</span><span class="ͼn">.</span><span>some(</span><span class="ͼt">p</span><span> => </span><span class="ͼt">p</span><span class="ͼn">.</span><span>name </span><span class="ͼn">===</span><span></span><span class="ͼt">permission</span><span>);</span><br/><span>};</span></div></div></div></div></div></div></div><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"></div></div></div></div></div></pre>

---

## Summary in one line

**RBAC is managed by fetching permissions from the user profile in `AuthProvider`, storing them in context, and using `checkPermission()` to show/hide UI modules (mainly the sidebar), while middleware only enforces “logged in” access.**

If you want, paste your `components/sidebar.tsx` and I’ll map exactly which permission strings control which screens (so you can explain it cleanly in documentation/viva).
