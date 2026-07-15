# Dictionary & Sets in python
info = {
    "name" : "Shumaila",
    "subjects" : ["dbms","AI", "Cyber Security"],
    "topic" : ("dictionary", "set"),
    "department": "IT",
    "course" : "python"
}
info["surname"] = "Qadri"
print(info)

null_dict = {}
print(type(null_dict))

# Nested Dictionary
dict = {
    "name" : "shumaila",
    "score" : {
        "chem" : 80,
        "math" : 98,
        "phsics" : 81
    }
}
print(dict)
print(dict["score"]["chem"])
print(info.values())
print(dict.items())
print(dict.get("name"))

# Sets

set = {1, 2, 3, 4, 5}
set.add(6)
set.add(7)
print(set.pop())
print(set.pop())
print(set)
print(type(set))
set.remove(6)
set.add(("anya", "alaya", "marwa"))
set.clear()
print(len(set))
print(set)

# Practice
# QNo1
# Store following word meaning in a python dictionary:
# table : "a piece of furniture", "lists of facts & figures"
# cat : "a small animal"
dictionary = {
    "table" : ["a piece of furniture","lists of facts & figures"],
     "cat" : "a small animal"
}
print(dictionary)
# QNo2
# You are given a list of subjects for students. Assume one classroom is required
# for one subject. How many classes are required by all students?
# "python", "java", "C++", "JavaScript", "java", "python",
# "java", "C++", "C"
subjects = {"python", "java", "C++", "JavaScript", "java", "python",
            "java", "C++", "C"}
print(subjects)
print(len(subjects))

# QNo3
# WAP to enter marks of 3 subjects from the user and store them in a dictionary.

marks = {}
a = int(input("Enter chemistry marks: "))
marks.update({"chem": a})
b = int(input("Enter math marks: "))
marks.update({"math": b})
c = int(input("Enter physics marks: "))
marks.update({"physics": c})
print(marks)
# QNo4
# Figure out a way to write 9 & 9.0 as a separate value
values = (( "int", 9),
         ("float", 9.0)
 )
print(values)
