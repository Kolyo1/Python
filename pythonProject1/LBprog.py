# print("Enter a :")
# a = float(input())
# print("Enter b :")
# b = float(input())
# print("Enter h :")
# h = float(input())
# S1 = ((a+b)*h)/2
# print(f" {S1:.2f} sm^2")
#
#
# r = float(input("Enter r :"))
# S2 = math.pi*math.pow(r, 2)
# P = 2*math.pi*r
# print(f" {S2:.3f} sm^2")
# print(f" {P:.3f} sm")
#
# money = float(input("Enter money :"))
# moneyItem = float(input("Enter money Item :"))
# change = money-moneyItem
# if change < 0:
#     print(f"Не достигат с {change: .2f} lv")
# else :
#     print(f"Change {change:.2f} lv")
from traceback import print_tb

from fontTools.misc.cython import returns

#
# priceHour = int(input("Enter priceHour : "))
# hour = int(input("Enter hour : "))
# if hour <= 1:
#     print("No tax!")
# elif hour > 1 and hour <= 10:
#     print(f" {priceHour * hour} lv.")
# elif hour > 10:
#     print(f" {(priceHour *2) * hour} lv.")
#
# firstName = input("Enter First Name ")
# lastName = input("Enter Last Name ")
# updatedFistName = firstName[1:-1]
# n = 4
# for i in range(n):
#     if i ==1:
#         print(f"Hello, {firstName} {lastName}!")
#     elif i == 2:
#         print(f"Hello, {lastName} {firstName}!")
#     elif i == 3:
#         print(f"Hello, {updatedFistName} !")

# num = float(input("Въведете num : "))
# n = float(input("Въведете n : "))
# sumAll = 0
# c = 0
# if n > 0 and num > 0:
#     while n > 1 and n <= 5:
#
#         while c < n:
#             sumAll += num
#             c += 1
#     if sumAll % 2 == 0:
#         print(f"Сумата е четна : {sumAll}")
#     else:
#         print(f"Сумата е нечетна : {sumAll}")

#
# n = int(input("Enter n : "))
# if n <= 6 and n > 2:
#     my_nums = []
#     even = []
#     odd = []
#
#     for i in range(n):
#         b = input("Enter elements: ")
#         my_nums.append(b)
#
#     for number in my_nums:
#         try:
#             float_number = float(number)
#             if float_number.is_integer():
#                 if int(float_number) % 2 == 0:
#                     even.append(number)
#                 else:
#                     odd.append(number)
#             else:
#                 print(
#                     f"{number} is a float and cannot be classified as even or odd in integer terms."
#                 )
#         except ValueError:
#             print(f"Invalid input: {number} is not a number.")
#
#     print(f"Even: {even}")
#     print(f"Odd: {odd}")

# age = int(input("Enter age : "))
# if age >= 18:
#     print("You are an adult")
# elif age < 18 and age >= 12:
#     print("You are a teenager")
# elif age < 12:
#     print("You are a child")
# elif age == 0:
#     print("You are a baby")

# grade = float(input("Enter grade: "))
# while grade >= 0 and grade <= 100:
#     if grade >= 90:
#         print("Excelent!")
#     elif grade >= 70 and grade < 90:
#         print("Good!")
#     elif grade >= 50 and grade < 70:
#         print("Satisfactory!")
#     elif grade >= 30 and grade < 50:
#         print("Unsatisfactory!")
#     elif grade < 30:
#         print("Fail!")

# for i in range(11):
#     for j in range(11):
#         res = i * j
#         print(f"{i} * {j} = {res} ")

# from itertools import permutations
#
#
# def generate_permutations(target_sum, number_count):
#     result = []
#     numbers = list(range(1, 11))
#
#     for permutation in permutations(numbers, number_count):
#         if sum(permutation) == target_sum:
#             result.append(permutation)
#
#     return result
#
#
# target_sum = 15
# number_count = 3
# result_permutations = generate_permutations(target_sum, number_count)
#
# print("Permutations of 3 numbers summing to 15:")
# for perm in result_permutations:
#     print(perm)

# import random
# 
# 
# def get_computer_choice():
#     choices = ["rock", "paper", "scissors"]
#     return random.choice(choices)
# 
# 
# def get_user_choice():
#     user_input = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
#     while user_input not in ["rock", "paper", "scissors"]:
#         print("Invalid choice, please try again.")
#         user_input = (
#             input("Enter your choice (rock, paper, or scissors): ").strip().lower()
#         )
#     return user_input
# 
# 
# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (
#         (user_choice == "rock" and computer_choice == "scissors")
#         or (user_choice == "paper" and computer_choice == "rock")
#         or (user_choice == "scissors" and computer_choice == "paper")
#     ):
#         return "You win!"
#     else:
#         return "Computer wins!"
# 
# 
# def play_game():
#     computer_choice = get_computer_choice()
#     user_choice = get_user_choice()
# 
#     print(f"You chose: {user_choice}")
#     print(f"Computer chose: {computer_choice}")
# 
#     result = determine_winner(user_choice, computer_choice)
#     print(result)
# 
#
#     play_game()

# def add(x, y):
#     return x + y
#
#
# def subtract(x, y):
#     return x - y
#
#
# def multiply(x, y):
#     return x * y
#
#
# def divide(x, y):
#     if y == 0:
#         raise ValueError("Не може да се дели на 0!")
#     return x / y
#
#
# def calculator():
#     print("Изберете действие : ")
#     print("1. Събиране")
#     print("2. Изваждане")
#     print("3. Умножение")
#     print("4. Деление")
#
#     while True:
#         choice = input()
#
#         if choice in ['1', '2', '3', '4']:
#             try:
#                 num1 = float(input("Въведете първото число : "))
#                 num2 = float(input("Въведете второто число : "))
#             except ValueError:
#                 print("Грешно. Въведете числа")
#                 continue
#
#             if choice == '1':
#                 print("Събиране")
#                 print(f"{num1} + {num2} = {add(num1, num2)}")
#             elif choice == '2':
#                 print("Изваждане")
#                 print(f"{num1} - {num2} = {subtract(num1, num2)}")
#             elif choice == '3':
#                 print("Умножение")
#                 print(f"{num1} * {num2} = {multiply(num1, num2)}")
#             elif choice == '4':
#                 print("Деление")
#                 try:
#                     print(f"{num1} / {num2} = {divide(num1, num2)}")
#                 except ValueError as e:
#                     print(e)
#             break
#         else:
#             print("Грешно въвеждане")
#calculator()

# def polidrome():
#     a = input("Enter : ")
#     if a == a[::-1]:
#         return (f"{a} is a polidrome")
#     else:
#         return (f"{a} is a not polidrome")
# 
# print(polidrome())

# import random
#
# def categorize_numbers(n):
#     if n < 5 or n > 10:
#         raise ValueError("n трябва да е между 5 и 10.")
#
#     numbers = [random.randint(-100, 100) for _ in range(n)]
#     categorized_numbers = [0 if num < 0 else 1 for num in numbers]
#
#     return numbers, categorized_numbers

# n = int(input("Enter n : "))
# try:
#     random_numbers, result = categorize_numbers(n)
#     print(f"Първи лист: {random_numbers}")
#     print(f"Променен лист: {result}")
# except ValueError as e:
#     print(e)

# n = int(input())
# while True:
#     list_1 = []
#     dict_1 = {}
#     if n>5 and n<10:
#         for i in range(1,n+1):
#             list_1.append(i)
#         for items in range(len(list_1)):
#             dict_1[list_1[items]] = list_1[len(list_1) - 1 - items]
#         for key, value in dict_1.items():
#             print(f"{key}:{value}")
#         break
#     else:
#         print("Invalid input")
#     continue
#    print(dict_1)

# from collections import Counter
# str = input("Enter a string: ")
# counter = Counter(str)
# for char, count in counter.items():
#     print(f"{char}: {count}")

# import random
# n = int(input())
# list_2 = [random.randint(-100, 100) for _ in range(n)]
# print(list_2)
# updated_list = [0 if a < 15 else 1 for a in list_2]
# print(updated_list)

# import random
# import secrets
# import string

# n = int(input())
# lst = [random.randint(-100,100) for i in range(n)]
# print(lst)
# print(max(lst))

# numberstr = int(input())
# length = int(input())
# characters = string.ascii_letters + string.digits
# llst = []
# while len(llst) < numberstr:
#     random_string = ''.join(random.choices(characters, k=length))
#     if len(set(random_string)) > 5:
#         llst.append(random_string)
# print(llst)

# import random
#
# n = int(input())
# m = int(input())
#
# lst1 = []
# lstodd = []
# lsteven = []
# lst2 = []
#
# for i in range(1,n+1):
#     lst1.append(random.randint(1,100))
# print("List1 ",lst1)
#
# for b in range(1,n+1):
#     lst2.append(random.randint(1,100))
# print("List2 ",lst2)
#
# common = set(lst1) & set(lst2)
# print("Common elements from both List1 and List2 ",list(common))
# for b in common:
#     if b%2 == 0:
#         lsteven.append(b)
#     else:
#         lstodd.append(b)
#
# print("Even from the common elms ", lsteven)
# print("Odd from the common elms ", lstodd)
#
# if list(common) != None:
#     avg = sum(list(common))/len(list(common))
#
# elm = [x for x in list(common) if x > m and x<avg]
# print("Elements above m and avg ",elm)

# n = int(input())
# ls = []
# for i in range(n):
#     d1 = {}
#     age = int(input("Enter age: "))
#     name = input("Enter name: ")
#
#     d1["Name"] = name
#     d1["Age"] = age
#     ls.append(d1)
#
# print("\n")
# for a in ls:
#     if a["Age"] > 25:
#         for key, value in a.items():
#             print(f"{key}: {value}")
#     print()

# n = int(input())
# lst1 = []
# for i in range(n):
#     d1 = {}
#     season = input("Enter season: ")
#     flower = input("Enter a flower name: ")
#     d1["season"] = season
#     d1["flower"] = flower
#     lst1.append(d1)
#
# search = input("Enter season to search: ")
#
# print("\n")
#
# print(f"\nFlowers for the season '{search}':")
# for a in lst1:
#     if a["season"].lower() == search.lower():
#         print(a["flower"])

# from num2words import num2words
# def num_to_string(n, limit = 10):
#     if n<= 0 :
#         return 'Enter a positive integer'
#     multiples = [n * i for i in range(1, limit + 1)]
#     words = [num2words(n)for n in multiples]
#     return words
#
# n = int(input())
# result = num_to_string(n)
# print(", ".join(result))

# class Engine:
#     def __init__(self, engineType, engineYear):
#         self.engineType = engineType
#         self.engineYear = engineYear
#     def printInfo(self):
#         print(f"Engine (type = {self.engineType}, year = {self.engineYear})")
# class Vehicles:
#     def __init__(self,brand , model, year, engine):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.engine = engine
#     def printInfo(self):
#         engine_Info = f"{self.engine.engineType} year = {self.engine.engineYear}"
#         print(f"My car is {self.brand}, model {self.model}, year {self.year}, engine {engine_Info}.")
#
# engine = Engine("Diesel", "2009")
# vehicle = Vehicles("BMW", "F60", "2010",engine)
# vehicle.printInfo()

# class Person:
#     def __init__(self, Fname, Lname, age, nation):
#         self.Fname = Fname
#         self.Lname = Lname
#         self.age = int(age)
#         self.nation = nation
#     def printPerson(self):
#         return f"My name is {self.Fname} {self.Lname}. I am {self.age} years old and i am from {self.nation}."
# class Student(Person):
#     def __init__(self, uni, yearOfStudy, grade, Fname, Lname, nation, age):
#         super().__init__(Fname, Lname, age, nation)
#         self.uni = uni
#         self.yearOfStudy = int(yearOfStudy)
#         self.grade = float(grade)
#     def ChangeUni(self):
#         newUni = input("Please enter new Uni: ")
#         self.uni = newUni
#
#     def printStudent(self):
#         return  f"{super().printPerson()} I study at {self.uni}, my grade is {self.grade}, i will graduate after {self.yearOfStudy} years."
# class Teacher(Person):
#     def __init__(self, WorkSpace, Salary, Experience, Fname, Lname, nation, age):
#         super().__init__(Fname,Lname, age, nation)
#         self.workSpace = WorkSpace
#         self.salary = float(Salary)
#         self.experience = int(Experience)
#     def ChangeWorkSpace(self):
#         newWorkSpace = input("Please enter new Work Space: ")
#         self.workSpace = newWorkSpace
#     def printTeacher(self):
#         return f"{super().printPerson()} I work at {self.workSpace}, my salary is {self.salary}, i am teaching for {self.experience} years."
# def CreateStudent():
#     Fname = input("Please enter your first name: ")
#     Lname = input("Please enter your last name: ")
#     Age = input("Please enter your age: ")
#     nation = input("Please enter your nation: ")
#     uni = input("Please enter your uni: ")
#     yearOfStudy = input("Please enter your year of study: ")
#     grade = input("Please enter your grade: ")
#     return Student(uni, yearOfStudy, grade, Fname, Lname, nation, Age)
# def CreateTeacher():
#     Fname = input("Please enter your first name: ")
#     Lname = input("Please enter your last name: ")
#     Age = input("Please enter your age: ")
#     nation = input("Please enter your nation: ")
#     WorkSPace = input("Please enter your work space: ")
#     Experience = input("Please enter your year of experience: ")
#     salary = input("Please enter your salary: ")
#     return Teacher(WorkSPace, salary, Experience, Fname, Lname, nation, Age)
# student = CreateStudent()
# print(student.printStudent())
# teacher = CreateTeacher()
# print(teacher.printTeacher())
# change_Uni = input("Do you want to change Uni:  ")
# if change_Uni.lower() == "yes":
#     student.ChangeUni()
# print(student.printStudent())
# change_WorkSpace = input("Do you want to change Work Space:  ")
# if change_WorkSpace.lower() == "yes":
#     teacher.ChangeWorkSpace()
# print(teacher.printTeacher())

choices = ["Active", "Non Active"]

class BankAcc:
    def __init__(self, ID, fName, lName, status, amount):
        self.ID = ID
        self.fName = fName
        self.lName = lName
        self.status = status
        self.amount = amount

    def changeStatus(self):
        while True:
            newStatus = input(f"Change status ({choices[0], {choices[1]}}): ").strip()
            if newStatus in choices:
                self.status = newStatus
                print("Status Updated")
                break
            else:
                print(f"Invalid Status. Choose {choices[0]} or {choices[1]}")

    def Withdraw(self,amount):
        if self.status != "Active":
            print(f"Withdraw denied. Account in non Active")
        elif amount > self.amount:
            print(f"Withdraw denied. Insuficient amount. Your ammount is {self.amount}")
        elif amount <= 0:
            print(f"No money in account")
        else:
            self.amount -= amount
            print(f"Withdraw success! New amount is {self.amount:2f} BGN")

    def printAcc(self):
        return (f"Your Bank Account is {self.ID}. \n"
                f"The name of the account is {self.fName} {self.lName}. \n"
                f"Active or not : {self.status}. \n"
                f"Ammount in {self.amount:2f} BGN \n")

def CreateBankAcc():
    ID = int(input("Enter ID: "))
    fName = input("Enter FName: ")
    lName = input("Enter LName: ")
    while True:
        status = input(f"Enter Status: {choices[0]}, {choices[1]} ").strip()
        if status in choices:
            break
        else:
            print(f"Invalid Status. Choose {choices[0]} or {choices[1]}")
    Amount = float(input("Enter Amount: "))
    return BankAcc(ID, fName, lName, status, Amount)

def createMultipleAcc():
    accounts = []
    n = int(input("Enter number of accounts: "))
    for i in range(n):
        print(f"Creating Account {i+1}")
        accounts.append(CreateBankAcc())
    return accounts

def WithdrawFromAcc(accounts):
    AccID = int(input("Enter AccID from where you want to withdraw: "))
    for acc in accounts:
        if acc.ID == AccID:
            print("Account Found!")
            ammount = float(input("Enter Amount: "))
            acc.Withdraw(ammount)
            return f"Withdrawn ammount: {ammount}"
    print(f"Account {AccID} not found.")

def ChangeStatus(accounts):
    accId = int(input("Enter AccID where you want to change status: "))
    for acc in accounts:
        if acc.ID == accId:
            print("Account Found!")
            acc.changeStatus()
            return "Status Updated"
    print("Account Not Found")

print("Welcome to Bank Account Menager")
all_accs = createMultipleAcc()

print(f"All accounts: ")
for acc in all_accs:
    print(acc.printAcc())

WithdrawFromAcc(all_accs)


ChangeStatus(all_accs)

print(f"All accounts: ")
for acc in all_accs:
    print(acc.printAcc())