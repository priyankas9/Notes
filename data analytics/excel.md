# 17/12/2024 Tuesday

---

# - chap 1,2(30),tableu,r,excel(70) midterm

- good visLIZAION, TRAITS,EXCELLENCE
- chap 1 and 2 imp
- excel function: count -> number
- counta
- countify
- vlookup
- indexmatch
- table

# VLookUp

---

- vertically loop garne
- The **VLOOKUP** function is a premade function in Excel, which allows searches across columns.

  It is typed `=VLOOKUP` and has the following parts:

  =VLOOKUP( **lookup_value** ,  **table_array** ,  **col_index_num** , [ **range_lookup** ])

* There are four pieces of information that you will need in order to build the VLOOKUP syntax:

1. The value you want to look up, also called the lookup value.
2. The range where the lookup value is located. Remember that the lookup value should always be in the first column in the range for VLOOKUP to work correctly. For example, if your lookup value is in cell C2 then your range should start with C.
3. The column number in the range that contains the return value. For example, if you specify B2:D11 as the range, you should count B as the first column, C as the second, and so on.
4. Optionally, you can specify TRUE if you want an approximate match or FALSE if you want an exact match of the return value. If you don't specify anything, the default value will always be TRUE or approximate match.

   **Limitation**

* VLook up cant go left cause u right ma amtra janca
* duplicate value cha bahen first record nai pass garcha

XLOOKUP SOLUTION for vlookp

# Approx Match

---

- **assumes the first column in the table is sorted either numerically or alphabetically, and will then search for the closest value** .

# Xlookup

---

- approx match different huncha
- All  direc tional
- 2019 v only

# Match

---

The *MATCH function searches for a specified item in a range of cells, and then returns the relative position of that item in the range* .

# Index

---

The **`INDEX`** function in Excel is used to return a value or the reference to a value within a specific range or table.

### **1. COUNT()**

 **Purpose** : Counts **numeric values** in a range (ignores text, blanks, or logical values).
 **Syntax** : `=COUNT(range)`
 **Example** :

* `=COUNT(A1:A10)`
  If A1:A10 contains: 5, 10, "", 15, "Text", 20 → **Result = 4** (only numbers are counted).

---

### **2. COUNTA()**

 **Purpose** : Counts the number of **non-empty** cells (includes text, numbers, and formulas).
 **Syntax** : `=COUNTA(range)`
 **Example** :

* `=COUNTA(A1:A10)`
  If A1:A10 contains: 5, 10, "", "Text", 20 → **Result = 4** (ignores blanks but includes text and numbers).

---

### **3. COUNTBLANK()**

 **Purpose** : Counts the number of **blank cells** in a range.
 **Syntax** : `=COUNTBLANK(range)`
 **Example** :

* `=COUNTBLANK(A1:A10)`
  If A1:A10 contains: 5, "", 10, "", "Text" → **Result = 2** (counts empty cells only).

---

### **4. COUNTIF()**

 **Purpose** : Counts the cells in a range that meet a  **single condition** .
 **Syntax** : `=COUNTIF(range, condition)`
 **Example** :

* `=COUNTIF(A1:A10, ">50")`
  If A1:A10 contains: 30, 60, 40, 80 → **Result = 2** (values > 50 are counted).
* `=COUNTIF(A1:A10, "Text")`
  Counts cells containing the word "Text".

---

### **5. COUNTIFS()**

 **Purpose** : Counts the cells that meet **multiple conditions** across ranges.
 **Syntax** : `=COUNTIFS(range1, condition1, range2, condition2, ...)`
 **Example** :

* `=COUNTIFS(A1:A10, ">50", B1:B10, "Yes")`
  A1:A10 contains: 60, 40, 80; B1:B10 contains: "Yes", "No", "Yes" → **Result = 2**
  (Counts cells where A > 50 AND corresponding B = "Yes").

---

### **6. IF()**

 **Purpose** : Checks a condition and returns one value if TRUE and another if FALSE.
 **Syntax** : `=IF(condition, value_if_true, value_if_false)`
 **Example** :

* `=IF(A1>50, "Pass", "Fail")`
  If A1 = 70 → **Result = "Pass"**
  If A1 = 40 → **Result = "Fail"**
* **Nested IF Example** :
  `=IF(A1>50, "Pass", IF(A1>30, "Average", "Fail"))`
  Handles multiple conditions.

---

### **7. LEN()**

 **Purpose** : Returns the number of characters in a text string (including spaces).
 **Syntax** : `=LEN(text)`
 **Example** :

* `=LEN("Excel Fun")` → **Result = 9**
* `=LEN(A1)`
  If A1 = "Hello World" →  **Result = 11** .

---

### **8. TRIM()**

 **Purpose** : Removes all **extra spaces** in a text string except single spaces between words.
 **Syntax** : `=TRIM(text)`
 **Example** :

* `=TRIM(" Hello Excel ")` → **Result = "Hello Excel"**
* `=TRIM(A1)`
  If A1 = " Data Science " → Result: **"Data Science"**

---

### **9. CONCATENATE()** *(or CONCAT in newer Excel)*

 **Purpose** : Joins multiple text strings into one.
 **Syntax** :

* `=CONCATENATE(text1, text2, ...)`
* **Newer Excel** : Use `=CONCAT(text1, text2, ...)`

 **Example** :

* `=CONCATENATE(A1, " ", B1)`
  If A1 = "Hello" and B1 = "World" →  **Result = "Hello World"** .
* **Alternative** : Use the `&` operator:
  `=A1 & " " & B1` → Combines A1 and B1 with a space.

# 31/12/2024 december tuesday 

---

- pivot table and charts
