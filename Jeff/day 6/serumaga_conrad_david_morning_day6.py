# # Regular expressions

# summary
# \d: Matches any digit (0-9).
# \w: Matches any alphanumeric character (a-z, A-Z, 0-9, and underscore)
# \s: Matches any whitespace character (space, tab, newline).
# .: Matches any character except a newline.
# *: Matches zero or more occurrences of the preceding character or group.
# +: Matches one or more occurrences of the preceding character or group.
# ?: Matches zero or one occurrence of the preceding character or group.
# [ ]: Matches any character within the square brackets. [^ 1: Matches any character not within the square brackets.
# ^: Matches the start of a line.
# $: Matches the end of a line.
# # Matching and Searching
# regex re.match(), re.search(), re.findall()

# Examplel Demonstrating regex | Match First Word, Match Group word, Matc

# import re
# text = "Hello, my name is Jeff Geoff. I am a programmer with 15years of experience"

# #Match first word
# match = re.search(r"\b\w+\b",text)

# if match:
#     print("Match: ",match.group())
    
# matches = re.findall(r"\d+", text)
# print("Matches:", matches)

#Example 2 validate iemail format
import re

# def validate_email(email):
#     pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
#     if re.match(pattern, email):
#         return True
#     else:
#         return False

# # Example usage:
# email1 = "example@example.com"
# email2 = "invalid_email"
# print(validate_email(email1))  # True
# print(validate_email(email2))  # False


# import re

# def validate_email(email):
#     email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
#     if re.match(email_regex,email):
#         return True
    
#     else:
#         return False
    
# email = input("Enter your email: ")
# print(validate_email(email))

#Generators and Iterators
#'yeild' generator
#Iterator '__iter__' "__next__" generator

def factorial(n):
    #Return the factorial of a number
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Print the factorial of a number from 1 - 10
for i in range(1,11):
    print(factorial(i))
    
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Usage:
fib_nums = fibonacci(100)
for num in fib_nums:
    print(num)

class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current
            self.current += 2
            return result
        else:
            raise StopIteration

# Usage:
even_nums = EvenNumbers(10)
for num in even_nums:
    print(num)

#Decorators @my_decorator
#DEcorators in python allows you to modify behaviour of functions or classes
#without directly changing their source code

def my_decorator(func):
    def inner():
        print("This is decorating")
        func()
    return inner

@my_decorator
def outer_decorator():
    print("This is outer decorator")
    
outer_decorator()