# Different types of exceptions in Python:

# SyntaxError
# Example:
# raise SyntaxError("Invalid syntax")

# TypeError
# Example:
# x = 5
# y = "hello"
# z = x + y  # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'

# NameError
# Example:
# raise NameError("Variable not found: x")

# IndexError
# Example:
# my_list = [1, 2, 3]
# print(my_list[3])  # Raises an IndexError: list index out of range

# KeyError
# Example:
# my_dict = {'key': 'value'}
# print(my_dict['invalid_key'])  # Raises a KeyError: 'invalid_key'

# ValueError
# Example:
# raise ValueError("Invalid argument")

# AttributeError
# Example:
# my_string = "Hello"
# print(my_string.uppercase())  # Raises an AttributeError: 'str' object has no attribute 'uppercase'

# IOError
# Example:
# with open("nonexistent_file.txt", "r") as file:  # Raises an IOError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
#     contents = file.read()

# ZeroDivisionError
# Example:
# x = 5
# y = 0
# z = x / y  # Raises a ZeroDivisionError: division by zero

# ImportError
# Example:
# import non_existent_module  # Raises an ImportError: No module named 'non_existent_module'

# Difference between Syntax Error and Exceptions:

# SyntaxError: Caused by incorrect syntax in the code, leading to program termination.
# Example:
# raise SyntaxError("Invalid syntax")

# Exceptions: Raised when the program encounters an error during execution, changing the program's flow but not stopping it.
# Example:
# try:
#     x = 5
#     y = "hello"
#     z = x + y  # Raises a TypeError: unsupported operand type(s) for +: 'int' and 'str'
# except TypeError:
#     print("Error: cannot add an int and a str")

# Try and Except Statement - Catching Exceptions:

# Example:
# try:
#     my_list = [1, 2, 3]
#     print(my_list[3])  # Raises an IndexError: list index out of range
# except IndexError:
#     print("An error occurred")

# Catching Specific Exception:

# Example:
# def divide(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Error: Division by zero")
#     except ValueError:
#         print("Error: Invalid value")
#
# divide(10, 0)  # Raises a ZeroDivisionError
# divide(10, "hello")  # Raises a TypeError

# Try with Else Clause:

# Example:
# try:
#     x = 5
#     y = 2
#     z = x / y
# except ZeroDivisionError:
#     print("Error: Division by zero")
# else:
#     print("Result:", z)

# Finally Keyword in Python:

# Example:
# try:
#     x = 5 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero")
# finally:
#     print("Finally block always executes")

# Raising Exception:

# Example:
# def check_age(age):
#     if age < 0:
#         raise ValueError("Invalid age")
#     else:
#         print("Age is valid")
#
# check_age(-5)  # Raises a ValueError: Invalid age

# Advantages of Exception Handling:

# Improved program reliability
# Simplified error handling
# Cleaner code
# Easier debugging

# Disadvantages of Exception Handling:

# Performance overhead
# Increased code complexity
# Possible security risks




#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#File Handling
#File handling in computer programming refers to the process of working with files stored on a computer's storage system.
# Advantages of File Handling:

# Versatility: File handling in Python allows you to perform a wide range of operations, such as creating, reading, writing, appending, renaming, and deleting files.
# Flexibility: File handling in Python is highly flexible, as it allows you to work with different file types (e.g. text files, binary files, CSV files, etc.), and to perform different operations on files (e.g. read, write, append, etc.).
# User–friendly: Python provides a user-friendly interface for file handling, making it easy to create, read, and manipulate files.
# Cross-platform: Python file-handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.

# Disadvantages of File Handling:

# Error-prone: File handling operations in Python can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).
# Security risks: File handling in Python can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.
# Complexity: File handling in Python can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.
# Performance: File handling operations in Python can be slower than other programming languages, especially when dealing with large files or performing complex operations.

# Example: Working in Read mode

# Example 1:
# Reading a file line by line using a for loop
file = open('geek.txt', 'r')
for each in file:
    print(each)

# Example 2:
# Reading the entire contents of a file using the read() function
file = open("geeks.txt", "r")
print(file.read())

# Example 3:
# Reading a file using the with statement
with open("geeks.txt") as file:
    data = file.read()
print(data)

# Example 4:
# Reading the first five characters of a file
file = open("geeks.txt", "r")
print(file.read(5))

# Example 5:
# Splitting lines while reading a file
with open("geeks.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

# Creating a File using the write() Function

# Example 1:
# Creating a file and writing content using the write() function
file = open('geek.txt', 'w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

# Example 2:
# Creating a file and writing content using the write() function and the with statement
with open("file.txt", "w") as f:
    f.write("Hello World!!!")

# Working in Append Mode

# Example:
# Appending content to an existing file
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()

# Implementing all the functions in File Handling

import os

def create_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write('Hello, world!\n')
        print("File " + filename + " created successfully.")
    except IOError:
        print("Error: could not create file " + filename)

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("Error: could not read file " + filename)

def append_file(filename, text):
    try:
        with open(filename, 'a') as f:
            f.write(text)
        print("Text appended to file " + filename + " successfully.")
    except IOError:
        print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
    try:
        os.rename(filename, new_filename)
        print("File " + filename + " renamed to " + new_filename + " successfully.")
    except IOError:
        print("Error: could not rename file " + filename)

def delete_file(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully.")
    except IOError:
        print("Error: could not delete file " + filename)


if __name__ == '__main__':
    filename = "example.txt"
    new_filename = "new_example.txt"

    create_file(filename)
    read_file(filename)
    append_file(filename, "This is some additional text.\n")
    read_file(filename)
    rename_file(filename, new_filename)
    read_file(new_filename)
    delete_file(new_filename)

#exception handling in file handling
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except IOError as e:
        print("Error: I/O error occurred:", str(e))

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print("File", filename, "written successfully.")
    except PermissionError:
        print("Error: Permission denied.")
    except IOError as e:
        print("Error: I/O error occurred:", str(e))

def append_file(filename, content):
    try:
        with open(filename, 'a') as file:
            file.write(content)
        print("Content appended to file", filename, "successfully.")
    except PermissionError:
        print("Error: Permission denied.")
    except IOError as e:
        print("Error: I/O error occurred:", str(e))

# Usage examples:

# Reading a file
read_file("example.txt")

# Writing to a file
write_file("new_file.txt", "This is some content.")

# Appending to a file
append_file("existing_file.txt", "This is additional content.")
