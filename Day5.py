# Loops
# while loop
count = 1
while count <= 5:
    print("hello")
    count += 1
print(count)

i = 1
while i <= 100:
   print("UOE", i)
   i += 1
print("Loop Ended")

#Practice
# Print numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1
# Print numbers from 100 to  1
i = 100
while i >= 1:
    print(i)
    i -= 1
# Print multiplication table of number
n = int(input("Enter a number: "))
a = 1
while a <= 10:
    print(n * a)
    a += 1
# Print the elements using the following list using loop
# [1, 4, 9, 16, 25, 36, 49, 64, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
# Search for a number x in this tuple using loop
# (1, 4, 9, 16, 25, 36, 49, 64, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 100)
x = 49
idx = 0
while idx < len(nums):
    if nums[idx] == x:
     print("Found at index", idx)
    idx += 1
# Break
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

print("End of loop")
# Continue
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1
print("End of loop")
# for loop
nums = [1, 2, 3, 4, 5, 6, 7]
for value in nums:
    print(value)
# Print the elements using the following list using loop
# [1, 4, 9, 16, 25, 36, 49, 64, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 100]
for value in nums:
    print(value)

# Print the elements using the following list using loop
# (1, 4, 9, 16, 25, 36, 49, 64, 100)
nums = (1, 4, 9, 16, 25, 36, 49, 64, 100)
idx = 0
x = 64
for value in nums:
    if value == x:
        print("Found at index", idx)
    idx += 1
    print(value)

# Range
seq = range(1, 10)
for i in seq:
    print(i)

for i in range(10):
    print(i)
# Using for & range
# print the numbers from 1 to 100
for i in range(1, 101):
    print(i)
# print the numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)
# Print the multiplication table of number n
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(n * i)