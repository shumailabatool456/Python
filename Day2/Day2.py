# Strings and conditional statements
#escape sequence characters \n  \t etc.
str_1 = "This is a string.\t I create it."
# str2 = 'This is a string'
# str3 = """This is a string"""
print(str_1)
#Concatenation
str1 = "hello"
str2 = "Shumaila"
print(str1 + str2)
print(len(str1))
print(len(str2))
#Indexing
string = "University of Education"
print(string[0])
print(string[14])

#Slicing
print(string[0:len(string)])
print(string[0:])
print(string[5:11])
print(string[14:23])
print(string[0:5])

#Negative indexing
print(string[5:11])
str3 = "Shumaila"
print(str3[-8:-1])
print(str3[-5:-1])
# String Functions
str4 = "I am a coder"
print(str4.endswith("er"))
str5 = "all power is within you."
print(str5.capitalize())
str5 = str5.replace("i", "s")
print(str5)
str6 = "I am a coder"
print(str6.find("a"))
print(str5.count("l"))

#Practice
#WAP to input user's first name & print its length.
firstname = input("Enter your first name: ")
print("length of your name", len(firstname))
#WAP to find the occurrence of 'S' in a string.
str7 = "I $ the dollar symbol $100."
print(str7.count("$"))

#Conditional Statements
age = 21
if age >= 18:
    print("You can vote & apply for licence.")
else:
    print("You can not vote & apply for licence.")
# Traffic Lights
light = "green"
if light == "green":
    print("Go")
elif light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
else:
    print("Broken traffic lights")

#Grade System
marks = float(input("Enter your marks: "))
if marks >= 90:
    grade = "A"
elif 90 > marks >= 80:
    grade = "B"
elif 80 > marks >= 70:
    grade = "C"
elif 70 > marks >= 60:
    grade = "D"
print("Grade of the student is ->", grade)

#Nesting
age = 21
if age >= 18:
    print("can drive")
    if age >= 80:
        print("can not drive")
    else:
        print("can drive")
else:
    print("can not drive")

#Practice
#WAP to check if a number entered by the user is odd or even.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
#WAP to find the greatest of three numbers entered by the user.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
if num1 >= num2 and num1 >= num3:
    print("the first number is greatest:", num1)
elif num2 >= num3:
    print("The second number is greatest:", num2)
else:
    print("The third number is greatest:", num3)
#WAP to check if a number is multiple of 7 or not.
number = int(input("Enter a number: "))
if number % 7 == 0:
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")
#WAP to find greatest of four numbers.
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))
if a >= b and a >= c and a>=d:
   print ('a is greatest')
elif b >= a  and b  >= c and b >= d:
   print('b is greatest')
elif c >=a and c >= b and c >= d:
   print('c is greatest')
else:
   print ('d is greatest')