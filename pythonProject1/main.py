# #This is my start on python
# print ("I like kebab!")
# print("It's really good!")

# #variables -- A reusable container for a value (string, integer, float, boolean) The variable behaves as if it was the value that it contains
# full_name = "Nikola Dimov"
# age = 19
# gpa = 3.3
# is_student = False
#
# print(f"Hello {full_name}")
# print(f"Your age is {age}")
# print(f"Your GPA is {gpa}")
#
# if is_student:
#     print("You are a student")
# else:
#     print("You are not a student")

# #arithmetics -- + addition| - subtraction| * multiplication| / division(returns a float)| // integer division(returns an integer)| % remainder
# friends = 10
# # addition friends += 1
# # subtraction friends -= 2
# # multiplication friends *= 2
# # division friends /= 2
# # integer divion friends //= 3
# # remainder remaining_friends = friends % 3
# print(remaining_friends)

# #Typecasting -- the process of converting a variable from one data type to another| str(),int(),float(), bool()
# name = ""# empty string in bool is false but with something in it is true
# age = 19
# gpa = 3.2
# is_student = True
# print(type(is_student))
# gpa = int(gpa)
# age = float(age)
# age = str(age)
# print(type(age))
#
# name = bool(name)
# print(name)

# #input function -- displays a message asking the user to type something| The function waits for the user to type and press Enter| The input is captured as a string (text)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# age += 1
# print(f"Hello {name}! ")
# print(f"You are {age} years old")

# #if statements -- execute some code only if a codition is True they allow for basic decision-making| (if, elif, else)
# age = int(input("Enter your age: "))
# has_ticket = True
# price = 10.00
#
# if age>= 65:
#     print("You are senior citizen")
#     print(f"The ticket price for an senior is ${price * 0.75}")
# elif age >= 18:
#     print("You are and adult")
#     print(f"The ticket price for an adult is ${price}")
# else:
#     print("You are a child")
#     print(f"The ticket price for a child is ${price * 0.5}")
#
# if has_ticket:
#     print("You may enter, you have a ticket")
# else:
#     print("You need a ticket")

# #logical operators -- evaluate multiple conditions (or, and, not)

# ##or -- at least on condition must be True
# temp = 25
# is_raining = False
#
# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is canceled")
# else:
#     print("The outdoor event is on")

# ##and -- both conditions must be True
# temp = 20
# is_sunny = True
# if temp >= 28 and is_sunny:
#     print("It is HOT outside")
#     print("It is SUNNY")
# elif temp <= 0 and is_sunny:
#     print("It is Cold outside")
#     print("It is SUNNY")
# elif 28 > temp > 0 and is_sunny:
#     print("It is Warm outside")
#     print("It is SUNNY")

# ##not -- inverts the condition (not False, not True
# temp = 0
# is_sunny = False
# if temp >= 28 and is_sunny:
#     print("It is HOT outside")
#     print("It is SUNNY")
# elif temp <= 0 and is_sunny:
#     print("It is Cold outside")
#     print("It is SUNNY")
# elif 28 > temp > 0 and is_sunny:
#     print("It is Warm outside")
#     print("It is SUNNY")
# elif temp >= 28 and not is_sunny:
#     print("It is Hot outside")
#     print("It is Cloudy")
# elif temp <= 0 and not is_sunny:
#     print("It is Cold outside")
#     print("It is Cloudy")
# elif 28 > temp > 0 and not is_sunny:
#     print("It is Warm outside")
#     print("It is Cloudy")

# #while loop -- used to repeat a block of code as a condition remains 'True'  we re-check the condition at the end of the loop
# name = input("Enter your name: ")
#
# while name == "":
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#
# while age < 0 :
#      print("Age can't be negative")
#      age = int(input("Enter your age: "))
#
# print(f"Hello {name}")
# print(f"Your age is {age}")

# #for loop -- used to iterate over a sequence (sting, list, tuple, set) repeat a block of code an exact amount of times
# for i in range(1, 11, 2):
#     print(i)
# name = "Nikola"
# for letter in name:
#     print(letter, end ="-")
# for i in range(10, 0, -1):
#     print(i)
# print("Happy new Year!")
# import time
# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)
# print("Happy new Year!")

# ##List[] -- mutable , most flexible
#fruits = ["apple", "pear", "orange", "banana"]
#fruits[0] = "mango"
#fruits.append("mango")
#fruits.remove("banana")
#fruits.pop(0)
#fruits.clear()
# for fruit in fruits:
#     print(fruit, end=" ")

# ##Tuple () -- immutable, faster
# fruits = ("apple", "pear", "orange", "banana")
# for fruit in fruits:
#      print(fruit, end=" ")

# ##Set {} = mutable(add/remove), unordered, NO duplicates, best for membership testing
#fruits = {"apple", "pear", "orange", "banana"}
#fruits.add("mango")
#fruits.remove("banana")
#fruits.pop()

