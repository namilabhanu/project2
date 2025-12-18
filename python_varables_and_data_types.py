#!/usr/bin/env python3
"""
Python Data Types Demonstration
This script showcases all major data types available in Python
"""

print("=" * 60)
print("PYTHON DATA TYPES COMPREHENSIVE GUIDE")
print("=" * 60)

# 1. NUMERIC TYPES
print("\n1. NUMERIC TYPES")
print("-" * 20)

# Integer
age = 25
negative_num = -10
large_num = 1000000
print(f"Integer: {age}, type: {type(age)}")
print(f"Negative: {negative_num}, Large: {large_num}")

# Float
price = 99.99
scientific = 1.5e-4
infinity = float('inf')
print(f"Float: {price}, type: {type(price)}")
print(f"Scientific: {scientific}, Infinity: {infinity}")

# Complex
complex_num = 3 + 4j
print(f"Complex: {complex_num}, type: {type(complex_num)}")
print(f"Real part: {complex_num.real}, Imaginary: {complex_num.imag}")

# 2. SEQUENCE TYPES
print("\n2. SEQUENCE TYPES")
print("-" * 20)

# String
name = "Python Programming"
multiline = """This is a
multiline string"""
raw_string = r"C:\Users\name\file.txt"
print(f"String: '{name}', type: {type(name)}")
print(f"Length: {len(name)}, Upper: {name.upper()}")
print(f"Raw string: {raw_string}")

# List (mutable)
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]
print(f"List: {fruits}, type: {type(fruits)}")
print(f"Mixed list: {mixed_list}")
print(f"Nested list: {nested_list}")

# Tuple (immutable)
coordinates = (10, 20)
single_tuple = (42,)  # Note the comma
empty_tuple = ()
print(f"Tuple: {coordinates}, type: {type(coordinates)}")
print(f"Single tuple: {single_tuple}, Empty: {empty_tuple}")

# Range
number_range = range(1, 10, 2)
print(f"Range: {number_range}, type: {type(number_range)}")
print(f"Range list: {list(number_range)}")

# 3. MAPPING TYPE
print("\n3. MAPPING TYPE")
print("-" * 20)

# Dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "JavaScript"]
}
nested_dict = {
    "user1": {"name": "John", "score": 95},
    "user2": {"name": "Jane", "score": 87}
}
print(f"Dictionary: {person}, type: {type(person)}")
print(f"Name: {person['name']}, Skills: {person.get('skills')}")
print(f"Nested dict: {nested_dict}")

# 4. SET TYPES
print("\n4. SET TYPES")
print("-" * 20)

# Set (mutable, unordered, unique elements)
colors = {"red", "green", "blue", "red"}  # duplicate "red" will be removed
empty_set = set()
print(f"Set: {colors}, type: {type(colors)}")
print(f"Length: {len(colors)}")

# Frozenset (immutable set)
frozen_colors = frozenset(["red", "green", "blue"])
print(f"Frozenset: {frozen_colors}, type: {type(frozen_colors)}")

# 5. BOOLEAN TYPE
print("\n5. BOOLEAN TYPE")
print("-" * 20)

is_active = True
is_complete = False
print(f"Boolean True: {is_active}, type: {type(is_active)}")
print(f"Boolean False: {is_complete}")
print(f"Boolean operations: {True and False}, {True or False}, {not True}")

# 6. BINARY TYPES
print("\n6. BINARY TYPES")
print("-" * 20)

# Bytes (immutable)
byte_data = b"Hello World"
byte_array_data = bytes([65, 66, 67])
print(f"Bytes: {byte_data}, type: {type(byte_data)}")
print(f"Bytes from list: {byte_array_data}")

# Bytearray (mutable)
mutable_bytes = bytearray(b"Hello")
mutable_bytes[0] = 72  # Change 'H' to 'h' (ASCII 72)
print(f"Bytearray: {mutable_bytes}, type: {type(mutable_bytes)}")

# Memoryview
memory_view = memoryview(byte_data)
print(f"Memoryview: {memory_view}, type: {type(memory_view)}")

# 7. NONE TYPE
print("\n7. NONE TYPE")
print("-" * 20)

nothing = None
print(f"None: {nothing}, type: {type(nothing)}")
print(f"Is None: {nothing is None}")

# 8. ADVANCED DATA STRUCTURES
print("\n8. ADVANCED DATA STRUCTURES")
print("-" * 20)

# Collections module examples
from collections import namedtuple, defaultdict, Counter, deque

# Named Tuple
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(10, 20)
print(f"Named Tuple: {p1}, x: {p1.x}, y: {p1.y}")

# Default Dictionary
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(f"Default Dict: {dict(dd)}")

# Counter
text = "hello world"
counter = Counter(text)
print(f"Counter: {counter}")

# Deque (double-ended queue)
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(f"Deque: {dq}")

# 9. TYPE CHECKING AND CONVERSION
print("\n9. TYPE CHECKING AND CONVERSION")
print("-" * 40)

# Type checking
print(f"isinstance(25, int): {isinstance(25, int)}")
print(f"isinstance('hello', str): {isinstance('hello', str)}")
print(f"isinstance([1,2,3], list): {isinstance([1,2,3], list)}")

# Type conversion
str_num = "123"
int_num = int(str_num)
float_num = float(str_num)
list_from_string = list("hello")
tuple_from_list = tuple([1, 2, 3])

print(f"String to int: '{str_num}' -> {int_num}")
print(f"String to float: '{str_num}' -> {float_num}")
print(f"String to list: 'hello' -> {list_from_string}")
print(f"List to tuple: [1,2,3] -> {tuple_from_list}")

# 10. MUTABLE vs IMMUTABLE
print("\n10. MUTABLE vs IMMUTABLE")
print("-" * 30)

print("IMMUTABLE TYPES:")
print("- int, float, complex, bool, str, tuple, frozenset, bytes")

print("\nMUTABLE TYPES:")
print("- list, dict, set, bytearray")

# Demonstration
immutable_tuple = (1, 2, 3)
mutable_list = [1, 2, 3]

print(f"Original tuple: {immutable_tuple}")
print(f"Original list: {mutable_list}")

# This would cause an error:
# immutable_tuple[0] = 10  # TypeError

# This works:
mutable_list[0] = 10
print(f"Modified list: {mutable_list}")

# 11. MEMORY AND IDENTITY
print("\n11. MEMORY AND IDENTITY")
print("-" * 25)

a = [1, 2, 3]
b = a  # Same object
c = [1, 2, 3]  # Different object

print(f"a: {a}, id: {id(a)}")
print(f"b: {b}, id: {id(b)}")
print(f"c: {c}, id: {id(c)}")
print(f"a is b: {a is b}")
print(f"a is c: {a is c}")
print(f"a == c: {a == c}")

# 12. PRACTICAL EXAMPLES
print("\n12. PRACTICAL EXAMPLES")
print("-" * 25)

# Data processing example
students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [90, 87, 93]},
    {"name": "Charlie", "grades": [78, 85, 88]}
]

for student in students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    print(f"{student['name']}: Average grade = {avg_grade:.1f}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# 13. PYTHON VARIABLE TYPES AND SCOPING
print("\n13. PYTHON VARIABLE TYPES AND SCOPING")
print("=" * 40)

# A. LOCAL VARIABLES
print("\nA. LOCAL VARIABLES")
print("-" * 20)

def local_example():
    local_var = "I'm local"  # Local variable
    print(f"Inside function: {local_var}")
    return local_var

result = local_example()
print(f"Returned value: {result}")
# print(local_var)  # This would cause NameError

# B. GLOBAL VARIABLES
print("\nB. GLOBAL VARIABLES")
print("-" * 20)

global_var = "I'm global"  # Global variable

def global_example():
    print(f"Accessing global: {global_var}")
    
def modify_global():
    global global_var
    global_var = "Modified global"
    print(f"Modified global: {global_var}")

global_example()
modify_global()
print(f"Global after modification: {global_var}")

# C. NONLOCAL VARIABLES (Enclosing Scope)
print("\nC. NONLOCAL VARIABLES")
print("-" * 25)

def outer_function():
    outer_var = "I'm in outer scope"
    
    def inner_function():
        nonlocal outer_var
        outer_var = "Modified by inner"
        print(f"Inner function: {outer_var}")
    
    print(f"Before inner call: {outer_var}")
    inner_function()
    print(f"After inner call: {outer_var}")

outer_function()

# D. CLASS VARIABLES vs INSTANCE VARIABLES
print("\nD. CLASS vs INSTANCE VARIABLES")
print("-" * 35)

class Student:
    # Class variable (shared by all instances)
    school_name = "Python Academy"
    student_count = 0
    
    def __init__(self, name, age):
        # Instance variables (unique to each instance)
        self.name = name
        self.age = age
        Student.student_count += 1
    
    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, School: {self.school_name}")

# Creating instances
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

student1.display_info()
student2.display_info()
print(f"Total students: {Student.student_count}")

# Modifying class variable
Student.school_name = "Advanced Python Academy"
student1.display_info()  # Shows updated school name

# E. STATIC VARIABLES (using class methods)
print("\nE. STATIC VARIABLES")
print("-" * 20)

class Counter:
    _count = 0  # Private class variable
    
    @classmethod
    def increment(cls):
        cls._count += 1
    
    @classmethod
    def get_count(cls):
        return cls._count
    
    @staticmethod
    def reset():
        Counter._count = 0

Counter.increment()
Counter.increment()
print(f"Counter value: {Counter.get_count()}")
Counter.reset()
print(f"After reset: {Counter.get_count()}")

# F. VARIABLE NAMING CONVENTIONS
print("\nF. VARIABLE NAMING CONVENTIONS")
print("-" * 35)

# Valid variable names
valid_name = "good"
_private_var = "starts with underscore"
__dunder_var__ = "dunder (double underscore)"
CamelCase = "not recommended for variables"
snake_case = "recommended for variables"
CONSTANT_VAR = "uppercase for constants"

print("Valid naming examples:")
print(f"snake_case: {snake_case}")
print(f"_private_var: {_private_var}")
print(f"CONSTANT_VAR: {CONSTANT_VAR}")

# G. VARIABLE ASSIGNMENT TYPES
print("\nG. VARIABLE ASSIGNMENT TYPES")
print("-" * 35)

# Simple assignment
x = 10
print(f"Simple assignment: x = {x}")

# Multiple assignment
a, b, c = 1, 2, 3
print(f"Multiple assignment: a={a}, b={b}, c={c}")

# Tuple unpacking
coordinates = (10, 20)
x_coord, y_coord = coordinates
print(f"Tuple unpacking: x={x_coord}, y={y_coord}")

# List unpacking
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"List unpacking: first={first}, middle={middle}, last={last}")

# Chained assignment
x = y = z = 100
print(f"Chained assignment: x={x}, y={y}, z={z}")

# Augmented assignment
counter = 5
counter += 3  # Same as counter = counter + 3
print(f"Augmented assignment: counter = {counter}")

# H. VARIABLE SCOPE DEMONSTRATION
print("\nH. VARIABLE SCOPE DEMONSTRATION")
print("-" * 40)

# LEGB Rule: Local, Enclosing, Global, Built-in
builtin_example = len  # Built-in function

global_scope_var = "Global"

def demonstrate_scope():
    enclosing_var = "Enclosing"
    
    def inner_scope():
        local_var = "Local"
        print(f"Local: {local_var}")
        print(f"Enclosing: {enclosing_var}")
        print(f"Global: {global_scope_var}")
        print(f"Built-in: {builtin_example([1,2,3])}")
    
    inner_scope()

demonstrate_scope()

# I. VARIABLE TYPES BY MUTABILITY
print("\nI. VARIABLE TYPES BY MUTABILITY")
print("-" * 40)

# Immutable variables
immutable_int = 42
immutable_str = "Hello"
immutable_tuple = (1, 2, 3)

print("IMMUTABLE VARIABLES:")
print(f"Integer: {immutable_int} (id: {id(immutable_int)})")

# When we "change" an immutable variable, we create a new object
immutable_int = 43
print(f"After 'change': {immutable_int} (id: {id(immutable_int)})")

# Mutable variables
mutable_list = [1, 2, 3]
mutable_dict = {"key": "value"}

print("\nMUTABLE VARIABLES:")
print(f"List before: {mutable_list} (id: {id(mutable_list)})")
mutable_list.append(4)  # Modifies the same object
print(f"List after: {mutable_list} (id: {id(mutable_list)})")

# J. SPECIAL VARIABLE TYPES
print("\nJ. SPECIAL VARIABLE TYPES")
print("-" * 30)

# Private variables (convention)
class MyClass:
    def __init__(self):
        self.public = "Everyone can access"
        self._protected = "Should not access directly"
        self.__private = "Name mangled by Python"
    
    def show_variables(self):
        print(f"Public: {self.public}")
        print(f"Protected: {self._protected}")
        print(f"Private: {self.__private}")

obj = MyClass()
obj.show_variables()
print(f"Accessing public: {obj.public}")
print(f"Accessing protected: {obj._protected}")
# print(obj.__private)  # This would cause AttributeError
print(f"Name mangled private: {obj._MyClass__private}")

# K. VARIABLE MEMORY MANAGEMENT
print("\nK. VARIABLE MEMORY MANAGEMENT")
print("-" * 35)

import sys

# Small integers are cached
a = 100
b = 100
print(f"Small integers - a is b: {a is b}")

# Large integers are not cached
x = 1000
y = 1000
print(f"Large integers - x is y: {x is y}")

# String interning
str1 = "hello"
str2 = "hello"
print(f"String interning - str1 is str2: {str1 is str2}")

# Memory usage
sample_list = [1, 2, 3, 4, 5]
print(f"List memory size: {sys.getsizeof(sample_list)} bytes")

# L. VARIABLE TYPE ANNOTATIONS (Python 3.5+)
print("\nL. VARIABLE TYPE ANNOTATIONS")
print("-" * 35)

# Type hints for variables
name: str = "Alice"
age: int = 25
height: float = 5.6
is_student: bool = True
grades: list[int] = [85, 90, 78]
student_info: dict[str, str] = {"name": "Bob", "major": "CS"}

print(f"Annotated variables:")
print(f"name: {name} (type: {type(name)})")
print(f"grades: {grades} (type: {type(grades)})")

# Optional types
from typing import Optional, Union, List, Dict

optional_value: Optional[str] = None
union_value: Union[int, str] = "could be int or string"
list_of_strings: List[str] = ["apple", "banana"]
string_dict: Dict[str, int] = {"a": 1, "b": 2}

print(f"Optional: {optional_value}")
print(f"Union: {union_value}")

print("\n" + "=" * 60)
print("PYTHON VARIABLE TYPES COMPLETE")
print("=" * 60)