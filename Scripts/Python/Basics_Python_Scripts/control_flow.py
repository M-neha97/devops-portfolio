# ========================================================
# MASTER CONTROL FLOW: CONDITIONALS & LOGIC
# Demonstrating: If-Else, Elif, Nested Ifs, and Membership
# ========================================================

# 1. BASIC IF-ELSE & NESTED LOGIC (Using your Age example logic)
# This shows you understand how to categorize values.
print("--- Section 1: Conditional Logic ---")
#age_value = 25
age_value=int(input("Enter age: "))

if age_value > 1 and age_value <= 2:
    print("Category: New-born")
elif age_value > 2 and age_value <= 18:
    print("Category: Teenager")
elif age_value > 18 and age_value <= 60:
    # Nested If: Checking sub-categories
    if age_value < 40:
        print("Category: Adult")
    else:
        print("Category: Older Adult")
else:
    print("Category: Senior Citizen")



# 2. COMPARISON OPERATORS
# Showing equality and inequality checks
print("\n--- Section 2: Comparison Checks ---")
if 2 == 2:
    print("Logic Check: Equal")
elif 2 != 3:
    print("Logic Check: Not equal")

# 3. MEMBERSHIP OPERATORS (Using your List example)
# Very important for checking if a  user exists in a system.
print("\n--- Section 3: List Membership ---")
name_list = ["neha", "vaibhav", "raj", "sneha", "pallavi"]

# checks if the user is in the list or not
if "neha" in name_list:
    print("Status: User 'neha' found in the system.")
elif "rajkumar" in name_list:
    print("Status: User 'rajkumar' found.")
else:
    # Case sensitivity check
    if "neha" == "Neha":
        print("Match: Case matches")
    else:
        print("Alert: Python is case-sensitive ('neha' is not 'Neha')")

print("\n" + "-"*50)
print("Control Flow Demonstration Complete")
