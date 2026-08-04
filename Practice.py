#Create a new file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.

with open("practice.txt", "w") as f:
    data= f.write("Hi Everyone!\nWe are learning file I/O\nin Java.\nI like  learning Java programming.")
    print(data)
#
# # WAF that replace all occurrences of "java" with "python" in above file.
def check_for_word():
    with open("practice.txt", "r") as f:
        data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)
    with open("practice.txt", "w") as f:
        f.write(new_data)
check_for_word()
# Search if the word "learning" exists in the file or not.
with open("practice.txt", "r") as f:
    data = f.read()
    if data.find("learning") != -1:
        print("Found")
    else:
        print("Not found")
# # WAF to find in which line of the file does the word "learning" occur first.
# # Print -1 if word not found
def check_line():
    word = "learning"
    data  = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no += 1
    return -1
check_line()

# From a file containing numbers separated by comma, print the count of even numbers.numbers
count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            print(int(val))
            count += 1
print(count)






