# Shell Scripting Practice – Level 1 to Level 3

This document contains Shell Scripting practice exercises from Basics to Loops.

---

# 🔹 Level 1 – Basics (Variables & Echo)

## 1️⃣ Variable Practice

```bash
#!/bin/bash
name="Neha"
echo "Hello, $name !"
echo "Welcome to Shell Scripting."
```

---

## 2️⃣ Arithmetic Operations

```bash
#!/bin/bash
echo "Arithmetic Operations..."
a=10
b=5

sum=$((a + b))
difference=$((a - b))
product=$((a * b))
division=$((a / b))

echo "The sum is : $sum"
echo "The difference is : $difference"
echo "The product is : $product"
echo "The division is : $division"
```

---

## 3️⃣ User Input

```bash
#!/bin/bash
echo "Enter your favorite programming language"
read programming_language
echo "Your favorite programming language is $programming_language."
```

---

# 🔹 Level 2 – Conditional Statements (if-else)

## 1️⃣ Check Even or Odd

```bash
#!/bin/bash
read -p "Enter a number : " number

if (( number % 2 == 0 )); then
    echo "The number $number is even"
else
    echo "The number $number is odd"
fi
```

---

## 2️⃣ Compare Two Numbers

```bash
#!/bin/bash
read -p "Enter first number:- " num1
read -p "Enter second number:- " num2

if [ $num1 -gt $num2 ]; then
    echo "First number $num1 is greater"
elif [ $num1 -eq $num2 ]; then
    echo "Both numbers are equal"
else
    echo "Second number $num2 is greater"
fi
```

---

## 3️⃣ String Comparison

```bash
#!/bin/bash
read -p "Enter first string value : " string_1
read -p "Enter second string value : " string_2

if [ "$string_1" = "$string_2" ]; then
    echo "Both strings are same"
else
    echo "Both strings are different"
fi
```

---

## 4️⃣ Login Simulation

```bash
#!/bin/bash
username="neha"
password="1234neha"

read -p "Enter username: " user
read -p "Enter password: " passw

if [[ "$username" = "$user" && "$password" = "$passw" ]]; then
    echo "Login Successful"
else
    echo "Access Denied"
fi
```

---

# 🔹 Level 3 – Loops

## 1️⃣ Print Numbers 1 to 10

```bash
#!/bin/bash
for number in {1..10}
do
    echo "Number is - $number"
done
```

---

## 2️⃣ Sum of First 10 Numbers

```bash
#!/bin/bash
sum=0
for i in {1..10}
do
    sum=$((sum+i))
done
echo "The sum of first 10 numbers is - $sum"
```

---

## 3️⃣ Factorial Finder

```bash
#!/bin/bash
read -p "Enter a number: " number
fact=1

for (( i=1; i<=number; i++ ))
do
    fact=$((fact * i))
done

echo "Factorial is $fact"
```

---

## 4️⃣ Countdown (While Loop)

```bash
#!/bin/bash
count=10

while [ $count -ge 1 ]
do
    echo "Number is: $count"
    count=$((count-1))
done
```

---

## 5️⃣ Multiplication Table

```bash
#!/bin/bash
read -p "Enter a number: " number

for (( i=1; i<=10; i++ ))
do
    echo "$number x $i = $((number*i))"
done
```

---

# ✅ Skills Covered

- Variables & echo  
- Arithmetic operations  
- User input handling  
- Conditional statements  
- String comparison  
- Authentication logic  
- for loop  
- while loop  
- Factorial logic  
- Multiplication tables  

This demonstrates progressive Shell Scripting skills from beginner to intermediate level.
