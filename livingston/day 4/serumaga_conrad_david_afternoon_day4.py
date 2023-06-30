# #Group blocks of code
# #There is need for code that is clean, reusable, maintainable

# #Declaring a function
# #def function_name():

# def afternoon():
#     name = input("What is your name: ")
#     print("Good afternoon!", name)
#     print("Class starts at 2pm")

# def driver(name="Boy"):
#     print("Hello", name)

# def age(x = 20):
#     return x

# def add(x, y):
#     return x + y

# def subtract(y,x = 6):
#     return x - y

# #Calling a function
# afternoon()

#Function parameters and arguments
#Arguments are specified after the function name
#parameters are the

#A simple calc
# def add(s,w):
#     return(s + w)

# def product(s,w):
#     return(s * w)

# import serumaga_conrad_david_afternoon_day4
# print(serumaga_conrad_david_afternoon_day4.product(8,4))

# # #Try not to import a module within itself

# #importing square root and factorial from the module math
# from math import *

# print(sqrt(16))
# print(factorial(5))

# #Or 
# import math

# print(math.sqrt(16))
#print(math.factorial(5))

#input and output in python
#input('prompt')

# name = input("Enter your name: ")
# print("My name is,", name)

# #Example 2

# number = int(input("Enter a number: "))
# product = number *10
# print(product)

# #Multiple inputs in python

# s,r,w = map(int, input("Enter the Values : ").split())
# print("The values are :", end =" ")
# print(s,r,w)

#How to capture input from a tuple
# w = (2,4,6,5,8)
# print("Current tuple")
# print(w)
# print(type(w))

# E = list(w)
# E.append(int(input("Enter new value:")))
# W=tuple(E)
# print("Updated tuple")
# print(w)

mylist = list(map(int, input("Enter the list values : ").split()))
myset = set(map(int, input("Enter the set values : ").split()))

print(mylist)
print(myset)
# my_set = {"conrad", "David"}
# print("Current set")
# print(my_set)