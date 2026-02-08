# ========================================================
# LOOPS: FOR, WHILE, BREAK, CONTINUE, PASS
# ========================================================

Devops_tools=["Docker","Jenkins","Ansible","Terraform","Git","GitHub"]

# iterating through a list using for loop
print("--------- for loop---------------")

for tools in Devops_tools:
    print(f"{tools}", end=" ")
print("\n")

# iterating through a list using while loop
print("--------- while loop---------------")

i=0
while (i<len(Devops_tools)):
    print(Devops_tools[i],end=" ")
    i+=1
print("\n")


#continue  # Skips the rest of the iteration and moves to the next tool
print(f"----- continue----------")

for tools in Devops_tools:
    if tools=="Ansible":
        continue  #skips Ansible 
    print(tools,end=" ")
print("\n")

#break ..When the break statement is executed, 
# the program immediately exits the loop - for or while

print(f"----- break----------")

for tools in Devops_tools:
    if tools=="Terraform":
        break
    print(f"{tools}",end=" ")
print("\n")

print(f"break in while loop")

i=0
while(i<len(Devops_tools)):  
    if Devops_tools[i]=="Git":
     break
    print(Devops_tools[i], end=" ")
    i+=1
print("\n")

# 3. THE PASS STATEMENT
# Use Case: Placeholder for code you haven't written yet (prevents errors).

def future_function():
    # I will write the backup logic here later
    pass

## Task: Find 'jenkins' in the list, but stop looking if you find 'error'.

services_list = ["nginx", "docker","terraform" ,"error", "jenkins"]

for service in services_list:
    if service=='error':
        print(f"error found")
        break
    elif service=='jenkins':
        print(f"service jenkins found")




