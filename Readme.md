# 📁 Python File I/O Practice

This folder contains my Python practice for **File Input/Output (File I/O)**.

Today I learned how to create, read, write, update, and delete files using Python.

## 📚 Topics Covered

* Opening files using `open()`
* Reading files using `read()`
* Reading files line by line using `readline()`
* Writing data using `write()`
* Using `with open()` for file handling
* File modes:

  * `r` → Read
  * `w` → Write
  * `r+` → Read and Write
  * `w+` → Write and Read
* Replacing text in a file
* Searching for a word in a file
* Finding the first line containing a specific word
* Splitting comma-separated data
* Counting even numbers
* Deleting files using the `os` module

## 📝 Practice Exercises

### 1. Basic File Handling

Created and worked with a file named `demo`.

Practiced:

```python
open()
read()
write()
readline()
close()
```

### 2. Creating and Writing a File

Created `practice.txt` and added text to it using Python.

### 3. Replacing Text

Replaced all occurrences of:

```text
Java → Python
```

using the `replace()` method.

### 4. Searching for a Word

Checked whether the word **"learning"** exists in the file.

### 5. Finding a Word's Line Number

Created a function to find the first line where the word **"learning"** occurs.

If the word is not found, the program prints:

```text
-1
```

### 6. Counting Even Numbers

Read numbers separated by commas from `numbers.txt` and:

* Printed the numbers
* Identified even numbers
* Counted the total number of even numbers

## 📂 Files

```text
File-IO/
│
├── file_handling.py
├── file_io_practice.py
├── practice.txt
├── numbers.txt
└── README.md
```

## 💡 Key Learning

File handling allows Python programs to store and retrieve information from files instead of keeping everything only in memory.

The `with open()` method is especially useful because Python automatically handles closing the file after the operation is completed.

## 🚀 Progress

**Day: File I/O Practice**

Continuing my Python learning journey and building my programming fundamentals step by step. 🐍
