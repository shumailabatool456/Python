# Functions in Python
def cal_sum(a, b):
    sum = a + b
    return sum
    print(sum)

cal_sum(1, 2)
cal_sum(10, 11)
def subtract_nums(a, b):
    return a - b
print(subtract_nums(45, 23))

def print_hello():
    print("hello")
print_hello()
print_hello()
print_hello()

# function to find average of three numbers
def calc_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average
print(calc_average(5, 9, 13))
# OR
def average(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = sum / 3
    print(avg)
    return avg
average(5, 9, 13)

# Types of function in  Python
# Built_in_functions
print("university of education", end=" ")
print("shumailabatool")
# length
print(len("blueberry"))
# type
print(type(len("blueberry")))
# range
for i in range(10):
    print(i)
# User_defined functions , functions we or programmers made
def calc_prod(num1, num2):
    prod = num1 * num2
    return num1*num2

print(calc_prod(5, 9))

def calc_prod(num1, num2 = 7):
    prod = num1 * num2
    return num1 * num2
print(calc_prod(5))
# WAF to print length of a list
cities = ["Lahore", "Vehari", "Multan", "Islamabad"]
def print_len(cities):
    print(len(cities))
print_len(cities)
# WAF to print elements of list in single line

heroes = ["Ironman", "spiderman", "safeguard", "benten"]
def print_heroes(list):
    for hero in heroes:
        print(hero, end=" ")
print_heroes(heroes)

# WAF to find factorial of number n (n is the parameter)
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
# OR
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(6)

# Function to convert USD to PKR
def usd_to_pkr(amount, exchange_rate=278):
    # Convert USD to PKR
    pkr = amount * exchange_rate
    return pkr
print(usd_to_pkr(20))
# Problem
def check_no(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_no(5)
# Recursion
# Recursive Function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)
# FACTORIAL
def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(5))
# Practice
# Write a recursive function to calculate sum of first n natural numbers
def calc_sum(n):
    if n==0:
        return 0
    return calc_sum(n-1) + n
print(calc_sum(7))

# write a recursive function to print all elements in a list
i = 0
fruits = ["apple", "banana", "cherry"]
def print_list(list, i):
    if (i == len(list)):
        return
    print(list[i])
    print_list(list, i+1)
print_list(fruits, 0)
#
def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n-1)
count_down(5)






