# This covers the classly learned things in here 

# Data

years = [2001, 2002, 2003, 2004, 2005]
apples = [50, 60, 55, 70, 65]
oranges = [40, 50, 45, 60, 55]

# Stacked Bar Plot

plt.bar(years, oranges, width=0.4, color='orange', alpha=0.6, label="Oranges")
plt.bar(years, apples, width=0.4, color='blue', alpha=0.6, bottom=oranges, label="Apples")

# Labels and title

plt.xlabel("Years")
plt.ylabel("Fruit Production")
plt.title("Apples and Oranges Production Over the Years")
plt.legend()
plt.grid(True)

# Show plot

plt.show()

---

# Pivot

---

![1739843784650](image/18febclasslearned/1739843784650.png)

use df.head to print as well

# HeatMap

---

for density
![1739844010883](image/18febclasslearned/1739844010883.png)

* [ ] importances :

![1739844254837](image/18febclasslearned/1739844254837.png)

fmt : d for decimal
can also plot add x and y value titles as well

# import url lib

# url retrieve

---

![1739844985754](image/18febclasslearned/1739844985754.png)

for openening image using PIL


![1739845235302](image/18febclasslearned/1739845235302.png)

pil bata ayeko value chai jahile ni rgb matra hncha
fetches protion 

plt.imshow(img_array[125-300 ,200-400])
arrray ma lagna use numpy array
![1739845915691](image/18febclasslearned/1739845915691.png)

# subplot

![1739846371618](image/18febclasslearned/1739846371618.png)

retruns figre and axes first row count secondly column count fig size : size of entire plot
can control every axes
postion starts from 0
height 

![1739846647016](image/18febclasslearned/1739846647016.png)

# Helper

---

- helps sub plot
- sns.pairplot

  ![1739847255803](image/18febclasslearned/1739847255803.png)
