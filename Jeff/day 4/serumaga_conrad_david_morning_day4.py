# Object Oriented Programming
# Class
# Object
# Inheritence
# Polymorphism\
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


class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print(self.name, self.year, self.course)


##Create student object
my_student = Student(name="Conrad", year=2000, course="BSSE")

# Display student details
my_student.display_details()
