# Lists
marks1 = 100
marks2 = 99
marks3 = 87
marks4 = 79
marks5 = 80
marks =[100, 99, 87, 79, 80]
print(marks)
marks[3] = 77
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[0:4])
print(marks[0:])
print(marks[:5])
print(marks[:-1])
# List Methods
marks.append(55)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)
marks.insert(1,99)
print(marks)
marks.pop(3)
print(marks)
marks.remove(99)
print(marks)
marks.pop()
print(marks)
marks.pop(0)

# Tuples
tup =(100,99,87,79,80, 100)
print(tup.index(99))
print(tup.count(100))
print(tup)
print(tup.index(99))

# Practice
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list

movies =[]
mov1 = input("Enter names of your favorite 1st movie:")
movies.append(mov1)
mov2 = input("Enter names of your favorite 2nd movie:")
movies.append(mov2)
mov3 = input("Enter names of your favorite 3rd movie:")
movies.append(mov3)
print (movies)

# WAP to check if a list contains a palindrome of elements.
# [1,2,3,2,1]    [1,,"abc", "abc", 1]
list1 = [1,2,3,2,1]
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not Palindrome")
list2 = [1, "abc", "abc", 1]
copy_list2 = list2.copy()
copy_list2.reverse()
if(copy_list2 == list2):
  print("Palindrome")
else:
  print("Not Palindrome")

# WAP to count the number of students with the "A" grade in the morning
# ["C","D", "A", "A", "B", "B", "A"]
grade = ["C","D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)
print(grade.count("A"))
