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
