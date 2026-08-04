# File Handling in Python

# Opening a file in read mode
f = open("demo", "r")

# Reading the complete file
data = f.read()
print(data)
print(type(data))

# Closing the file
f.close()


# Reading a file line by line
with open("demo", "r") as f:
    line1 = f.readline()
    line2 = f.readline()

    print(line1)
    print(line2)

    data = f.read()
    print(data)

    line1 = f.readline()
    print(line1)


# Opening a file in read and write mode
with open("demo", "r+") as f:
    data = f.write("\nOK, but nobody loves me.")
    print(data)


# Opening a file in write and read mode
with open("demo", "w+") as f:
    data = f.write("You are the best.")
    print(data)


# Deleting the file
import os

os.remove("demo")