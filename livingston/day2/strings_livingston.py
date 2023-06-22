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
