"""
Functions and Lambdas in Python
"""

from functools import reduce
from typing import Any, Callable, List, Tuple


# Basic function
def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet("Alice"))


# Function with default parameters
def add(a: int, b: int = 10) -> int:
    return a + b


print(add(5))
print(add(5, 3))


# Function with multiple return values
def get_min_max(numbers: List[int]) -> Tuple[int, int]:
    return min(numbers), max(numbers)


result = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(result)
min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {min_val}, Max: {max_val}")


# Function with variable arguments (*args)
def sum_all(*args: int) -> int:
    return sum(args)


print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5))


# Function with keyword arguments (**kwargs)
def print_info(**kwargs: Any) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=25, city="New York")


# Function with *args and **kwargs
def print_details(*args: Any, **kwargs: Any) -> None:
    print("Args:", args)
    print("Kwargs:", kwargs)


print_details(1, 2, 3, name="Alice", age=25)


# Positional-only parameters (Python 3.8+)
# Parameters before / can ONLY be passed positionally
def divide(a: float, b: float, /) -> float:
    return a / b


print(divide(10, 2))
# print(divide(a=10, b=2))  # Error - can't use keyword arguments with /


# Keyword-only parameters
# Parameters after * MUST be passed by keyword
def describe(name: str, *, age: int, city: str) -> str:
    return f"{name} is {age} years old and lives in {city}"


print(describe("Alice", age=25, city="New York"))
# print(describe("Alice", 25, "New York"))  # Error - age and city must be keywords


# Positional-only and keyword-only together
def complex_func(a: int, b: int, /, c: int, *, d: int) -> int:
    return a + b + c + d


print(
    complex_func(1, 2, 3, d=4)
)  # a,b positional only, c either, d keyword only

# Lambda functions (anonymous functions)
square = lambda x: x**2
print(square(5))

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))

# Lambda with default arguments
add_default = lambda x, y=10: x + y
print(add_default(5))
print(add_default(5, 3))

# Using map with lambda
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Using filter with lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Using sorted with lambda
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "Diana", "score": 95},
]
sorted_by_score = sorted(students, key=lambda x: x["score"])
print(sorted_by_score)


# Nested function (closure)
def outer(x: int) -> Callable[[int], int]:
    def inner(y: int) -> int:
        return x + y

    return inner


add_5 = outer(5)
print(add_5(10))
print(add_5(20))


# Function decorators - modify function behavior
def decorator(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result

    return wrapper


@decorator
def say_hello(name: str) -> str:
    return f"Hello, {name}!"


print(say_hello("Alice"))


# Decorator with arguments
def repeat(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> List[Any]:
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results

        return wrapper

    return decorator


@repeat(times=3)
def greet_repeat(name: str) -> str:
    return f"Hello, {name}!"


print(greet_repeat("Alice"))


# Docstrings
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle

    Returns:
        The area of the circle
    """
    return 3.14159 * radius**2


print(calculate_area(5))
print(calculate_area.__doc__)


# Type hints
def add_typed(a: int, b: int) -> int:
    return a + b


print(add_typed(5, 3))


# Function with type hints for lists
def sum_list(numbers: List[int]) -> int:
    return sum(numbers)


print(sum_list([1, 2, 3, 4, 5]))

# Using reduce with lambda
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

# List comprehension vs map/lambda
numbers = [1, 2, 3, 4, 5]
squared_comp = [x**2 for x in numbers]
squared_lambda = list(map(lambda x: x**2, numbers))
print(squared_comp)
print(squared_lambda)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)


# Generator function - lazy evaluation, memory efficient
def count_up_to(n: int):
    i = 1
    while i <= n:
        yield i
        i += 1


for num in count_up_to(5):
    print(num)


# Function with recursion
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


# Higher-order function (function that returns a function)
def make_multiplier(n: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * n

    return multiplier


times_3 = make_multiplier(3)
print(times_3(10))

# Using any() and all() with lambda
numbers = [2, 4, 6, 8, 10]
all_even = all(lambda x: x % 2 == 0 for x in numbers)
print(all_even)

# Using min/max with lambda
data = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20},
]
oldest = max(data, key=lambda x: x["age"])
youngest = min(data, key=lambda x: x["age"])
print(f"Oldest: {oldest}")
print(f"Youngest: {youngest}")


# Special feature: *args unpacking
def print_all(a: int, b: int, c: int) -> None:
    print(f"a={a}, b={b}, c={c}")


args = [1, 2, 3]
print_all(*args)  # Unpacks list into individual arguments


# Special feature: **kwargs unpacking
def print_person(name: str, age: int, city: str) -> None:
    print(f"{name}, {age}, {city}")


person_dict = {"name": "Alice", "age": 25, "city": "NYC"}
print_person(**person_dict)  # Unpacks dict into keyword arguments

# Special feature: Walrus operator := (Python 3.8+)
# Assigns and returns value in one expression
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List has {n} elements")

# Special feature: Default mutable argument gotcha (avoid!)
# DON'T do this:
# def bad_append(item, lst=[]):
#     lst.append(item)
#     return lst


# DO this instead:
def good_append(item: int, lst: List[int] = None) -> List[int]:
    if lst is None:
        lst = []
    lst.append(item)
    return lst


print(good_append(1))
print(good_append(2))


# Special feature: Function annotations (metadata)
def annotated(x: int, y: str) -> bool:
    return len(y) > x


print(annotated.__annotations__)

# Special feature: functools.wraps preserves original function metadata
from functools import wraps


def my_decorator(func: Callable) -> Callable:
    @wraps(func)  # Preserves func's name, docstring, etc
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def important_function(x: int) -> int:
    """This is important"""
    return x * 2


print(important_function.__name__)  # Shows 'important_function', not 'wrapper'


# Special feature: *args with positional-only to prevent mistakes
def safe_greet(greeting: str, /, *names: str) -> None:
    for name in names:
        print(f"{greeting}, {name}!")


safe_greet("Hello", "Alice", "Bob", "Charlie")
# safe_greet(greeting="Hello", "Alice")  # Error - can't mix positional-only with keywords
