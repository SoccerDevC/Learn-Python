class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is woofing")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")


dog = Dog("Spot")
cat = Cat("Fluffy")

dog.eat()   # Output: Spot is eating
dog.bark()  # Output: Spot is woofing

cat.eat()   # Output: Fluffy is eating
cat.meow()  # Output: Fluffy is meowing
 

#Example 2 Demonstrating inheritance

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        print("Brand:", self.brand)
        print("Color:", self.color)

    def move(self):
        print("Vehicle is moving...")


class Car(Vehicle):
    def __init__(self, brand, color, num_wheels):
        super().__init__(brand, color)
        self.num_wheels = num_wheels

    def display_info(self):
        super().display_info()
        print("Number of wheels:", self.num_wheels)

    def honk(self):
        print("Honking the horn....")


# Create a Car object
my_car = Car("Toyota", "Red", 4)

# Access and modify the car attributes
print("Brand:", my_car.brand)  # Output: Brand: Toyota
my_car.color = "Gray"

# Invoke the car methods
my_car.display_info()
my_car.move()
my_car.honk()


# #Excercise 
#calculate the area and perimeter of a circle and rectangle using inheritance
class Shape:
    def __init__(self, length):
        self.length = length

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Create a Circle object
circle = Circle(5)
rectangle = Rectangle(2, 3)
print(circle.area() )     # Output: 78.5
print(rectangle.area())   # Output: 6

#Multiple Inheritence
class Animal:
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating...")
        
class Flyable:
    def fly(self):
        print(f"{self.name} is flying")
        
class Bird(Animal, Flyable):
    def __init__(self, name,species):
        super().__init__(name)
        self.species =species
        
    def display_info(self):
        # super().display_info()....generates an error
        print(f"Species: {self.species}")
        print(f"Name: {self.name}")
        
        
# Create a Bird object
my_bird =Bird("Pigeon", "bird")

#invoke the bird method
my_bird.eat()
my_bird.fly()
my_bird.display_info()

#Method overiding

class Animal:
    def make_sound(self):
        print("Animal is making a sound!")
        
class Dog(Animal):
    def make_sound(self):
        print("Dog is barking")
        
class Cat(Animal):
    def make_sound(self):
        print("Catis meowing")

def make_animal_sound(animal):
    animal.make_sound()
    
#Create objects
animal = Animal()
dog =Dog()
cat = Cat()

# Implement 
make_animal_sound(animal)#Output: Animal is making a sound
make_animal_sound(dog)#Output :Dog is barking
make_animal_sound(cat) #Output: Cat is barking

#Polymorphism allows you to write code that can work with different objects
#implementation of a method that is already defined in its base class
#Methods OverridingOccurs when a derived class, subclass, (child class), provides its own,
#Method Overloading allows a class to have multiple methods with the same name but different parameters 

#Example 4
class Shape:
    def calculate_area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def calculate_area(self):
        return self.length * self.width
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def calculate_area(self):
         return 3.14 * self.radius**2
     
    def calculate_circumference(self):
         return 3.14 * self.radius
     
    #Create shape objects
rectangle = Rectangle(5,5)
circle =Circle(4)
print("Rectangle Area: ", rectangle.calculate_area)
print("Circle Area:", circle.calculate_area)

#Overloading functions
class Calculator:
    def add(self, x, y):
        return x + y
    def add(self, x, y,z):
        return x + y +z
    
#create object
calculator = Calculator()

#Displays last method

#Abstraction 
#allow you to focus on essential features and hide them from unecessary details

#Example 5: Demonstrate abstractions
from abc import ABC, abstractclassmethod

class Vehicle(ABC):
    def start(self):
        pass
    
class Car(Vehicle):
    def start(self):
        print("car is starting...")
        
    def stop(self):
        print("Stopping car")
        
class Truck(Vehicle):
    def start(self):
        print("truck is starting...")
        
    def stop(self):
        print("Stopping the truck")
        
#Create Vehicle objects
car = Car()
truck =Truck()

#Start the vehicle
car.start()
truck.start()

#stop the vehicle
car.stop()
truck.stop()

#Exercise 2
#DEmonstrate Abstraction using calculating area of a circle and rectangles
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


# Create a Rectangle object
rectangle = Rectangle(2, 3)
print("Rectangle Area:", rectangle.calculate_area())

# Create a Circle object
circle = Circle(5)
print("Circle Area:", circle.calculate_area())

#Assignment 1 
#Create a Receipt printing program with a GUI interface, 
# a more advanced detail earns more points