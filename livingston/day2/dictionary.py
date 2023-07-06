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
cars={"toyota":"premio",
      "number_plate":2323}
print(cars)