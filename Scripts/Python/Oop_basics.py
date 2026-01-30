# ==============================================================================
# 05_OOP_FUNDAMENTALS.PY
# Purpose: Demonstrating Python Basics, Escape Sequences, and OOP Pillars.
# Pillars covered: Encapsulation, Inheritance, and Polymorphism.
# ==============================================================================

# --- SECTION 1: BASICS & ESCAPE SEQUENCES ---
print("Hi, This is my first Python Code...Hello World !!\n")

# Single line comment example
print("My name is \"Neha\"\n")  # Using escape characters for double quotes
print('Hello, "Pari"\n')        # Mixing single and double quotes

# Handling Windows file paths with escape characters (\\)
print("My path is:- C:\\Users\\HP\\Desktop\\Python_Neha\\8th_Jan_2026\\hello.py")
print("message1\tmessage2")    # Tab space example

print("-" * 100)

# --- SECTION 2: CLASSES & CONSTRUCTORS ---
class Animal:
    name = "Cow"
    color = "white"
    weight = 30

    def __init__(self):
        """Constructor: Initializes when an object is created."""
        self.name = "dracula"
        print("init method called...")

    def weight_animal(self):
        print(f"weight is {self.weight}")

# Object Instantiation
animal1 = Animal()
print(animal1.weight)
animal1.weight = 60
animal1.weight_animal()
print("name is:- ", animal1.name)

animal2 = Animal()
print(animal2.weight)
animal2.weight_animal()

print("-" * 60)

# --- SECTION 3: ENCAPSULATION (DATA HIDING) ---
class UserProfile:
    def __init__(self, name, bio, amount, pincode):  
        self.name = name
        self.bio = bio
        # Private attributes (prefixed with __)
        self.__amount = amount    
        self.__pincode = pincode

    def upload_image(self, image):
        print(f"{self.name} content: {image}")

    def addSalary(self, salary, pin):
        """Method demonstrating access control using private variables."""
        if self.__pincode == pin:
            salary += self.__amount
            print(f"{self.name} has added salary of {salary}")
        else:
            print(f"Wrong pin..not allowed..")



user1 = UserProfile("Neha", "I am DevOps Lover", 1000, 1234)
print(user1.name)  
user1.upload_image("peacock")   
user1.addSalary(2000, 1234)     

print("-" * 60)

# --- SECTION 4: INHERITANCE ---
class A:
    name = "abc"
    age = 40
    salary_amount = 1000

    def getdetails(self):
        print(f"I am {self.name} and my age is {self.age}")
    
class B(A): # B inherits from A
    def getbalance(self, amount):
        print(f"I am {self.name} and I have savings of {amount}")

    def update_balance(self, deposit):
        deposit += self.salary_amount
        return deposit

# Demonstrating Inheritance functionality
a_obj = A()
b_obj = B()

a_obj.getdetails()
b_obj.getbalance(1000)
print(f"Updated Balance: {b_obj.update_balance(6000)}")

print("-" * 80)
print(" Polymorphism ")
print("-" * 80)

# --- SECTION 5: POLYMORPHISM ---
# Multiple classes sharing the same method name but with different behaviors
class Human:
    def identity(self, name):
        print(f"Hi, I am {name} and I speak")

class Dog:
    def identity(self, name):
        print(f"Hi, I am {name} and I bark")

class Cow:
    def identity(self, name):
        print(f"Hi, I am {name} and I meow")
     
def process_identity(obj, name):
    """A generic function that calls the identity method regardless of object type."""
    obj.identity(name)



h = Human()
d = Dog()
c = Cow()

process_identity(h, "Neha")
process_identity(d, "Tommy")
process_identity(c, "bulbul")
