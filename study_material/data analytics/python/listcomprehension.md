# List comprehension

---


in Python is a concise way to create lists using a single line of code. It is often used for generating new lists by applying an operation to each element in an existing iterable or for filtering elements based on a condition.

**Basic Syntax:**

[expression for item in iterable if condition]
***expression: Operation or value to be added to the new list.
item: Variable representing each element in the iterable.
iterable: The collection (like a list, range, etc.) being iterated over.
condition: (Optional) A filter to include elements only if the condition is True.***


**Examples:**
Generate a list of numbers:

numbers = [x for x in range(10)]
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Square of each number:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


Filter even numbers:
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

**Nested list comprehension (Multiplication table):
table = [[x * y for y in range(1, 6)] for x in range(1, 4)]
print(table)**

Output: [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]

**Convert strings to uppercase:**


words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']

**Numbers divisible by both 3 and 5:**
divisible = [x for x in range(1, 50) if x % 3 == 0 and x % 5 == 0]
print(divisible)  # Output: [15, 30, 45]


***List comprehensions are powerful and improve code readability for simple operations. For complex operations, traditional loops are usually better for clarity.***
