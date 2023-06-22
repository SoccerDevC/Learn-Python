#They are used to store many items in a single variable
#Lists are ordered,Allow duplicate items

#Afternoon = ["Trevor","Peter","Blessing"]
#print(Afternoon)
#Duplicates in Lists, 

Afternoon = ["trevor", "Peter","Blessing","Trevor","Trevor","Blessing"]
print(Afternoon)

#list length
print(len(Afternoon))

#list type
print(type(Afternoon))
#Access List Items
print(Afternoon[2])
print(Afternoon[-3])
print(Afternoon[-5])
#Accessing a range of items
print(Afternoon[3:5])
#value attached to first index is outputed but not the last
print(Afternoon[:5])
print(Afternoon[1:])
#Adding items to lists
Afternoon.append("Martha")
Afternoon.remove
Afternoon.insert(0,"Cono")
Afternoon.pop(5)
print(Afternoon)