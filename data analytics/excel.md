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

# - imp pivot table k ho kasari banaune imp question

**## What is a Pivot Table?

A pivot table is a powerful data analysis tool found in spreadsheet applications like Microsoft Excel. It allows users to summarize, analyze, and visualize large datasets interactively. Unlike traditional tables, which present data in a fixed format, pivot tables enable users to rearrange data dynamically, facilitating better insights into relationships between variables. This capability to "pivot" or rotate data makes it easier to compare and contrast different aspects of the dataset without altering the original data source.

## Importance of Pivot Tables

1. Data Summarization: Pivot tables condense large amounts of data into a concise format, making it easier to identify trends and patterns.
2. Interactive Analysis: Users can manipulate the data by dragging and dropping fields, applying filters, and sorting, which enhances exploratory data analysis.
3. Dynamic Reporting: As the underlying data changes, pivot tables can be refreshed to reflect new information without needing to recreate the table.
4. Visual Insights: They can be used alongside pivot charts to create compelling visual representations of data, aiding in decision-making processes[2](https://www.geeksforgeeks.org/pivot-tables-in-excel/)[3](https://www.polymersearch.com/blog/pivot-tables)[4](https://careerfoundry.com/en/blog/data-analytics/how-to-create-a-pivot-table/).

## How to Create a Pivot Table in Excel

Creating a pivot table in Excel involves several straightforward steps:

1. Prepare Your Data: Ensure your dataset is organized in a tabular format with clear headers for each column.
2. Insert the Pivot Table:
   * Go to the Insert tab on the Excel ribbon.
   * Click on PivotTable from the menu.
   * In the dialog box that appears, confirm the selected data range or adjust it if necessary.
   * Choose whether to place the pivot table in a new worksheet or an existing one, then click OK[2](https://www.geeksforgeeks.org/pivot-tables-in-excel/)[4](https://careerfoundry.com/en/blog/data-analytics/how-to-create-a-pivot-table/).
3. 
4. Build Your Pivot Table:

* A PivotTable Field List pane will appear on the right side of your screen.
* Drag and drop fields from this pane into one of four areas: Filters, Columns, Rows, and Values.
* Rows: Place categories you want to analyze.
* Columns: Place categories for comparison.
* Values: Place numerical data you want to summarize (e.g., sums or averages).
* Filters: Add any criteria you want to filter your data by[1](https://study.com/academy/lesson/pivot-table-definition-uses-examples.html)[2](https://www.geeksforgeeks.org/pivot-tables-in-excel/)[5](https://www.javatpoint.com/excel-pivot-table).
* 

1. 
2. Customize Calculations:

* Right-click on any value in the Values area and select Value Field Settings to choose how you want to summarize the data (e.g., Sum, Average, Count) [2](https://www.geeksforgeeks.org/pivot-tables-in-excel/)[4](https://careerfoundry.com/en/blog/data-analytics/how-to-create-a-pivot-table/).

1. 
2. Finalize Your Pivot Table:

* Adjust formatting as needed and explore different views by dragging fields around or applying filters.

By following these steps, you can effectively create a pivot table that transforms raw data into actionable insights, enhancing your analytical capabilities within Excel.

Share

**

# msdos

index match

---

### Using `INDEX-MATCH` in Excel

The `INDEX-MATCH` combination is a powerful alternative to `VLOOKUP` and `HLOOKUP` for data lookups in Excel. It offers more flexibility and avoids limitations like requiring the lookup value to be in the first column.

---

#### **Syntax**

1. **`INDEX` Function**
   * **Formula** : `=INDEX(array, row_num, [column_num])`
   * **Purpose** : Returns the value of a cell within a specific range, based on row and column numbers.
2. **`MATCH` Function**
   * **Formula** : `=MATCH(lookup_value, lookup_array, [match_type])`
   * **Purpose** : Returns the relative position of a lookup value in a row or column.
3. **Combining `INDEX` and `MATCH`**
   * **Formula** : `=INDEX(range, MATCH(lookup_value, lookup_array, match_type), column_number)`
   * **Purpose** : Finds a value based on criteria.

---

#### **Example of `INDEX-MATCH`**

Suppose you have the following table:

| **A** | **B** | **C** |
| ----------- | ----------- | ----------- |
| Product     | Category    | Price       |
| Apple       | Fruit       | 2.00        |
| Carrot      | Vegetable   | 1.50        |
| Banana      | Fruit       | 1.20        |

* **Goal** : Find the price of "Banana."

1. Use `MATCH` to find the row number of "Banana":

   <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">excel</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-excel">=MATCH("Banana", A2:A4, 0)
   </code></div></div></pre>

   This will return `3`.
2. Use `INDEX` to get the price based on the row number:

   <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">excel</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-excel">=INDEX(C2:C4, 3)
   </code></div></div></pre>

   This will return `1.20`.
3. Combine `INDEX` and `MATCH`:

   <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">excel</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-excel">=INDEX(C2:C4, MATCH("Banana", A2:A4, 0))
   </code></div></div></pre>

   This will dynamically return `1.20`

# macros - repetitve task

---

Macros are used to automate repetitive tasks in Excel using VBA (Visual Basic for Applications).

#### **Enabling Macros**

1. Go to  **File > Options > Trust Center > Trust Center Settings** .
2. Click **Macro Settings** and enable macros.

#### **Creating a Macro**

1. Press `Alt + F11` to open the VBA editor.
2. Insert a new module:  **Insert > Module** .
3. Write your macro code. Example:
   <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">vba</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-vba">Sub HelloWorld()
       MsgBox "Hello, World!"
   End Sub
   </code></div></div></pre>
4. Save your workbook as **Excel Macro-Enabled Workbook** (`*.xlsm`).
5. Run the macro via **Developer > Macros** or by assigning it to a button.

---

#### **Example Macro to Automate `INDEX-MATCH`**

If you often perform `INDEX-MATCH`, you can create a macro for it.

1. Open the VBA editor (`Alt + F11`).
2. Paste this code into a module:
   <pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">vba</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1" aria-label="Copy"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>Copy code</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-vba">Sub IndexMatchExample()
       Dim ws As Worksheet
       Set ws = ThisWorkbook.Sheets("Sheet1") ' Change "Sheet1" to your sheet name

       Dim lookupValue As String
       lookupValue = InputBox("Enter the lookup value:")

       Dim result As Variant
       result = Application.WorksheetFunction.Index(ws.Range("C2:C4"), _
                 Application.WorksheetFunction.Match(lookupValue, ws.Range("A2:A4"), 0))

       MsgBox "The result is: " & result
   End Sub
   </code></div></div></pre>
3. Run the macro and enter the lookup value (e.g., "Banana").

# conditional formatting

---
