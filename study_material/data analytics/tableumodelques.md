## **1. Theoretical Questions**

### **Q1: What is Tableau, and why is it used for data visualization?**

**Answer:** Tableau is a **data visualization** and **business intelligence** tool that helps users analyze data through interactive dashboards, reports, and charts. It enables non-technical users to explore data and derive insights using a **drag-and-drop** interface without coding.

---

### **Q2: Explain the different file types used in Tableau.**

**Answer:**

* **.twb (Tableau Workbook):** Contains visualization details but does **not** store data.
* **.twbx (Tableau Packaged Workbook):** Contains both visualization and **data** (useful for sharing).
* **.tds (Tableau Data Source):** Stores data connection details but does not contain data.
* **.tde (Tableau Data Extract):** A compressed snapshot of data optimized for performance.
* **.hyper (Hyper Extract):** A more advanced and faster data extract format introduced in Tableau 10.5.

---

### **Q3: What are the types of data connections available in Tableau?**

**Answer:**
Tableau supports two types of data connections:

1. **Live Connection** – Directly connects to a database (e.g., SQL, Oracle) and retrieves **real-time** data.
2. **Extract Connection** – Takes a **snapshot** of data and stores it locally for faster performance.

---

### **Q4: What is the difference between Measures and Dimensions?**

**Answer:**

* **Measures** – Numerical values that can be **aggregated** (e.g., Sales, Profit, Quantity).
* **Dimensions** – Categorical data used for **grouping** or **filtering** (e.g., Region, Product, Category).

---

### **Q5: What are the different types of joins in Tableau?**

**Answer:**

1. **Inner Join** – Returns matching records in both tables.
2. **Left Join** – Returns all records from the left table and matching records from the right table.
3. **Right Join** – Returns all records from the right table and matching records from the left table.
4. **Full Outer Join** – Returns all records from both tables, filling missing values with NULL.

---

### **Q6: What is Data Blending, and how is it different from Joins?**

**Answer:**
**Data Blending** is used when **data comes from different sources** (e.g., SQL and Excel) and cannot be joined. It creates a **temporary relationship** between datasets.

 **Joins** , on the other hand, work within the **same database** and combine tables based on a common key.

---

### **Q7: What are Level of Detail (LOD) Expressions in Tableau?**

**Answer:**
LOD expressions allow users to calculate **aggregations** at different levels of granularity.

* **Fixed:** `{ FIXED [Region] : SUM(Sales) }` → Aggregates at the Region level.
* **Include:** `{ INCLUDE [Category] : SUM(Sales) }` → Includes additional fields in aggregation.
* **Exclude:** `{ EXCLUDE [State] : SUM(Sales) }` → Removes specific fields from aggregation.

---

## **2. Practical & Application-Based Questions**

### **Q8: How do you connect a dataset to Tableau?**

**Answer:**

1. Open Tableau.
2. Click **"Connect to Data"** and select the **data source** (Excel, SQL, etc.).
3. Drag the table or data sheet onto the  **Canvas** .
4. Click **"Go to Worksheet"** to start visualizing data.

---

### **Q9: What are the steps to create a bar chart in Tableau?**

**Answer:**

1. Drag a **dimension** (e.g., "Category") to the **Columns** shelf.
2. Drag a **measure** (e.g., "Sales") to the **Rows** shelf.
3. Click on the chart type and select  **Bar Chart** .

---

### **Q10: How do you create filters in Tableau?**

**Answer:**

1. Drag a **dimension** (e.g., "Region") to the **Filters** shelf.
2. Choose the values to filter.
3. Click **"Show Filter"** to add an interactive filter to the dashboard.

---

### **Q11: What are Hierarchies and Sets in Tableau?**

**Answer:**

* **Hierarchies** allow grouping fields in a drill-down structure (e.g., Country → State → City).
* **Sets** are **custom-defined** subsets of data used for filtering and analysis.

---

### **Q12: How do you create a Calculated Field in Tableau?**

**Answer:**

1. Click **Analysis** →  **Create Calculated Field** .
2. Enter a formula (e.g., `Profit Margin = SUM(Profit) / SUM(Sales)`).
3. Click  **OK** , and use the field in your visualization.

---

### **Q13: How do you apply Parameters in a Visualization?**

**Answer:**

1. Click **Create Parameter** in the Data Pane.
2. Set the **data type** (e.g., integer, string).
3. Use the parameter in a **calculated field** (e.g., `IF [Sales] > [Parameter] THEN "High" ELSE "Low"`).

---

### **Q14: Explain how Mapping works in Tableau.**

**Answer:**

1. Drag a geographic field (e.g., "Country") to the **Rows or Columns** shelf.
2. Tableau automatically assigns  **latitude and longitude** .
3. Choose **Map** as the visualization type.

---

## **3. Dashboard & Storytelling Questions**

### **Q15: What are the best practices for creating an effective dashboard?**

**Answer:**

* Keep it **simple** and  **interactive** .
* Use **consistent color schemes** and avoid clutter.
* Include **filters and tooltips** for better interactivity.
* Ensure **fast performance** by limiting  **data extracts** .

---

### **Q16: What is the difference between a Dashboard and a Story in Tableau?**

**Answer:**

* **Dashboard** : A collection of multiple visualizations in one view.
* **Story** : A **sequence of visualizations** (like PowerPoint slides) used for storytelling.

---

### **Q17: How do you create an Interactive Dashboard in Tableau?**

**Answer:**

1. Click **"New Dashboard"** in the bottom pane.
2. Drag **multiple worksheets** onto the dashboard.
3. Add **Filters, Actions, and Parameters** for interactivity.

---

### **Q18: What are Actions in a Dashboard?**

**Answer:**
Actions allow user interaction in a dashboard:

* **Filter Action** – Clicking on one visualization filters another.
* **Highlight Action** – Highlights related data points.
* **URL Action** – Opens a web page when clicking a visualization.

---

## **4. Scenario-Based Questions**

### **Q19: How would you visualize sales data for different regions?**

**Answer:**
Use a **Map Chart** with **color coding** or a **Bar Chart** showing sales per region.

---

### **Q20: How do you filter data for specific years and regions?**

**Answer:**
Use a **Date Filter** (drag Date field to Filter shelf) and a  **Region Filter** .

---

### **Q21: If you want to compare sales trends over time, what chart should you use?**

**Answer:**
A **Line Chart** showing Sales vs. Time (drag Date to Columns and Sales to Rows).

---

### **Q22: How would you present "Sales vs. Profit by Category"?**

**Answer:**
Use a **Side-by-Side Bar Chart** or a **Scatter Plot** (Sales on X-axis, Profit on Y-axis).
