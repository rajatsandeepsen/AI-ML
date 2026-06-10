# ============================================
# Python Basics for Beginners
# ============================================

# 1. VARIABLES AND DATA TYPES
# =============================

# String - text enclosed in quotes
from typing import List

name = "Alice" + "Dony"
print(name)

# Integer - whole numbers
age = 25
year = 2024

# Float - decimal numbers
height = 5.7
temperature = 98.6

# Boolean - True or False
is_student = True
is_raining = False

print(f"My name is {name}, I am {age} years old")
print(f"Height: {height}, Temperature: {temperature}")


# 2. BASIC OPERATIONS
# ====================

# Arithmetic operations
num1 = 10
num2 = 3

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
integer_division = num1 // num2
remainder = num1 % num2

print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {integer_division}")
print(f"{num1} % {num2} = {remainder}")


# 3. CONDITIONALS (IF/ELSE)
# ==========================

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# Comparison operators
x = 5
y = 10

if x < y:
    print(f"{x} is less than {y}")

if x != y:
    print(f"{x} is not equal to {y}")


# 4. LISTS (Collections of items)
# ================================

fruits = ["apple", "banana", "orange", "mango"]
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Add item to list
print(f"Numbers: {numbers}")


# 5. LOOPS
# ========

# FOR LOOP - repeat a specific number of times
print("\nFor Loop - Counting:")
for i in range(5):
    print(f"Count: {i}")

# FOR LOOP - iterate through a list
print("\nFor Loop - Through list:")
for fruit in fruits:
    print(f"I like {fruit}")

# WHILE LOOP - repeat until condition is false
print("\nWhile Loop:")
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1


# 6. FUNCTIONS
# ============


def greet(person_name: List[str]):
    """Function that greets someone"""
    return f"Hello, {person_name}!"


result = greet(["bob"])
print(result)


def add_numbers(a: int, b: int) -> int:
    """Hello"""

    total = a + b
    return total


sum_result = add_numbers(7, 3)
print(f"7 + 3 = {sum_result}")


def multiply(x, y):
    """Function that multiplies two numbers"""
    return x * y


print(multiply(4, 5))


# 7. DICTIONARIES (Key-value pairs)
# ==================================

person = {
    "name": "Charlie",
    "age": 30,
    "city": "New York",
    "is_developer": True,
}

person["age"] += 3

print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")


# 8. USER INPUT
# =============

# Uncomment to test user input:
age = float(input("What is your age? "))
print(f"Nice to meet you, {type(age)}!")


# 9. SIMPLE PROGRAM - CALCULATOR
# ===============================


def simple_calculator(num1, num2, operation):
    """Basic calculator for beginners"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Unknown operation"


print(f"\nCalculator: 15 + 5 = {simple_calculator(15, 5, '+')}")
print(f"Calculator: 20 - 8 = {simple_calculator(20, 8, '-')}")
print(f"Calculator: 6 * 4 = {simple_calculator(6, 4, '*')}")
print(f"Calculator: 30 / 6 = {simple_calculator(30, 6, '/')}")


# 10. COMMENTS AND BEST PRACTICES
# ================================

# Use meaningful variable names
user_age = 25  # Good
ua = 25  # Bad - not clear

# Variables should be lowercase with underscores
my_variable = 10


# Functions should describe what they do
def calculate_tax(amount):
    return amount * 0.10


print(f"Tax on $100: ${calculate_tax(100)}")

print("\n✓ All basic concepts demonstrated!")
