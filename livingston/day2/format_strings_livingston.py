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

