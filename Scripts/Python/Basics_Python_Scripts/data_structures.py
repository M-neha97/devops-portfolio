# ========================================================
# MASTER DATA STRUCTURES & STRING FUNCTIONS
# Purpose: Demonstration of Python basics for DevOps
# ========================================================

'''
Basics Data Types:
- string (str): Text data
- integer (int): Whole numbers (e.g., Port numbers)
- float (float): Decimals (e.g., CPU load)
- boolean (bool): True/False (e.g., is_server_up)

Grouped Data Types:
- list: Ordered, mutable collection
- tuple: Ordered, immutable (fixed) collection
- set: Unordered, unique collection
- dictionary: Key-Value pairs
'''
 
# 1. STRING FUNCTIONS
string_input = "  devops automation with python  "

print(f"string_input is:- {string_input}")
print(f"length of string_input is:- {len(string_input)}")
print(f"remove spaces from input string:- {string_input.strip()}")
print(f"Uppercase:- {string_input.strip().upper()}")
print(f"Lowercase:- {string_input.strip().lower()}")
print(f"Capitalize:- {string_input.strip().capitalize()}") #only first character
print(f"Replace words:- {string_input.replace("python","shell scripting")}")
print(f"split function:- {string_input.split()}")
print(f"{string_input.split()[0][0:3]}")  # indexing

# 2. LISTS (The Array equivalent in Python)

sample_list= ["Terraform","Git" ,"Linux", "Ansible","Docker","Jenkins"]

print(f"sample_list is:- {sample_list}")
print(f"length of sample_list is:- {len(sample_list)}")
print(f"{sample_list[2][0:3]}") # indexing and slicing 
print(f"{sample_list[0:4]}")
sample_list.append("Kubernetes")
print(f"after appending list is:- {sample_list} and length is:- {len(sample_list)}")
sample_list[1]="GitHub"  
print(sample_list)

# 3. TUPLES (Fixed data)

tuple_input=("Neha","BTech",30,"Mumbai")
print(f"tuple input is:- {tuple_input} and length is:- {len(tuple_input)}")
print(tuple_input[0])
int_tuple_data=(30,40,50,1,2)
print(f"max number:- {max(int_tuple_data)}") # returns max value
print(f"min value:- {min(int_tuple_data)}")
print(f"sorted tuple:- {sorted(int_tuple_data)}")

for index, no in enumerate(int_tuple_data, start=1):   # we 
    print(f"Index {index}: {no}")

# 4. SETS (Unique values only)

set_data={"read","write","execute","read"}
print(f"Operations available:-{set_data}") #removes duplicate data
set_data.add("Python")
print(f"updated set input:- {set_data}")
set_data.remove("Python")
print(f"removed python:- {set_data}")
print("")
# 5. DICTIONARY (group of key:value pairs)

server_config = {
    "hostname": "web-server",
    "ip": "192.168.1.50",
    "is_active": True
}

print(f"keys of server_config:- {server_config.keys()}")
print(f"values of server_config:- {server_config.values()}")
print(f"hostname is:- {server_config["hostname"]}")
server_config["database"]="MySql"
print(f"database is:- {server_config.get("database")}")














