# #Create a list with 5 items (names of people) and write a python program to output the 2nd item
# names = ["John", "Mary", "Peter", "Paul", "George"]
# print(names[1])

# #Write a python program to change the value of the first item to a new value
# names[0]="Conrad"
# print(names)

# #Write a python program to add a sixth item to the list
# names.append("David")
# print(names)

# # Write a python program to add “Bathel” as the 3rd item in your list
# names.insert(2, "Bathel")
# print(names)

# #Write a python program to remove the 4th item from the list
# # names.remove("Bathel")
# # print(names)

# names.remove(names[2])
# print(names)

# #Use negative indexing to print the last item in your list
# print(names[-1])

# #Create a new list with 7 items and use a range of indexes to print the 3rd, 4th and 5th items.
# names = ["John", "Mary", "Peter", "Paul", "George", "David", "Bathel"]
# print(names[3:6])

# # Write a list of countries and make a copy of it.
# countries =["Germany", "Italy","Uganda","canada"]
# countries_copy = countries.copy()
# print(countries_copy)
# print(countries)

# #Write a python program to loop through the list of countries
# for country in countries:
#     print(country)

# #. Write a list of animal names and sort them in both descending and ascending order
# animals = ["dog", "cat", "bird", "fish", "cow", "horse", "pig"]
# animals.sort()
# print(animals)
# animals.sort(reverse=True)
# print(animals)

#. Using the list above, write a python program to output only animal names with the letter 
# ‘a’ in them
# for animal in animals:
#     if "a" in animal:
#         print(animal)

# # Write two lists, one containing your first names and the other your second names. Join the two lists
# first_names=["Serumaga", "Sembutto"]
# second_names=["Conrad", "David"]
# names = first_names + second_names
# print(names)


####################################################################
#Exercise 2
# #1. Consider the tuple below;
# Write a python program to output your favorite phone brand.
x = ("samsung", "iphone", "tecno", "redmi")
# fav_phone = input("Form a scale of 1 to 10. How much do you like your phone ")

# if fav_phone in range(1,4):
#     print("Your favorite phone brand is " + x[2])
# elif fav_phone in range(4,7):
#     print("Your favorite phone brand is " + x[3])
# elif fav_phone in range(7,9):
#     print("Your favorite phone brand is " + x[0])
# elif fav_phone in range(9,11):
#     print("Your favorite phone brand is " + x[1])
 
# Use negative indexing to print the 2nd last item in your tuple. 
print(x[-2])

#Using the phones list above, write a python program to update “iphone” to “itel”
z = list(x)
z[1]="Itel"
x=tuple(z)
print(x)

#Write a python program to add “Huawei” to your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
c = list(x)
c.append("Huawei")
b=tuple(c)
print(b)

#Write a python program to loop through the tuple above.
for i in x:
    print(i)

#Write a python program to remove/delete the first item in your tuple.
x = ("samsung", "iphone", "tecno", "redmi")
v=list(x)
v.remove(v[0])
x = tuple(v)
print(x)

# Using the tuple() constructor, create a tuple of the cities in Uganda.
cities_in_ug=("Kampala", "Wakiso", "Gulu", "kololo")

#Write a python program to unpack your tuple
city1, city2, city3, city4=cities_in_ug
print(city1)
print(city2)
print(city3)
print(city4)

#9. Use a range of indexes to print the 2nd, 3rd and 4th cities in your tuple above.
for i in range(1,4):
    print(cities_in_ug[i])

#Write two tuples, one containing your first names and the other your second names. Join the two tuples
first_names=("Serumaga", "Sembutto")
second_names=("Conrad", "David")
names = first_names + second_names
print(names)

#. Create a tuple of colors and multiply it by 3
colors = ("turquoise", "green", "blue", "yellow")
print(colors*3)

# . Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# Count the number of occurrences of 8 in the tuple
count = thistuple.count(8)

print(count)



######################################################
# Exercise 3
#Use the set() constructor to create a set of 3 of your favorite beverages
drinks = {"coffee", "tea", "milk"}
print(drinks)

#Use the correct method to add 2 more items to the beverages set.
drinks.add("juice")
drinks.add("water")
print(drinks)

# Given the set below;
mySet = {"oven", "kettle", "microwave","refrigerator"}
# Check if microwave is present in the set.
if "microeave" in mySet:
    print("Microwave is in the set")

# Write a python program to remove “kettle” from the set above
mySet.remove("kettle")
print(mySet)

#5. Write a python program to loop through the set above.
for item in mySet:
    print(item)

# Write a set of 4 items and a list of two items. Write a python program to add elements in 
# the list to elements in the set
mySet = {"oven", "kettle", "microwave","refrigerator"}
drinks = ["coffee", "tea"]
print(mySet)
print(drinks)
mySet.update(drinks)
print(mySet)

#Write two sets, one containing your ages and the other your first names. Join the two sets
first_names= {"Serumaga", "Semakula"}
ages = {"20", "21"}
first_names.update(ages)
print(first_names)

######################################################
#Exercise 4
#. Declare two variables, an integer and a string and use the correct method to concatenate the two variables
integer = 3
string = "Python"
print(string +" is at a rate of {}".format(integer))

# Consider the example below
txt = " Hello, Uganda! "

# Output the string without spaces at the beginning, in the middle, and at the end
output = txt.strip()
print(output)

# Write a python program to convert the value of 'txt' to uppercase
uppercase_txt = txt.upper()
print(uppercase_txt)

# Write a python program to replace character 'U' with 'V' in the string above
replaced_txt = txt.replace('U', 'V')
print(replaced_txt)

# Using the code below, write a python program to return a range of characters in the 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
range_of_chars = y[1:4]
print(range_of_chars)

# The piece of code below will give an error when output
x = 'All "Data Scientists" are cool!'
# Write a python program to correct it by escaping the inner double quotes
x_corrected = 'All "Data Scientists" are cool!'
print(x_corrected)


##################################################
# Exercise5 (Dictionaries)

# With reference to the dictionary below, write a python program to print the value of the shoe size

Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoe_size = Shoes["size"]
print(shoe_size)

# Write a python program to change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print(Shoes)

# Write a python program to add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print(Shoes)

# Write a python program to return a list of all the keys in the dictionary above
keys_list = list(Shoes.keys())
print("Keys:", keys_list)

# Write a python program to return a list of all the values in the dictionary above
values_list = list(Shoes.values())
print("Values:", values_list)

# Check if the key "size" exists in the dictionary above
if "size" in Shoes:
    print("Key 'size' exists in the dictionary")
else:
    print("Key 'size' does not exist in the dictionary")

# Write a python program to loop through the dictionary above
for key, value in Shoes.items():
    print(key, ":", value)

# Write a python program to remove "color" from the dictionary
Shoes.pop("color")
print("Dictionary after removing 'color':", Shoes)

# Write a python program to empty the dictionary above
Shoes.clear()
print("Dictionary after clearing:", Shoes)

# Write a dictionary of your choice and make a copy of it
my_dict = {"name": "John", "age": 30, "city": "New York"}
my_dict_copy = my_dict.copy()
print("Original Dictionary:", my_dict)
print("Copied Dictionary:", my_dict_copy)

# Write a python program to show nested dictionaries
nested_dict = {
    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Alice", "age": 25}
}
print("Nested Dictionary:", nested_dict)
