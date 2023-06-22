#Tuples are used to store items in a single variable
#Tuples are ordered and unchangeable

phones = ("samsung", "iphone","Techno")
print(phones)

#Still allow for duplicate values
phones = ("samsung", "iphone","Techno","Techno","samsung")
print(phones)
#Exercise use the len() with this tuple example
print(len(phones))

#tuples showing different data types

Tuple1 = ("matooke","rice")
Tuple2 = (100,200,300,500)
print(Tuple1)
print(Tuple2)

#Excercise How to access tuples
#Add items to a tuple
phones = ("samsung", "iphone","Techno")
z = list(phones)
z.append("Nokia")
phones=tuple(z)
print(phones)

#remove items from a tuple
phones = ("samsung", "iphone","Techno")
t=list(phones)
t.remove("iphone")
phones=tuple(t)
print(phones)

#adding two tuples
phones = ("samsung", "infinix","Techno")
phones_for_the_rich=("Iphone",)
phones += phones_for_the_rich
print(phones)
phones += phones_for_the_rich
print(phones)

#Unpacking a tuple ie extracting values into variables
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#using astericks ie to cater for more values than variabless
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#for loop in a tuple
phones = ("samsung", "infinix","Techno")
for y in  phones:
    print(y)
