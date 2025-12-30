# PDF GENERATION

---

* [X] Rename page name pdf generation to Notice Generation
  Rename button name create new pdf data to create new notice data

  **Add from**
* [X] Add new fields : Signatory (Digital Signature)

  **requirement Signatory :**
* [X] png
* [X] 2mb
* [X] encrypted storage -> base 64
* [X] decrypt for fetch
  **Signatory Details**
* [X] Name
* [X] Position
* [X] Footer
* [ ] When saving the digital signature save it in base64 and use application key to encryt and decryt dor ecurity

  **Action**
* [X] rename action pdf generation to generate notice
* [X] when user clicks on the button : display a pop up modal
* [X] Heading : Filter Buildings :
* [X] Ward : Dropdown of ward
* [X] Block Number : ILIKE
* [X] Area Name : ILIKE
* [X] House Number
* [X] BIN
* [X] Category : dropdown
* [X] Reanme the pdf/pdf-generation route to notice/notice-generation
* [X] Button : Filter

  - The filtered Buildings must be in queue format since we don't know what will the number of the buildings that will be filetered
    - After the filer button is clicked pass it to a different view with filtered table and more records
    - And the fucntion to geenerate the pdf for this should be runned in background
* [ ] Form fields hierarchy chnages
* [ ] Notice Layout fixes
* [ ] Input accept p tags and all
* [ ] Preview of notice
* [ ] pdf to PDF

**Code changes**

---

* [X] Generate notice button ->pop up filter form
* [X] In popup form rename filter to generate
* [X] Once the user clicks on the generate button throw to another data table fields :

  - ID
  - Notice Generation Date
  - Filters
  - Actions :

    - Donwload Notice ( disabled until file is reeady)
      - View Buildings
* [X] As user  clicks on the another page or the generate button make a new record in table generated_notice of who filtered what and all
  **Quick Changes

  - [X] first action notice generation clcik lead to generated notice page **
  - [X] in Generated notice page add new button as download new notice
  - [X] and after geberate redirect to same oage with new records
  - [X] add new action in view buildings as view response
  - [X] in filter popup add multi select in ward
  - [ ] As soon as user click on dwonload notice he / she should download the notice of the previously selected unique reference number and all

# Change Map

---

* [X] Add new columns in db :
* [X] digital_signature
* [X] signatory_name
* [X] signatory_position
* [X] footer
* [X] database : new table named: generatednotice

  - added fileds : id,user_id , notice\_generation_date,filters

# DB Query

---

ALTER TABLE pdf_body_data
ADD COLUMN digital_signature VARCHAR(255) NULL,
ADD COLUMN signatory_name VARCHAR(255) NULL,
ADD COLUMN signatory_position VARCHAR(255) NULL,
ADD COLUMN footer TEXT NULL;

//Table : Genrated-notice

CREATE SEQUENCE generatednotice_id_seq
    START 1
    INCREMENT 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

CREATE TABLE generatednotice (
    id INTEGER NOT NULL DEFAULT nextval('generatednotice_id_seq'::regclass) PRIMARY KEY,
    user_id INTEGER NULL,
    notice_generation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    filters TEXT,
pdf_generation_id integer
);

ALTER SEQUENCE generatednotice_id_seq OWNED BY generatednotice.id;
