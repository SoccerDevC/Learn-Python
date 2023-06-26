# Object Oriented Programming
# Class
# Object
# Encapsulation
# Inheritence
# Polymorphism
# Abstractraction

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# class Car:
#      def __init__(self,make,model,year):
#          self.make = make
#          self.model = model
#          self.year = year
#      def start_engine(self):
#          print("Engine started")

#      def stop_engine(self):
#          print("Engine stopped")

# car = Car("Prado","tx",2023)
# car.start_engine()
# car.stop_engine()

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self,amount):
#         self.balance += amount
#         print(self.balance)
#     def withdraw(self,amount):
#         self.balance -= amount
#         print(self.balance)

# b1 = BankAccount("John",1000)
# b1.deposit(500)
# b1.withdraw(500)

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#     def area(self):
#         return self.length * self.width
#     def perimeter(self):
#         return 2 * (self.length + self.width)

# r1 = Rectangle(2,3)
# print(r1.area())
# print(r1.perimeter())


# class Student:
#     def __init__(self, name, year, course):
#         self.name = name
#         self.year = year
#         self.course = course

#     def display_details(self):
#         print(self.name, self.year, self.course)


# ##Create student object
# my_student = Student(name="Conrad", year=2000, course="BSSE")

# # Display student details
# my_student.display_details()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello", self.name, self.age)


# # Exercise 1
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def calculate_area(self):
#         return 3.14 * self.radius * self.radius

#     def calculate_circumference(self):
#         return 2 * 3.14 * self.radius


# # Create circle object

# my_circle = Circle(7)
# print(my_circle.calculate_area())
# print(my_circle.calculate_circumference())

# # Exercise2
# # Calculate and display employee bonuses(15%) of salary (employee1: 150000, employee2: 230000)


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def calculate_bonus(self):
#         return self.salary * 0.15


# # Create employee object

# employee1 = Employee("John", 150000)
# employee2 = Employee("Mary", 230000)

# print(employee1.calculate_bonus())
# print(employee2.calculate_bonus())

# # Encapsulation

# # key main goals of encapsulation are
# """
# 1. To hide implementation details of the object
# 2. To protect object from changes
# 3. To prevent the object from external changes
# 4. Code organization and modularity
# """
# # Example4: with Bank account


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number  # Encapsulates account number attribute
#         self._balance = balance  # Encapsulates balance attribute

#     def deposit(self, amount):
#         self._balance += amount  # Encapsulates the seposit

#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self._balance


# # create a bank object

# my_account = BankAccount("1234", 1000)

# # Access the Bank object and modify encapsulated attributes indirectly
# print(my_account._account_number)
# print(my_account._balance)
# my_account.deposit(500)
# print(my_account._balance)
# my_account.withdraw(100)

# print(my_account._balance())

# Exercise 3: Convert temperature(37) from Celsius to fahrenheit


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def ferenheit(self):
        return (self._celsius * 9 / 5) + 32


temp = Temperature(30)
print(temp.ferenheit())

# Assignment 1: show encapsulation with employee information to give a
# pay increamentation (Salary with employee information to new_salary) e.g from 850000 to 1000000


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
