# Requirements for dncc

---

- Update look up value for structure type
- Review building and cotainment database and ensure all these changes are visible in Add/Edit/Show

  - Add new columns (take maharshi dai's passed excel as a reference )

  | Road Name                                                                  |                                                          |
  | -------------------------------------------------------------------------- | -------------------------------------------------------- |
  | Block Number                                                               |                                                          |
  | House Number                                                               | Already in DB;``Road Code, Road Name, Block Number…     |
  | Water Bill Payment Status                                                  | Options: Yes/No/NA; If Water Supply is City Water Supply |
  | WASA Bill Payment Status                                                   | Options: Yes/No/NA; If Any sewer connection              |
  | IF                                                                         |                                                          |
  | Either Water Bill Payment Status or WASA Bill Payment status is true, then |                                                          |
  | WASA Bill No.                                                              |                                                          |
  | (SewerCode)/(Drain                                                         |                                                          |
  | Code)/ Water Suppy Pipeline Code -> Fields are non mandatory except road   |                                                          |
  | code                                                                       |                                                          |
- Service Provider Module :

  - Add new field "Contract Document"
  - PDF Upload with limit of 5 mb
  - Edit and View should be updated accordingly.

  ## Mobile App

  ---


  1. Update Building Information

  - Same as building form form web to mobile app

    2.Supervisory Assessment
    -

| Area Name                      | View Only                                                                |
| ------------------------------ | ------------------------------------------------------------------------ |
| Block Number                   | View Only                                                                |
| Road Number/ Road Name         | View Only                                                                |
| Road Code                      | View Only                                                                |
| Building Number                | View Only                                                                |
| Owner Name                     | View Only                                                                |
| Owner Gender                   | View Only                                                                |
| Owner Contact                  | View Only                                                                |
|                                |                                                                          |
| Building Toilet Connection     | Dropdown/ Based on IMIS/ Prefilled                                       |
| Containment Type               | Follow same logic as Building Add form, if there is containment, prefill |
| it, else blank                 |                                                                          |
| Containment Volume             | Mandatory if containment                                                 |
| Containment Construction Date  | Mandatory if containment                                                 |
| Road Width                     | Ensure this value is visible to SP and ETO in Mobile app and web app     |
| Distance from Nearest          |                                                                          |
| Motorable Road                 | Ensure this value is visible to SP and ETO in Mobile app and web app     |
| Appropriate Desludging Vehicle |                                                                          |
| Size                           | Ensure this value is visible to SP and ETO in Mobile app and web app     |
| Confirmed Emptying Date        | Ensure this value is visible to SP and ETO in Mobile app and web app     |
| Advance Paid Amount            | Ensure this value is visible to SP and ETO in Mobile app and web app     |
| Advance Payment Receipt        |                                                                          |

    Emptying Form :

| Mobile App                                                                                        |
| ------------------------------------------------------------------------------------------------- |
| Total Cost                                                                                        |
| Change                                                                                            |
| to:``Advance Paid Amount: (Prefilled)``Additional Payment: (accept 0 if no          |
| additional payment, but should be not null.``Total Paid Amount: Sum of A and B (prefilled) |

- Sanitation System Category : Display as category in read only as per following category and also needs to eb saved the data in database 

| Toilet Connection               | Category                    |
| ------------------------------- | --------------------------- |
| Sewer Network                   | WASA Sewerage Connection    |
| Drain Network                   | Directly Connected to Drain |
| Septic Tank                     |                             |
| Pit/ Holding Tank               | Non-Functional Septic Tank  |
| Onsite Treatment (Anaerobic     |                             |
| Digestor/ Biogas, DEWATS, etc.) | Onsite Treatment            |
| Composting Toilets (Ecosan,     |                             |
| UDDT, etc.)                     | Onsite Treatment            |
| Water Body                      | Directly Connected to Drain |
| Open Ground                     | Directly Connected to Drain |
| Community Toilet                |                             |
| Open Defecation                 |                             |
| Shared Toilets                  |                             |
| Shared Containment              |                             |
| Containment Outlet Connection   |                             |
| (If Containment)                | Category                    |
| Septic Tank connected to Sewer  |                             |
| Network                         | WASA Sewerage Connection    |
| Septic Tank connected to Drain  |                             |
| Network                         | Non-Functional Septic Tank  |
| Septic Tank connected to Soak   |                             |
| Pit                             | Functional Septic Tank      |
| Septic Tank connected to Water  |                             |
| Body                            | Non-Functional Septic Tank  |
| Septic Tank connected to Open   |                             |
| Ground                          | Non-Functional Septic Tank  |
| Septic Tank without Outlet      |                             |
| Connection                      | Non-Functional Septic Tank  |
| Septic Tank with Unknown        |                             |
| Outlet Connection               | Non-Functional Septic Tank  |
| Lined Pit connected to a Soak   |                             |
| Pit                             | Non-Functional Septic Tank  |
| Lined Pit connected to Water    |                             |
| Body                            | Non-Functional Septic Tank  |
| Lined Pit connected to Open     |                             |
| Ground                          | Non-Functional Septic Tank  |
| Lined Pit connected to Sewer    |                             |
| Network                         | WASA Sewerage Connection    |
| Lined Pit connected to Drain    |                             |
| Network                         | Non-Functional Septic Tank  |
| Lined Pit without Outlet        | Non-Functional Septic Tank  |
| Lined Pit with Unknown Outlet   |                             |
| Connection                      | Non-Functional Septic Tank  |
| Lined Pit with Impermeable      |                             |
| Walls and Open Bottom           | Non-Functional Septic Tank  |
| Double Pit                      | Non-Functional Septic Tank  |
| Permeable/ Unlined Pit          | Non-Functional Septic Tank  |

- Site Setting :

- [ ] Auto Assign Service Provider (yes/no) -> should also need a db change +

* [ ] If yes then Service Provider selectable
* [ ] If no then Service Provider auto assign as per the selected (Can take birendranagar as a reference)
