#store multiple items in a single variable
#unchangeable but one can add and remove items

setone = {"rice", "matooke","Irish"}
print(setone)

#Duplicates in Sets
setone = {"rice", "matooke","Irish", "Irish"}
print(setone)

#Exercise find the length of your set, datatype,accessing items in sets
#Add items, Add two sets together

#length
fruit = {"apple", "banana", "cherry"}
print(len(fruit))

#datatype
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3, 4, 5}
set3 = {True, False, False}
print(type(set1))
print(type(set2))
print(type(set3))

#accessing items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Add items
set = {"apple", "banana", "mango"}
set.add("orange")
print(set)

#adding sets
fruits_for_poor = {"apple", "banana", "cherry"}
fruits_for_rich = {"pineapple", "mango", "papaya"}

fruits_for_poor.update(fruits_for_rich)

print(fruits_for_poor)

#remove items
fruits = {"apple", "jackfruit", "mango"}
fruits.remove("mango")
print(fruits)