# Day 3
# Basic Operators and expressions (Input and output operators)
"""
-Arithmetic Operators
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
** Exponentiation
// Floor division (returns a number without a remainder)

-Comparison Operators
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to
== Equal to
!= Not equal to

-Logical Operators
Logical AND "and"
Logical OR "or"
Logical NOT "not"

-Assignment Operators
Assign value: '='
Add value: '+'
Subtract value: '-'
Add and assign value: '+='
subtract and assign value: '-='
Multiply and assign value: '*='
Divide and assign value: '/='
Modulus and assign value: '%='
Exponentiate and assign value: '**='

-Membership Operators
In: 'in' operator checks if a value exists in a sequence
Not in: 'not in' operator checks if a value does not exist in a sequence

-Identity Operators
Is: 'is' operator: checks if two values are the same
Is not: 'is not' operator: checks if two values are not the same

"""
# Examples
# # Addition
# x = 50 + 45
# print(x)

# # Subtraction
# y = 45 - 50
# print(y)

# # Multiplication
# z = 50 * 45
# print(z)

# # Division
# w = 45 / 50
# print(w)

# # Floor Division
# v = 45 // 50
# print(v)

# # Modulus
# u = 45 % 50
# print(u)

# # Exponentiation
# t = 45**50
# print(t)

# # Examples og comparison operators
# # comparison operators
# a = 25
# b = 9

# # Greater than
# if a > b:
#     print("a is greater than b")
#     print(a > b)

# # Less than
# if a < b:
#     print("a is less than b")
#     print(a < b)

# # Greater than or equal to
# if a >= b:
#     print("a is greater than or equal to b")
#     print(a >= b)

# # Less than or equal to
# if a <= b:
#     print("a is less than or equal to b")
#     print(a <= b)

# # Equal to
# if a == b:
#     print("a is equal to b")
#     print(a == b)

# # Not equal to
# if a != b:
#     print("a is not equal to b")
#     print(a != b)

# # Less than or equal to
# print(a <= b)

# Examples with Logical operators
# # Logical operators
# a = True
# b = False

# # Logical AND
# print(a and b)

# # Logical NOT
# print(not a)
# print(not b)

# # Logical OR
# print(a or b)


# # Assignment operators
# compound  assignment operators

# a = 19
# b = 20
# # Add and Assign
# a += 5
# print(a)

# # Subtract and Assign
# b -= 5
# print(b)

# # Multiply and Assign
# c = 19
# c *= 5
# print(c)

# # Divide and Assign
# d = 19
# d /= 5
# print(d)

# # Modulus and Assign
# e = 19
# e %= 5
# print(e)

# # Exponentiate and Assign
# f = 2
# f **= 5
# print(f)

# # # Membership operators
# cars = ["Jeep", "Tesla", "BMW", "RollRoyce"]

# if "Jeep" in cars:
#     print("Jeep is in the list")
#     print("Tesla" in cars)
#     print("Toyota" in cars)

# # # Identity operators
# x = 10
# y = 10

# # List
# # is not operator
# z = [1, 2, 3, 4, 5]
# w = [1, 2, 3, 4, 5]
# print(z is not w)

# Bitwise operators
"""
Bitwise operators are used to perform operations on individual bits in of binary numbers.

Bitwise AND "&"Performs a bitwise operation between the corresponding bits of two integers
Bitwise OR "|" Performs a bitwise operation between the corresponding bits of two integers
Bitwise XOR "^" Performs a bitwise operation between the corresponding bits of two integers
Bitwise NOT "~" Performs a bitwise NOT operation between the corresponding bits of two integers
Bitwise left shift "<<", Performs a bitwise left shift operation
Bitwise right shift ">>", Performs a bitwise right shift operation

"""
# # Examples of Bitwise operations
# a = 10  # 1010 in binary
# b = 20

# # Bitwise AND operations
# result_and = a & b
# print(result_and)

# # Bitwise OR operations
# result_or = a | b
# print(result_or)

# # Bitwise XOR operations
# result_xor = a ^ b
# print(result_xor)

# # Bitwise NOT operations
# result_not = ~a
# print(result_not)

# # Bitwise left shift operations
# result_left_shift = a << 2
# print(result_left_shift)

# # Bitwise right shift operations
# result_right_shift = a >> 2
# print(result_right_shift)

# #Example and Assignment
# Create a simple calculator function to calculate (add, subtract, multiply, divide)


# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def divide(a, b):
#     return a / b


# # elif and else if are the same
# def main():
#     print("Conrad's Simple Calculator")
#     number1 = float(input("Enter the first number: "))
#     number2 = float(input("Enter the second number: "))
#     operator = input("Enter the operator (+, -, *, /): ")

#     if operator == "+":
#         result = add(number1, number2)
#     elif operator == "-":
#         result = subtract(number1, number2)
#     elif operator == "*":
#         result = multiply(number1, number2)
#     elif operator == "/":
#         result = divide(number1, number2)
#     else:
#         print("Invalid operator")
#         return
#     print(f"The result is {result}")


# if __name__ == "__main__":
#     main()
# Assignment create a simple calculator program with a GUI interface.
#  Make your title of the calculator program window with your name e.g "Seru Cono Simple Calculator"
import tkinter as tk


# Function to perform calculation
def calculate():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        output.config(text="Result: " + str(result))  # Display the result
    except:
        output.config(text="Invalid input")


# Create the main window
window = tk.Tk()
window.title("Seru Cono Simple Calculator")  # Set the title

# Create the GUI elements
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

button = tk.Button(window, text="Calculate", command=calculate)
button.pack(pady=5)

output = tk.Label(window, text="Result: ")
output.pack(pady=10)

# Start the main loop
window.mainloop()
