# to-do 2025.04.10

---

* [X] install fullcalender
* [X] add new inputs in application

# to-do 2025.04.11

---

* [X] application save
* [ ] desludging table -> application form redirection

# to-do 2025.04.15 Tuesday

---

* [ ] desludging table -> application form redirection

  * [ ] reschedule
  * [X] emtying
* [X] disalying prefilled values in an input

  - Datas that is passed : bin , owner name ,owner contact and next emtoying date (proposed emtying date)
    tech docs : C:\xampp\htdocs\notes\Notes\imis_dncc\2025\april\april15.md

# to-do 2025.04.16 Wednesday

---

* [X] desludging table -> application form redirection

- reschedule

* [X] display input value by prefilling it

  - [X] while prefilling value look for multi elect and how to display it
* [ ] calender -> fullcalender app for reschedule
* [ ] javascript logic : when emtying disable input of proposed emtying date
* [ ] save application form after the redirection & update the ststus flag accordingly 😄

# to-do 2025.04.17 Thursday

---

* [ ] calender -> fullcalender app for reschedule
* [X] javascript logic : when emtying disable input of proposed emtying date
* [X] save application form after the redirection & update the ststus flag accordingly 😄

**issue Faced:**
while passing the data / prefilling it applicatin's orms value is not being passsed due to which it says the data is required validation error
proposed emtying date had the strict validation for after or equal of thr todays date
supervioy date should be before proposed emtying date

**CALENDER-FEATURE**

---

| Feature                                      | Support |
| -------------------------------------------- | ------- |
| Full calendar view with day/week/month       | ✅      |
| Disable weekends and custom dates (holidays) | ✅      |
| Show events as**slots per date**       | ✅      |
| Handle click events to open forms/modals     | ✅      |
| Integration with Laravel (via Ajax or Blade) | ✅      |

# to-do 2025.04.18 Friday

---

* [ ] calender -> reschedule (flatpickr)
* [X] uninstall full calender
* [X] install flatpickr
* [X] Display the **day of the week** in brackets next to the date
* [ ] logical flaw issue : when clicking reshdule the only make proposed emtying date's take valu and work accordingly and only different calender when clciking by reschedule button
* [ ] Search for a new **calendar component** (e.g., Flatpickr, FullCalendar) that:* [ ] Displays **available slots**
* [ ] Shows **available dates** (based on site logic)
* [ ] **Disables holidays and weekends**
* [ ] **Highlights important dates**
* [ ] Uses values from **site settings** (`holiday_list`, `weekends`, etc.)
