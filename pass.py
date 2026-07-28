# pass statement
for i in range(5):
    pass
if i > 5:
    pass
print("some useful work")

# Write a program to find sum of first n numbers. (using while)
n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)

# Write a program to find factorial of first n numbers. (using for)
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
    i += 1
print("factorial is", fact)
