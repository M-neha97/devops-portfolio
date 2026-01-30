# ==============================================================================
# MAIN_APP.PY: DEMONSTRATING MODULES, PACKAGES, AND BUILT-INS
# ==============================================================================

# --- 1. CUSTOM MODULE IMPORTS ---
# Importing specific items and using Aliasing (as)

from modules import var1, multiply as mul
from utils import sum1, evn_odd_no
import random, string
from datetime import datetime

# --- Testing Custom Modules ---
print(f"Variable from modules.py: {var1}")
print("")
print(f"Multiplication Result: {mul(10, 15)}")
print("")
print(f"Sum from utils.py: {sum1(34, 89)}")
print("")

# --- User Input Interaction ---
try:
    no = int(input("Enter a number: "))
    if evn_odd_no(no):
        print(f"Number {no} is an even number")
    else:
        print(f"Number {no} is an odd number")
except ValueError:
    print("Please enter a valid integer.")



# --- Exploring Built-in Modules ---
print("\n--- Built-in Module Demos ---")
print("")
print(f"Random Number (13-20): {random.randint(13, 20)}")
print("")
print(f"Uppercase Letters: {string.ascii_uppercase}")
print("")

# Creating a random 3-letter string
x = random.choices(string.ascii_letters, k=3)
print(f"Random Choice (3 letters): {x}")

print("")
# --- Datetime Operations ---
print(f"Current Time: {datetime.now()}")
print("")
print(f"Specific Date: {datetime(2022, 6, 17)}")
