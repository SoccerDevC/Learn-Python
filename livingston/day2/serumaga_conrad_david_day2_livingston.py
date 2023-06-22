#used to store data values in key pairs
#Dictionaries are ordered, changeable but do not allow duplicates
#Dicts can have items of any data type

mydict={
    "name":"Conrad",
    "age":30,
    "city":"New York",
    "phone":"iphone",
    "iphonemodel":"iphone15",
    "year":2023
}
print(mydict)

#length of a dictionary
print(len(mydict))

#datatype of a dictionary
print(type(mydict))

#Acces dictionary items
z = mydict["year"]
print(z)
y=mydict.get("iphonemodel")
print(y)
w = mydict.keys()
print(w)

#Excercise One : use the values () method to return a list of values in the dictionary

# u = mydict.values()
# print(u)

#Exercise two: to check if a key does exist in the dictionary

# key = input("Enter a key")
# if key in mydict:
#     print ("Key exists in the dictionary")
# else:
#     print("key doesn't exist")


#execise three: Give an example on how to change dictionary items, How to update

#Changing an existing item in the dictionary
# mydict["name"]="David"
# print(mydict)

#How to update multiple items in the dictionary
# update_dict = {
# "name": "Serumaga",
# "age":20,
# "phone":"Samsung",
# }

# mydict.update(update_dict)
# print(mydict)

#Excercise four: Give an example on how to add dictionary items, how to remove dictionary items

# mydict["sex"]="male"
# mydict["course"]="BSSE"
# print(mydict)

#adding items using another dictionary
# add_dictionary ={
#     "fav_drink":"Water",
#     "bd":"november"
# }
# mydict.update(add_dictionary)
# print(mydict)

#delete dictionary items
# del mydict["name"]
# print(mydict)

#Excercise five : Give an example on how you can loop through a dictionary and also how to nest dictionaries
# Creating a nested dictionary
student_scores = {
    "John": {"Math": 90, "Science": 85, "English": 92},
    "Alice": {"Math": 95, "Science": 88, "English": 89},
    "Michael": {"Math": 82, "Science": 90, "English": 78}
}

# Looping through the outer dictionary
for student, scores in student_scores.items():
    print(f"Student: {student}")
    for subject, score in scores.items():
        print(f"\t{subject}: {score}")



##########################################
#numbers in python
# floats, complex numbers, integers
w= 10
r=3.9
s=2j

#print(type(w))
#print(type(r))
#print(type(s))

#integers

a = 2
b = 52343533
c = -353252

print(type(a))
print(type(b))
print(type(c))

#floats

g = 2.89
z = 3.3
e = -76.983

print(type(g))
print(type(z))
print(type(e))

#complex numbers

w = 6 + 10j
t = 4j
h = -2j

print(type(w))
print(type(t))
print(type(h))

#type conversions
w = 10 #int
r=3.9 #float
s = 2j #complex

#convert from int to complex
z=complex(w)
print(z)
print(type(z))

#convert from float to complex
z= complex(z)
print(z)
print(type(z))

#convert from int to float
z=float(w)
print(z)
print(type(z))


#convert from complex to float
z= float(z)
print(z)
print(type(z))

##########################################################3
#casting_livingston

#works mostly when you want to specify a variable type
#casting works on int, string and float

h = int(20) #h is 20
y = int(30000) #y is 30000
a = int("8") #a is 8
print(h)
print(y)
print(a)
print(type(a))

########################################################
#strings
#python shows a single character as a string
print("Afternoon")
print('Afternoon')
#assign string a variable
w = "Afternoon"
print(w)
#multiline strings
q = """ I am offering BSSE Year three
Currently doing recess in python,
Data science, Django. """

print(q)

# strings as arrays
a= "Afternoon"
print(a[1])
print(a[2])

#Excercise one: use the len() function to determine the length of the string
print(len(a))

#Excercise two: Give an example of using a for loop in a string
for x in a:
    print(x)
#Exercise three: Give an example of slicing in strings
print(a[0:3])
print(a[:3])
print(a[3:])
print(a[3:6])
print(a[3:6:2])
print(a[::2])

#how to modify strings
a = "Afternoon"
print(a.lower())

print(a.upper())

#remove whitespaces
b = " After noon "
print(b.strip())
print(b)

#String Concatenation
c="Afternoon"
d ="Class"
w = c + d
# print(w)
z= c + " " + d
print(z)


####################################################
#format_ Strings
# Works when one wants to combine a string to a number
#we need to use the format method
# this format () takes the first parameters, formats them and places them in the string where the place holders are

#this no longer works
# age = 23
# name = " My name is livingston, I am " + age
# print(name)

# age =23
# name ="My name is Conrad, I am {}"
# print(name.format(age)) 

# grade = 3
# name = "Conrad"
# city = "London"
# print("My name is {} and I live in {}.".format(name,city))

course = "BSSE"
year = 2
name = " Conrad"
age = 20

print("My name is {}, I am {} years old, doing {} in year {} ".format(name,age,course,year))

#######################################
#Boolean
#These evaluate to a true or false
print(20 < 10)
print(30 == 40)
print(30 > 10)

print(bool(15))

r="Conrad"
z=30

print(bool(r))
print(bool(z))
#Exercise Use a condition to show how to use booleans

name = "Conrad"

if name =="Conrad":
    print("You are welcome to your Dashboard Conrad!")
else:
    print("We don't know you")

