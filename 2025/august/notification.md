# Notification

---

**Times to notify**

- application creation
  - service provider
  - emptying operator
  - supervisor
- After emptying : treatment plant
  - help desk
  - service provider
- After disposal
  - help desk
  - servce provider

**Task**

---

* [X] Db : table and sequence
* [X] Header
* [X] Controller
* [X] Mapping of notification
* [X] Dashboard
* [ ] Clear all action
* [ ] Once the user opens make it clear
* [ ] Supervisory also notification
* [ ] Number of message in notification
* [ ] Emptying
* [ ] Fstp
* [ ] Help Desk

**Changes**

---

- database :
  CREATE SEQUENCE notification_id_seq
  START WITH 1
  INCREMENT BY 1
  NO MINVALUE
  NO MAXVALUE
  CACHE 1;

*** Create Table columns user_id, message, mode, status and created_at

CREATE TABLE IF NOT EXISTS public.notification

(

    id integer NOT NULL DEFAULT nextval('notification_id_seq'::regclass),

    user_id integer NOT NULL,

    message character varying(256) COLLATE pg_catalog."default" NOT NULL,

    mode character varying(50) COLLATE pg_catalog."default",

    status boolean,

    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP,

    updated_at timestamp without time zone,

    CONSTRAINT notification_pkey PRIMARY KEY (id)

)

**

- layout\dashboard blade

functionloadNotifications() {

    fetch("/notifications")

    .then(response=>response.json())

    .then(data=> {

    letnotificationIcon=document.getElementById('bell');

    letnotificationList=document.getElementById('notification-list');

    letbadge=document.getElementById('badge');

    notificationList.innerHTML='';

    if (data.length>0) {

    notificationIcon.classList.add('has-notifications');

    badge.style.display='inline'

    data.forEach(item=> {

    constli=document.createElement('li');

    li.textContent=item.message;

    li.onclick= () =>markAsRead(item.id);

    li.style.cursor='pointer';

    li.style.padding='10px';

    li.style.borderBottom='1px solid #ddd';

    notificationList.appendChild(li);

    });

    } else {

    notificationIcon.classList.remove('has-notifications');

    badge.style.display='none';

    notificationIcon.classList.remove('has-notifications');

    badge.style.display='none';

    // Show 'no notifications' message

    constemptyLi=document.createElement('li');

    emptyLi.id='no-notification-text';

    emptyLi.className='text-center text-muted py-3';

    emptyLi.innerHTML=`

    `<i class="fa fa-bell-slash fa-2x mb-2" style="color: #ccc;"></i>``<br>`

    No new notifications

    `;

    notificationList.appendChild(emptyLi);

    }

    });

    }

    functionmarkAsRead(id) {

    fetch('/notification/read', {

    method:'POST',

    headers: {

    'X-CSRF-TOKEN': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),

    'Content-Type': 'application/json'

    },

    body: JSON.stringify({ id:id })

    }).then(() =>loadNotifications());

    }

    setInterval(loadNotifications, 120000);

    document.addEventListener("DOMContentLoaded", loadNotifications);
