
## Passing Data from Schedule Desludging to Application Form

### **Objective**

To pass pre-filled data from the **Schedule Desludging** module to the **FSM Application Create Form** using session flashing in Laravel. This includes:

* `next_emptying_date`
* `bin` (containment ID)
* `owner_name`
* `owner_contact`

---

### **Flow Overview**

1. **User clicks “Confirm for Assessment”** in the schedule desludging list.
2. **Selected containment info is flashed to session** .
3. **Redirected to `fsm/applications/create` route** .
4. **Application Create form auto-fills specific fields using session data** .

---

### **1. Flashing Data in Controller**

<pre class="overflow-visible!" data-start="901" data-end="1321"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-[5px]">php</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center rounded-sm px-2 font-sans text-xs"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none px-4 py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></span><span class="" data-state="closed"><button class="flex items-center gap-1 px-4 py-1 select-none"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path d="M2.5 5.5C4.3 5.2 5.2 4 5.5 2.5C5.8 4 6.7 5.2 8.5 5.5C6.7 5.8 5.8 7 5.5 8.5C5.2 7 4.3 5.8 2.5 5.5Z" fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.66282 16.5231L5.18413 19.3952C5.12203 19.7678 5.09098 19.9541 5.14876 20.0888C5.19933 20.2067 5.29328 20.3007 5.41118 20.3512C5.54589 20.409 5.73218 20.378 6.10476 20.3159L8.97693 19.8372C9.72813 19.712 10.1037 19.6494 10.4542 19.521C10.7652 19.407 11.0608 19.2549 11.3343 19.068C11.6425 18.8575 11.9118 18.5882 12.4503 18.0497L20 10.5C21.3807 9.11929 21.3807 6.88071 20 5.5C18.6193 4.11929 16.3807 4.11929 15 5.5L7.45026 13.0497C6.91175 13.5882 6.6425 13.8575 6.43197 14.1657C6.24513 14.4392 6.09299 14.7348 5.97903 15.0458C5.85062 15.3963 5.78802 15.7719 5.66282 16.5231Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.5 7L18.5 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>Edit</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-php"><span><span>public</span><span></span><span>function</span><span></span><span>confirmForAssessment</span><span>(</span><span>$id</span><span>)
{
    </span><span>$containment</span><span> = </span><span>Containment</span><span>::</span><span>findOrFail</span><span>(</span><span>$id</span><span>);

    </span><span>session</span><span>()-></span><span>flash</span><span>(</span><span>'next_emptying_date'</span><span>, </span><span>$containment</span><span>->next_emptying_date);
    </span><span>session</span><span>()-></span><span>flash</span><span>(</span><span>'bin'</span><span>, </span><span>$containment</span><span>->bin);
    </span><span>session</span><span>()-></span><span>flash</span><span>(</span><span>'owner_name'</span><span>, </span><span>$containment</span><span>->owner_name);
    </span><span>session</span><span>()-></span><span>flash</span><span>(</span><span>'owner_contact'</span><span>, </span><span>$containment</span><span>->owner_contact);

    </span><span>return</span><span></span><span>redirect</span><span>()-></span><span>route</span><span>(</span><span>'fsm.applications.create'</span><span>);
}
</span></span></code></div></div></pre>

---

### **2. Receiving Flashed Data in ApplicationController**

<pre class="overflow-visible!" data-start="1388" data-end="1934"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-[5px]">php</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center rounded-sm px-2 font-sans text-xs"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none px-4 py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></span><span class="" data-state="closed"><button class="flex items-center gap-1 px-4 py-1 select-none"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path d="M2.5 5.5C4.3 5.2 5.2 4 5.5 2.5C5.8 4 6.7 5.2 8.5 5.5C6.7 5.8 5.8 7 5.5 8.5C5.2 7 4.3 5.8 2.5 5.5Z" fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.66282 16.5231L5.18413 19.3952C5.12203 19.7678 5.09098 19.9541 5.14876 20.0888C5.19933 20.2067 5.29328 20.3007 5.41118 20.3512C5.54589 20.409 5.73218 20.378 6.10476 20.3159L8.97693 19.8372C9.72813 19.712 10.1037 19.6494 10.4542 19.521C10.7652 19.407 11.0608 19.2549 11.3343 19.068C11.6425 18.8575 11.9118 18.5882 12.4503 18.0497L20 10.5C21.3807 9.11929 21.3807 6.88071 20 5.5C18.6193 4.11929 16.3807 4.11929 15 5.5L7.45026 13.0497C6.91175 13.5882 6.6425 13.8575 6.43197 14.1657C6.24513 14.4392 6.09299 14.7348 5.97903 15.0458C5.85062 15.3963 5.78802 15.7719 5.66282 16.5231Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.5 7L18.5 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>Edit</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-php"><span><span>public</span><span></span><span>function</span><span></span><span>create</span><span>(</span><span>Request $request</span><span>)
{
    </span><span>return</span><span></span><span>view</span><span>(</span><span>'fsm.applications.create'</span><span>, [
        </span><span>'formAction'</span><span> => </span><span>$this</span><span>->applicationService-></span><span>getCreateFormAction</span><span>(),
        </span><span>'formFields'</span><span> => </span><span>$this</span><span>->applicationService-></span><span>getCreateFormFields</span><span>(), // contains pre-filled data
        </span><span>'indexAction'</span><span> => </span><span>$this</span><span>->applicationService-></span><span>getIndexAction</span><span>(),
        </span><span>'bin'</span><span> => </span><span>session</span><span>(</span><span>'bin'</span><span>),
        </span><span>'ownerName'</span><span> => </span><span>session</span><span>(</span><span>'owner_name'</span><span>),
        </span><span>'ownerContact'</span><span> => </span><span>session</span><span>(</span><span>'owner_contact'</span><span>),
        </span><span>'nextEmptyingDate'</span><span> => </span><span>session</span><span>(</span><span>'next_emptying_date'</span><span>),
    ]);
}
</span></span></code></div></div></pre>

---

### **3. Injecting Data into Form Fields Dynamically**

<pre class="overflow-visible!" data-start="1997" data-end="2844"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none rounded-t-[5px]">php</div><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-sidebar-surface-primary text-token-text-secondary dark:bg-token-main-surface-secondary flex items-center rounded-sm px-2 font-sans text-xs"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none px-4 py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy</button></span><span class="" data-state="closed"><button class="flex items-center gap-1 px-4 py-1 select-none"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-xs"><path d="M2.5 5.5C4.3 5.2 5.2 4 5.5 2.5C5.8 4 6.7 5.2 8.5 5.5C6.7 5.8 5.8 7 5.5 8.5C5.2 7 4.3 5.8 2.5 5.5Z" fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"></path><path d="M5.66282 16.5231L5.18413 19.3952C5.12203 19.7678 5.09098 19.9541 5.14876 20.0888C5.19933 20.2067 5.29328 20.3007 5.41118 20.3512C5.54589 20.409 5.73218 20.378 6.10476 20.3159L8.97693 19.8372C9.72813 19.712 10.1037 19.6494 10.4542 19.521C10.7652 19.407 11.0608 19.2549 11.3343 19.068C11.6425 18.8575 11.9118 18.5882 12.4503 18.0497L20 10.5C21.3807 9.11929 21.3807 6.88071 20 5.5C18.6193 4.11929 16.3807 4.11929 15 5.5L7.45026 13.0497C6.91175 13.5882 6.6425 13.8575 6.43197 14.1657C6.24513 14.4392 6.09299 14.7348 5.97903 15.0458C5.85062 15.3963 5.78802 15.7719 5.66282 16.5231Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path><path d="M14.5 7L18.5 11" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>Edit</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-php"><span><span>public</span><span></span><span>function</span><span></span><span>getCreateFormFields</span><span>(</span><span></span><span>)
{
    </span><span>$nextEmptyingDate</span><span> = </span><span>session</span><span>(</span><span>'next_emptying_date'</span><span>, </span><span>''</span><span>);
    </span><span>$bin</span><span> = </span><span>session</span><span>(</span><span>'bin'</span><span>, </span><span>''</span><span>);
    </span><span>$ownerName</span><span> = </span><span>session</span><span>(</span><span>'owner_name'</span><span>, </span><span>''</span><span>);
    </span><span>$ownerContact</span><span> = </span><span>session</span><span>(</span><span>'owner_contact'</span><span>, </span><span>''</span><span>);

    </span><span>foreach</span><span> (</span><span>$this</span><span>->createFormFields </span><span>as</span><span> &</span><span>$section</span><span>) {
        </span><span>foreach</span><span> (</span><span>$section</span><span>[</span><span>'fields'</span><span>] </span><span>as</span><span> &</span><span>$field</span><span>) {
            </span><span>if</span><span> (</span><span>$field</span><span>->inputId === </span><span>'proposed_emptying_date'</span><span>) {
                </span><span>$field</span><span>->inputValue = </span><span>$nextEmptyingDate</span><span>;
            } </span><span>elseif</span><span> (</span><span>$field</span><span>->inputId === </span><span>'bin'</span><span>) {
                </span><span>$field</span><span>->inputValue = </span><span>$bin</span><span>;
            } </span><span>elseif</span><span> (</span><span>$field</span><span>->inputId === </span><span>'customer_name'</span><span>) {
                </span><span>$field</span><span>->inputValue = </span><span>$ownerName</span><span>;
            } </span><span>elseif</span><span> (</span><span>$field</span><span>->inputId === </span><span>'customer_contact'</span><span>) {
                </span><span>$field</span><span>->inputValue = </span><span>$ownerContact</span><span>;
            }
        }
    }

    </span><span>return</span><span></span><span>$this</span><span>->createFormFields;
}</span></span></code></div></div></pre>
