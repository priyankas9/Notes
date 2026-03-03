# Address Not Found

---



“Address Not Found” arises when the searched BIN is either:

* not in the database, OR
* in the database but has no containment records.

Because your dropdown filters only buildings that have containments.

///// 


# What We Found (Impact Analysis Summary)

## 1️⃣ The dropdown filters out valid buildings

Because of:

<pre class="overflow-visible! px-0!" data-start="343" data-end="389"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-0 bottom-96"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Building::whereHas('containments');</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

The system  **only shows buildings that already have containments** .

### Impact:

* Buildings that exist but have no containment are treated like they don’t exist.
* Users may think the address is invalid when it is actually valid.
* Valid addresses are excluded from workflow.

---

## 2️⃣ “Address Not Found” does NOT actually mean the address doesn’t exist

It can mean two different things:

* BIN truly does not exist
* BIN exists but has no containment

### Impact:

* The system cannot distinguish between:
  * Missing address
  * Missing containment
* This causes misleading behavior and incorrect assumptions.

---

## 3️⃣ Backend and Frontend logic are inconsistent

* Frontend expects clear statuses.
* Backend only returns:
  <pre class="overflow-visible! px-0!" data-start="1127" data-end="1177"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-0 bottom-96"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>"status" => !empty($containmentIds)</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>
* Missing BIN causes 500 error instead of structured response.

### Impact:

* Poor error handling
* Hard to debug
* System looks unstable (500 errors)

---

## 4️⃣ Workflow Limitation

Because only buildings with containments are selectable:

* Users cannot create applications for buildings without containment.
* This blocks potential data entry processes.
* Forces manual workarounds.

---

# 🎯 Final Impact Conclusion (Clean Version for Report)

> The current BIN dropdown implementation filters buildings based on existing containment records. As a result, valid buildings without containment are excluded and may be interpreted as “Address Not Found.” This creates ambiguity between non-existent addresses and missing containment data, leading to incorrect workflow blocking, misleading system behavior, and reduced usability.

---

# 🧠 In very simple words:

We found that:

* “Address Not Found” does not always mean the address is missing.
* Sometimes it just means there is no containment.
* The system mixes up these two cases.
* This affects usability, clarity, and workflow accuracy.

# APPLICATION Deletion Logic

---



## Business process: When does an application get deleted?

### ✅ Application **can be deleted** only when:

1. The application exists (`Application::findOrFail($id)` succeeds)
2. It has **NO related records** in:
   * `emptying`
   * `sludge_collection`
   * `feedback`

If all three are absent → it deletes:

<pre class="overflow-visible! px-0!" data-start="460" data-end="569"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-0 bottom-96"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>$application->delete();</span><br/><span>return redirect(...)->with('success','Application deleted successfully.');</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## When does an application NOT get deleted?

### ❌ It will NOT delete if **any one** of these exists:

#### 1) Emptying exists

<pre class="overflow-visible! px-0!" data-start="704" data-end="839"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-0 bottom-96"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>if($application->emptying()->exists()){</span><br/><span>  return ... "Cannot delete Application that has associated Emptying Information."</span><br/><span>}</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

#### 2) Sludge collection exists

<pre class="overflow-visible! px-0!" data-start="874" data-end="1027"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-0 bottom-96"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>if($application->sludge_collection()->exists()){</span><br/><span>  return ... "Cannot delete Application that has associated Sludge Collection Information."</span><br/><span>}</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

#### 3) Feedback exists

<pre class="overflow-visible! px-0!" data-start="1053" data-end="1188"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-0 bottom-96"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>if($application->feedback()->exists()){</span><br/><span>  return ... "Cannot delete Application that has associated Feedback Information."</span><br/><span>}</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### ❌ It will also NOT delete if:

* the ID doesn’t exist (findOrFail throws)
* any unexpected error happens (caught by `catch`)

  Then it returns:

<pre class="overflow-visible! px-0!" data-start="1335" data-end="1377"><div class="w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border corner-superellipse/1.1 border-token-border-light bg-token-bg-elevated-secondary rounded-3xl"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="pointer-events-none absolute inset-x-px top-0 bottom-96"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-bg-elevated-secondary"></div></div></div><div class="corner-superellipse/1.1 rounded-3xl bg-token-bg-elevated-secondary"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>"Failed to delete Application."</span></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# Why is this rule important? (Business reason)

This is a  **data integrity rule** :

Once an application has progressed into operational steps (emptying, sludge collection, feedback), deleting it would:

* break reports
* break history/audit trail
* orphan related records
* mess up trip tracking and compliance

So the system only allows deletion when the application is still “fresh” and has no downstream activity.

---

# Impact analysis (what we found)

## ✅ Positive impacts of this delete restriction

1. **Prevents loss of important operational records**

* You keep evidence of services performed.

2. **Maintains database consistency**

* No broken links / orphan records.

3. **Supports audit and accountability**

* You can trace what happened even if someone wants to remove an application.

---

## ⚠ Possible negative impacts / limitations

1. **Users cannot correct mistakes easily**

* If a wrong application was created and emptying/sludge/feedback was added by mistake, they can’t delete it — they must edit/cancel instead.

2. **No “soft cancel” path shown here**

* Your system has “delete” OR “not delete”.
* In real operations, you often need “Cancel” status rather than deletion.

3. **Generic catch hides the real error**

* The catch message “Failed to delete” doesn’t tell why (permissions, DB issue, etc.) which makes debugging harder.

---

# Clean report-ready paragraph (you can paste in thesis)

> The application deletion process is restricted to preserve operational and audit data. An application can only be deleted when it has no associated emptying, sludge collection, or feedback records. If any of these dependent records exist, deletion is blocked and the user is notified. This control ensures data integrity by preventing orphaned service records and maintaining historical traceability; however, it reduces flexibility when correcting mistakes, suggesting the need for an alternative workflow such as application cancellation rather than deletion.
>



use Illuminate\Support\Facades\DB;

public function destroy($id)
{
    try {
        return DB::transaction(function () use ($id) {

    // Lock the row to avoid race conditions (two users deleting at same time)$application = Application::where('id', $id)->lockForUpdate()->firstOrFail();

    // Check related records (block deletion if any exists)
            if ($application->emptying()->exists()) {
                return redirect('fsm/application')
                    ->with('error', __('Cannot delete: Emptying record already exists for this application.'));
            }

    if ($application->sludge_collection()->exists()) {
                return redirect('fsm/application')
                    ->with('error', __('Cannot delete: Sludge Collection record already exists for this application.'));
            }

    if ($application->feedback()->exists()) {
                return redirect('fsm/application')
                    ->with('error', __('Cannot delete: Feedback record already exists for this application.'));
            }

    // ✅ Safe to delete (no dependent records)
            $application->delete();

    return redirect('fsm/application')
                ->with('success', __('Application deleted successfully.'));
        });

    } catch (\Illuminate\Database\Eloquent\ModelNotFoundException $e) {
        return redirect('fsm/application')
            ->with('error', __('Application not found.'));
    } catch (\Throwable $e) {
        // Optional: log the real error for debugging
        // \Log::error('Application delete failed', ['id' =>$id, 'error' => $e->getMessage()]);

    return redirect('fsm/application')
            ->with('error', __('Failed to delete Application.'));
    }
}
