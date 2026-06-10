# ================================================
# Python Built-in Functions for Beginners
# ================================================

# Built-in functions are pre-made functions that come with Python
# You don't need to install anything - they're ready to use!


# 1.  - Display output
# ============================

print("Hello, World!")
print("Line 1", "Line 2", "Line 3")  # Multiple arguments
print("Name: Alice", "Age: 25", sep="- ")  # Custom separator


# 2. TYPE() - Check data type
# =============================

print("\n--- TYPE() Function ---")
print(type(42))  # <class 'int'>
print(type(3.14))  # <class 'float'>
print(type("hello"))  # <class 'str'>
print(type([1, 2, 3]))  # <class 'list'>
print(type(True))  # <class 'bool'>
print(type({"name": "Bob"}))  # <class 'dict'>


# 3. LEN() - Get length
# ======================

print("\n--- LEN() Function ---")
text = "Python"
numbers = [10, 20, 30, 40, 50]
fruits = ("apple", "banana", "orange")

numbers.append(3)
fruits = fruits + ("mango",)

print(f"Length of '{text}': {len(text)}")  # 6
print(f"Length of list: {len(numbers)}")  # 5
print(f"Length of tuple: {len(fruits)}")  # 3


# 4. INT(), FLOAT(), STR() - Convert data types
# ===============================================

print("\n--- Conversion Functions ---")

# String to Integer
num_str = "42"
num_int = int(num_str)
print(f"'{num_str}' as integer: {num_int}")

# String to Float
price_str = "19.99"
price_float = float(price_str)
print(f"'{price_str}' as float: {price_float}")

# Integer to String
age = 25
age_str = str(age)
print(f"{age} as string: '{age_str}'")

# Float to Integer (truncates decimal)
temperature = 98.7
temp_int = int(temperature)
print(f"{temperature} as integer: {temp_int}")


# 5. INPUT() - Get user input
# =============================

print("\n--- INPUT() Function ---")
# Uncomment to test:
# user_input = input("Enter your name: ")
# print(f"Hello, {user_input}!")

# Note: input() always returns a string
# age_input = input("Enter your age: ")
# age = int(age_input)  # Convert to integer


# 6. RANGE() - Generate sequences of numbers
# =============================================

print("\n--- RANGE() Function ---")

# Range from 0 to 4
print("Range 0-4:")
for i in range(5):
    print(i, end=" ")


# Range from 2 to 8
print("\nRange 2-8:")
for i in range(2, 9):
    print(i, end=" ")


# Range with step (0, 2, 4, 6, 8)
print("\nRange 0-10 with step 2:")
for i in range(0, 11, 2):
    print(i, end=" ")


# 7. LIST() - Convert to list
# =============================

print("\n--- LIST() Function ---")

# Convert string to list of characters
text = "Python"
text_list = list(text)
print(f"String to list: {text_list}")

# Convert range to list
numbers = list(range(5))
print(f"Range to list: {numbers}")

# Convert tuple to list
my_tuple = (10, 20, 30)
my_list = list(my_tuple)
print(f"Tuple to list: {my_list}")


# 8. MIN(), MAX(), SUM() - Find values
# ======================================

print("\n--- MIN(), MAX(), SUM() Functions ---")

a = 1
b = 2
c = [a, b]

scores = [85, 92, 78, 95, 88]

print(f"Scores: {scores}")
print(f"Minimum: {min(scores)}")
print(f"Maximum: {max(scores)}")
print(f"Sum: {sum(scores)}")

# Works with direct values too
print(f"Min of 5, 2, 8, 1: {min(5, 2, 8, 1)}")
print(f"Max of 5, 2, 8, 1: {max(5, 2, 8, 1)}")


# 9. SORTED() - Sort values
# ===========================

print("\n--- SORTED() Function ---")

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_asc = sorted(numbers)  # Ascending order
sorted_desc = sorted(numbers, reverse=True)  # Descending order

print(f"Original: {numbers}")
print(f"Sorted ascending: {sorted_asc}")
print(f"Sorted descending: {sorted_desc}")

# Sort strings
names = ["Charlie", "Alice", "Bob", "Diana"]
sorted_names = sorted(names)
print(f"Sorted names: {sorted_names}")


# 10. ROUND() - Round numbers
# =============================

print("\n--- ROUND() Function ---")

price = 19.567
rounded = round(price, 2)  # Round to 2 decimal places
print(f"{price} rounded to 2 decimals: {rounded}")

temperature = 98.456
print(f"{temperature} rounded to 1 decimal: {round(temperature, 1)}")
print(f"{temperature} rounded to integer: {round(temperature)}")


# 11. ABS() - Absolute value
# ============================

print("\n--- ABS() Function ---")

numbers = [10, -5, 3, -8, 0]
for num in numbers:
    print(f"Absolute value of {num}: {abs(num)}")


# 12. POW() - Power/Exponent
# ============================

print("\n--- POW() Function ---")

print(f"2 to the power of 3: {pow(2, 3)}")
print(f"5 to the power of 2: {pow(5, 2)}")
print(f"10 to the power of 3: {pow(10, 3)}")


# 13. SUM() WITH DEFAULT - Add numbers
# ======================================

print("\n--- SUM() with Default Value ---")

expenses = [10, 25, 15, 30]
total = sum(expenses)
print(f"Expenses: {expenses}")
print(f"Total: ${total}")

# Sum with starting value
bonus = 100
total_with_bonus = sum(expenses, bonus)
print(f"Total with bonus: ${total_with_bonus}")


# 14. ENUMERATE() - Get index and value
# =======================================

print("\n--- ENUMERATE() Function ---")

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# With starting index
print("\nWith index starting at 1:")
for index, fruit in enumerate(fruits, 1):
    print(f"{index}: {fruit}")


# 15. ZIP() - Combine lists
# ===========================

print("\n--- ZIP() Function ---")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Paris"]

# Combine multiple lists
combined = zip(names, ages, cities)
for name, age, city in combined:
    print(f"{name}, {age} years old, from {city}")


# 16. MAP() - Apply function to all items
# =========================================

print("\n--- MAP() Function ---")


def double(x):
    return x * 2


numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

# Map with lambda (quick anonymous function)
squared = list(map(lambda x: x**2, numbers))
print(f"Squared: {squared}")


# 17. FILTER() - Keep items that match condition
# ================================================

print("\n--- FILTER() Function ---")


def is_even(x):
    return x % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(f"All numbers: {numbers}")
print(f"Even numbers: {even_numbers}")


n = int(input("Int"))
print(list(filter(lambda x: x != n, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


# 18. REVERSED() - Reverse order
# ================================

print("\n--- REVERSED() Function ---")

numbers = [1, 2, 3, 4, 5]
reversed_list = list(reversed(numbers))
print(f"Original: {numbers}")
print(f"Reversed: {reversed_list}")


# 19. ALL() and ANY() - Check conditions
# ========================================

print("\n--- ALL() and ANY() Functions ---")

# ALL() - all items must be True
scores1 = [85, 90, 88]
scores2 = [85, 45, 88]

print(f"All scores in {scores1} >= 80? {all(score >= 80 for score in scores1)}")
print(f"All scores in {scores2} >= 80? {all(score >= 80 for score in scores2)}")

# ANY() - at least one item must be True
print(f"Any score in {scores1} >= 90? {any(score >= 90 for score in scores1)}")
print(f"Any score in {scores2} >= 90? {any(score >= 90 for score in scores2)}")


# 20. ISINSTANCE() - Check if variable is a type
# ================================================

print("\n--- ISINSTANCE() Function ---")

value1 = 42
value2 = "hello"
value3 = [1, 2, 3]

print(f"Is {value1} an integer? {isinstance(value1, int)}")
print(f"Is {value2} a string? {isinstance(value2, str)}")
print(f"Is {value3} a list? {isinstance(value3, list)}")


# 21. PRACTICAL EXAMPLE - Student Grade Analyzer
# ================================================

print("\n--- PRACTICAL EXAMPLE: Grade Analyzer ---")


def analyze_grades(grades):
    """Analyze student grades using built-in functions"""
    if not grades:
        return

    min_grade = min(grades)
    max_grade = max(grades)
    avg_grade = sum(grades) / len(grades)
    passed = sum(1 for g in grades if g >= 70)

    print(f"Total grades: {len(grades)}")
    print(f"Lowest: {min_grade}")
    print(f"Highest: {max_grade}")
    print(f"Average: {round(avg_grade, 2)}")
    print(f"Passed (≥70): {passed}")


student_grades = [85, 92, 78, 95, 88, 65, 91]
analyze_grades(student_grades)

print("\n✓ All built-in functions demonstrated!")
