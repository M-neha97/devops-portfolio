
#Exercise 1: Calculate the multiplication and sum of two numbers
no1=int(input("Enter the first no.."))
no2=int(input("Enter the second no.."))

def function1(a,b):
    product=a*b
    if product<=1000:
        return product
    else:
        return a+b

result=function1(no1,no2)
print(f"final result is:- {result}")

#Print the Sum of a Current Number and a Previous number

for i in range(0,10): 
        if i==0:
             print(f"Current Number {i} Previous Number {i} Sum: {i+i}")
        else:
             a=i-1
             print(f"Current Number {i} Previous Number {a} Sum: {i+a}")
             

#Write a Python code to accept a string from the user and display characters 
# present at an even index number.

str_val=input("Enter string value from the user: ")
print(f"string value is: {str_val}")

for i in range(len(str_val)):
     if i%2==0:
          print(str_val[i])
     #print("")

#Write a Python code to remove characters from a string from 0 to n and return a new string
#"pynative", 2
# output 'native'

string_val="pynative"
n=2
def remove_char(str1,n):
     for i in range(0,n):
          str1=str1.replace(str1[i]," ")
 
     return str1
     
     
    
result_str=remove_char(string_val,n)
print(f"result is:- {result_str}")

#Write a code to return True if the list’s first and last numbers are the same. 
# If the numbers are different, return False.
#numbers_x = [10, 20, 30, 40, 10]
# output True

my_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(my_list)

def comparefun(my_list):
    len_list=len(my_list)
    print(len_list)
    if my_list[0]==my_list[len_list-1]:
        print("True")
    else:
        print("False")
        
comparefun(my_list)

#Write a Python code to display numbers from a list divisible by 5

list_input=[10, 20, 33, 46, 55,75]

def div_by_5_fun(list_input):
    for i in range(len(list_input)):
        if list_input[i]%5==0:
            print(list_input[i])

div_by_5_fun(list_input)
    

#Write a Python code to find how often the substring “Emma” appears in the given string.
'''
str_x = "Emma is good developer. Emma is a writer"
output=Emma appeared 2 times
'''
str_x = "Emma is good developer. Emma is a writer Emma"
list_in=str_x.split(" ")
print(list_in)
count=0
for i in range(len(list_in)):
    if list_in[i]=="Emma":
        count+=1
print(f"Emma appeared {count} times")

cnt = str_x.count("Emma")
print(cnt)

'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

row=5

for i in range(0,row): 
    for j in range(i+1):
        print(i+1,end=" ")
    print()
    
'''
Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. 
For example, 545 is a palindrome number
'''

no=int(input("Enter a number:- "))
print(f"no is:- {no}")

def palindrome_fun(number):
    original_no=number
    
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")
   

palindrome_fun(no)


'''
Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
input:-
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
output:
result list: [25, 35, 40, 60, 90]
'''

result_list=[]
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

for i in list1:
    if i%2!=0:
        result_list.append(i)

for j in list2:
    if j%2==0:
        result_list.append(j)
        

print(f"result_list is {result_list}")


# If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits  ..reverse order

number=int(input("Enter input from the user:- "))

while number>0:
    digit=number%10
    number=number//10
    print(digit,end=" ")


#multiplication table for numbers 1 through 10

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print("")
    

'''
* * * * *  
* * * *  
* * *  
* *  
*
'''

row=5
for i in range(row):
    for j in range(row-i):
        print("*",end=" ")
    print("")

'''
Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

base = 2
exponent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)
'''

def exponent_fun(base, exp):
    result=1
    while(exp>=1):
        result*=base
        exp=exp-1
    return result

base=int(input("enter base:- "))
exponent=int(input("enter exponent:- "))
result_value=exponent_fun(base,exponent)
print(f"the result is {result_value}")

'''
 Fibonacci series up to 15 terms
 first two numbers are 0 and 1
 For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
 
 Fibonacci sequence:
0  1  1  2  3  5  8  13  21  34  55  89  144  233  377
 '''

 # 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377

first_no=0
second_no=1
print(f"{first_no} {second_no}",end=" ")
i=3
while i<=15:
    sum=first_no+second_no  
    first_no=second_no  
    second_no=sum 
    i+=1 
    print(f"{sum}",end=" ")
    
# OR

# first two numbers
num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 15 times
for i in range(15):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res
    

#a simple countdown timer of 5 seconds using a while loop
'''
Time remaining: 5 seconds
Time remaining: 4 seconds
Time remaining: 3 seconds
Time remaining: 2 seconds
Time remaining: 1 seconds
Time's up!
'''
i=5
while(i>0):
    print(f"Time remaining: {i} seconds")
    i-=1
print(f"Time's up!")

    
    




 
  
 

  

