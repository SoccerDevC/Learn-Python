#control flow
# If/else statements allow you to execute different blocks of code based on conditions.

# # Example 1:
# x = 10
# if x > 5:
#     print("x is greater than 5")
# else:
#     print("x is less than or equal to 5")

# # Example 2:
# name = "Alice"
# if name == "Alice":
#     print("Hello, Alice!")
# else:
#     print("Hello, stranger!")

#elif
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")


# While loops repeatedly execute a block of code as long as a condition is true.

# # Example 1:
# count = 0
# while count < 5:
#     print("Count:", count)
#     count += 1

# # Example 2:
# num = 10
# while num > 0:
#     print("Number:", num)
#     num -= 2

# # Example 3:
# password = ""
# while password != "secret":
#     password = input("Enter the password: ")
#     if password == "secret":
#         print("Access granted!")
#     else:
#         print("Access denied!")

# For loops iterate over a sequence (such as a list, tuple, or string) or other iterable objects.

# # Example 1:
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# # Example 2:
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for num in numbers:
#     sum += num
# print("Sum:", sum)

# # Example 3:
# name = "Python"
# for char in name:
#     print(char)


# fruits = ["Banana", "orange", "apple", "lemon", "Banane"]

# for x in fruits:

# print(x)

# X=0
# while x < 5:
#     print(x)
#     X+=1


# #Using Break
# even_number = []
# odd_number = []
# print("Enater 100 in order to stop the loop")
# i = 0
# while (1,10):
#     number = int(input("Enter number:"))
#     if (number % 2 == 1):
#         if (number == 100):
#             break
#         even_number.append(number)
#     else:
#         odd_number.append(number)
# print(even_number)
# print(odd_number)


# #break statement
# for number in range(1,10):
#     if number == 5:
#         break
#     print(number)

# #example 2
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# #continue statement
# for number in range(1,10):
#     if number == 5:
#         continue
#     print(number)

#Exception handling

# # Example 1:
# num1 = 10
# num2 = 0

# try:
#     result = num1 / num2
#     print("Division result:", result)
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# finally:
#     print("Finally block executed.")

# # Output:
# # Error: Division by zero is not allowed.
# # Finally block executed.


# # Example 2:
# numbers = [10, 20, 0, 30, 40]

# try:
#     for num in numbers:
#         result = 100 / num
#         print("Division result:", result)
        
#         # if result == 10:
#         #     break
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except Exception as e:
#     print("Error:", str(e))

# # Output:
# # Division result: 10.0

# # Example 3:
# try:
#     num = int("abc")
#     print("Converted number:", num)
# except ValueError:
#     print("Error: Invalid value provided.")
# except Exception as e:
#     print("Error:", str(e))

# # Output:
# # Error: Invalid value provided.

#Example 4
#Dict is a dictionary {}

# emotion ={
#     "happy": "I'm glad to hear you're happy",
#     "sad": "I'm sorry to see you' sad",
#     "angry":"take a deep breath and stay alive",
#     "fearful":"I understand that fear can be challenging",
#     'disgusted': "That's unfortunte to feel disgusted",
# }
# #Prompt the user to enter their emotions
# user_emotion = input("How are you feeling today")

# #convert the user input to lowercase
# user_emotion = user_emotion.lower()

# if user_emotion in emotion:
#     print(emotion[user_emotion])
# else:
#     print("I'm sorry i don't understand your emotion")

# #print(user_emotion)


#EXERCISE
# print("Welcome to the Student Mental Health Survey!")

# # Create an empty dictionary to store the responses
# survey_responses = {}

# # Ask for student information
# name = input("Please enter your name: ")
# grade = input("Please enter your grade: ")

# # Ask survey questions
# print("\nSurvey Questions:")
# print("1. How are you feeling today?")
# feeling = input("   Enter your response: ")
# print("2. Have you been experiencing any stress or anxiety lately?")
# stress_anxiety = input("   Enter your response (yes/no): ")
# print("3. Are you getting enough sleep?")
# sleep = input("   Enter your response (yes/no): ")

# # Store the responses in the dictionary
# survey_responses[name] = {
#     "Grade": grade,
#     "Feeling": feeling,
#     "Stress/Anxiety": stress_anxiety,
#     "Sleep": sleep
# }

# # Print a summary of the survey responses
# print("\n--- Survey Summary ---")
# for name, response in survey_responses.items():
#     print("Name:", name)
#     for question, answer in response.items():
#         print(question + ":", answer)

# # You can further process or analyze the survey responses as per your requirements

print("Welcome to Conrad's mental health facility")

responses={
    "1":"Everything will be okay.",
    "2":"Nothing is impossible, so you can make it",
    "3":"Well, hope you feel better",
    "4":"You're not alone!",
    "5":"Hope we can make you feel better",
    "6":"This is relatively good",
    "7":"This is pretty good",
    "8":"This is good",
    "9":"This is great",
    "10":"This is amazing",
    
}
response = input("From a scale of 1 to 10 rate your mental health")
print(responses[response])