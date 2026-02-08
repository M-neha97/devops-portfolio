# ==============================================================================
# FUNCTIONS_AND_LAMBDA.PY
# Purpose: Demonstrating Standard Functions (def) and Anonymous Functions (lambda)
# Topics: standard functions,Lambda, Sorting complex data, Map, Filter, and Reduce.
# ==============================================================================

from functools import reduce

"""
Lambda Function Definition:
It is a small anonymous function which can take any number of arguments 
but should have only a single expression.

Standard Function:
def func(a, b):
    return a + b

Lambda Equivalent:
add = lambda a, b: a + b

Usecases:
- Custom sorting logic
- Functional operations on collections (map, filter, reduce)
"""

# --- SECTION 1: STANDARD FUNCTIONS (def) ---

def greet(entry_name):
    """Simple function demonstrating code reusability."""
    print(f"Greeting {entry_name} from Admin")

greet("Aayush")
greet("Neha")
greet("Khan")




# --- SECTION 2: RETURN VALUES ---

def multiply(list_input):
    """Demonstrates returning a value to be used in further calculations."""
    product = 1
    for number in list_input:
        product *= number
    return product

x = multiply([12, 434, 5])
print(f"\nMultiply Result: {x}")
print(f"Result plus 10: {x + 10}")


# --- SECTION 3: ARBITRARY ARGUMENTS (*args) ---

def sample_fun(x, *names):
    """Demonstrates how *args packs extra arguments into a Tuple."""
    print(f"\nFixed argument: {x}")
    print(f"Tuple of names (*args): {names}")
    print(f"Accessing index 2: {names[2]}")
    print(f"Data type: {type(names)}")

sample_fun("Aayush", "Neha", "Admin", "Khan")


# --- SECTION 4: MATHEMATICAL LOGIC (Factorials) ---

def factorial_fun(num):
    """Calculates factorial using a for-loop and range."""
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

print(f"\nFactorial of 6: {factorial_fun(6)}")


# --- SECTION 5: PALINDROME LOGIC (String vs Integer) ---

def palindrome_string(string_value):
    """Checks palindrome using string slicing [::-1]."""
    if string_value == string_value[::-1]:
        print(f"'{string_value}' is a palindrome.")
    else:
        print(f"'{string_value}' is not a palindrome.")

def palindrome_int(int_value):
    """Checks palindrome using mathematical remainder and floor division."""
    number = int_value
    palin_sum = 0
    while int_value > 0:
        reminder = int_value % 10
        palin_sum = palin_sum * 10 + reminder
        int_value //= 10
    return palin_sum == number

# Execution of Palindrome Logic
test_str = "radar"
palindrome_string(test_str)

test_int = 12321
if palindrome_int(test_int):
    print(f"The number {test_int} is a palindrome.")



# --- SECTION 6: NESTED LOOPS (Grid/Map Generation) ---

def map_fun(row, col):
    """Demonstrates nested loops and controlling print behavior with 'end'."""
    print(f"\nGenerating {row}x{col} grid:")
    for i in range(row):
        for j in range(col):
            print("*", end=" ")
        print("")

map_fun(3, 4)

# --- SECTION 7: LAMBDA & FUNCTIONAL PROGRAMMING ---

#  BASIC LAMBDA USAGE ---
add = lambda a, b: a + b
print(f"Lambda Addition (4+10): {add(4, 10)}")
print(f"Lambda Addition (42+30): {add(42, 30)}")

fun1 = lambda: "hello guys!"
print(f"No-argument Lambda: {fun1()}")

# Lambda with if-else (Conditional Expression)
check_odd_even = lambda n: "Even" if n % 2 == 0 else "Odd"
print(f"Is 10 Even or Odd? {check_odd_even(10)}")
print(f"Is 29 Even or Odd? {check_odd_even(29)}")

# Immediately Invoked Function Expression (IIFE)
# Useful for one-time calculations without defining a variable
print(f"Immediate Square of 10: {(lambda x: x**2)(10)}")
res = (lambda x: x**2)(10)
print(f"Result stored in variable: {res}")



# --- 2. SORTING BASICS ---
li = [5, 8, 12, 6, 4]
sorted_function = sorted(li)
print(f"\nOriginal List: {li}")
print(f"Sorted List (Ascending): {sorted_function}")

# --- 3. SORTING COMPLEX DATA (TUPLES) ---
# Format: (Name, Score1, Score2)
student_data_tuples = [
    ("Aayush", 70, 60),
    ("Neha", 79, 67),
    ("Admin", 70, 79),
    ("Khan", 70, 65),
    ("Ramesh", 72, 50)
]

# Sort by name (index 0) in reverse
sorted_by_name = sorted(student_data_tuples, key=lambda x: x[0], reverse=True)
print(f"\nSorted by Name (Reverse): {sorted_by_name}")

# Sort by score (index 1) in reverse
sorted_by_score = sorted(student_data_tuples, key=lambda x: x[1], reverse=True)
print(f"Sorted by Score (Reverse): {sorted_by_score}")

# Multi-level Sort: By score descending (index 1), then by third value (index 2) descending
# Note: Using -x[2] inside a tuple key is a clever way to handle numeric secondary sorts
output = sorted(student_data_tuples, key=lambda x: (x[1], -x[2]), reverse=True)
print(f"Multi-level Sort (Score Desc, index2 Desc): {output}")

# --- 4. SORTING COMPLEX DATA (DICTIONARIES) ---
student_data_dicts = [
    {"name": "Aayush", "age": 70},
    {"name": "Neha", "age": 75},
    {"name": "Admin", "age": 68},
    {"name": "Ramesh", "age": 90},
    {"name": "Suresh", "age": 10},
]

# Sort by age
result_dict_sort = sorted(student_data_dicts, key=lambda x: x["age"])
print(f"\nDictionaries sorted by age: {result_dict_sort}")

# Find Max age using Lambda
max_age_value = max(student_data_dicts, key=lambda y: y["age"])
print(f"Maximum age record: {max_age_value}")

# --- 5. FUNCTIONAL TOOLS: MAP, FILTER, REDUCE ---
numbers = [5, 8, 12, 6, 4]

# Map: Transform every item (e.g., squaring all numbers)
squared_numbers = list(map(lambda n: n**2, numbers))
print(f"\nMap (Squares): {squared_numbers}")

# Filter: Select items based on condition
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
print(f"Filter (Even numbers only): {even_numbers}")

# Reduce: Accumulate list into a single value (Product of all elements)
product_numbers = reduce(lambda x, y: x * y, numbers)
print(f"Reduce (Product of all numbers): {product_numbers}")



# --- 6. ADVANCED: CLOSURES (FUNCTION RETURNING LAMBDA) ---
def calc(n):
    """Returns a lambda that raises a number to power 'n'."""
    return lambda x: x**n

res_power_3 = calc(3) # res_power_3 is now a function that cubes values
print(f"\n6 raised to power 3 (using closure): {res_power_3(6)}")

# --- 7. MINI PROJECT: CALCULATOR DICTIONARY ---
# Demonstrates using Lambdas within a dictionary for clean, readable branching
calc_ope = {
    "add": lambda x, y: x + y,
    "mul": lambda x, y: x * y,
    "sub": lambda x, y: x - y,
    "div": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
}

operation = "mul"
val_a, val_b = 10, 15
print(f"\nPerforming {operation} on {val_a} and {val_b}: {calc_ope[operation](val_a, val_b)}")

print("-" * 50)
print("Lambda and Functional Programming demonstration complete.")
