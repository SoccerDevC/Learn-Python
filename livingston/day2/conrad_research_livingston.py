# Create a dictionary with information about Conrad
conrad_dict = {
    "name": "Conrad",
    "age": 30,
    "city": "Kampala"
}

# Accessing values by key
print(conrad_dict["name"])  # Output: Conrad

# Modifying values by key
conrad_dict["age"] = 31
print(conrad_dict["age"])  # Output: 31

# Checking if a key exists in the dictionary
if "city" in conrad_dict:
    print("Key 'city' exists in Conrad's dictionary.")

# Removing a key-value pair
del conrad_dict["name"]
print(conrad_dict)  # Output: {'age': 31, 'city': 'Kampala'}

# Getting the number of key-value pairs in the dictionary
print(len(conrad_dict))  # Output: 2

# Iterating over keys
for key in conrad_dict:
    print(key)  # Output: age, city

# Iterating over values
for value in conrad_dict.values():
    print(value)  # Output: 31, Kampala

# Iterating over key-value pairs
for key, value in conrad_dict.items():
    print(key, value)  # Output: age 31, city Kampala

# Clearing the dictionary
conrad_dict.clear()
print(conrad_dict)  # Output: {}

# Deleting the dictionary
del conrad_dict

# Create a dictionary for Kampala city
kampala_dict = {
    "country": "Uganda",
    "population": 1.7,
    "language": "English",
    "timezone": "EAT"
}

# Accessing values by key
print(kampala_dict["country"])  # Output: Uganda

# Modifying values by key
kampala_dict["population"] = 2.5
print(kampala_dict["population"])  # Output: 2.5

# Checking if a key exists in the dictionary
if "language" in kampala_dict:
    print("Key 'language' exists in Kampala's dictionary.")

# Removing a key-value pair
del kampala_dict["timezone"]
print(kampala_dict)  # Output: {'country': 'Uganda', 'population': 2.5, 'language': 'English'}

# Getting the number of key-value pairs in the dictionary
print(len(kampala_dict))  # Output: 3

# Iterating over keys
for key in kampala_dict:
    print(key)  # Output: country, population, language

# Iterating over values
for value in kampala_dict.values():
    print(value)  # Output: Uganda, 2.5, English

# Iterating over key-value pairs
for key, value in kampala_dict.items():
    print(key, value)  # Output: country Uganda, population 2.5, language English

# Merging two dictionaries
merged_dict = {**conrad_dict, **kampala_dict}
print(merged_dict)  # Output: {'age': 31, 'city': 'Kampala', 'country': 'Uganda', 'population': 2.5, 'language': 'English'}

# Clearing the dictionary
kampala_dict.clear()
print(kampala_dict)  # Output: {}

# Deleting the dictionary
del kampala_dict
