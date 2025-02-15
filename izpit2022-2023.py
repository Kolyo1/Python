# zad 1

# list = []
# n = int(input())
# if n > 5 and n < 35:
#     for i in range(0,n+1):
#         b = int(input())
#         if b > 30 and b < 300:
#             list.append(b)
# print(list)
# count = 0
# for a in list:
#     if a%3 == 0:
#         count += 1
# print(count)

# listby4 = []

# for c in list:
#     if c %6 == 4:
#         listby4.append(c)
# print(min(listby4))

# list2 = [v for v in list if v > 9 and v < 100 and (v %2 == 0 or v%3 == 0)]
# print(list2)
# listOddInd = []
# for m in list2:
#     if m %2 != 0:
#         listOddInd.append(m)
# print(f"AVG: {sum(listOddInd)/len(listOddInd)}")

# listEven = [x for x in list2 if x%2 == 0]
# if listEven:
#     min_even = min(listEven)
#     list2.remove(min_even)
# print("New list2 ", list2)


#Zad 2

class Employee:
    def __init__(self,I_num,fname,lname,work_experience,educational_level,salary,age):
        self.I_num = I_num
        self.fname = fname
        self.lname = lname
        self.work_experince = work_experience
        self.educational_level = educational_level
        self.salary = salary
        self.age = age
    
    def display_info(self):
        print (f"ID:{self.I_num}. Name {self.fname} {self.lname}, Staj {self.work_experince}, Education {self.educational_level}, Salary {self.salary}, Age {self.age}.")    
    
    def bonus(self):
        if self.educational_level == 'Vishe':
            bonus = int(self.salary) + (self.salary* 0.05)
            self.salary = float(self.salary) + float(bonus)
            self.salary = float(self.salary+ ((self.work_experince * 0.012))) + int(self.salary)

        elif self.educational_level == 'Sredno':
            bonus = int(self.salary) + (self.salary* 0.02)
            self.salary = float(self.salary) + float(bonus)
            self.salary = float(self.salary+ ((self.work_experince * 0.012))) + int(self.salary)

        else :
            self.salary = float(self.salary+ ((self.work_experince * 0.012))) + int(self.salary)

        money = self.salary
        print(f"Salary is {money: .2f}")

empl1 = Employee(1, "Ahmed", "Dubarov", 3, "Vishe", 3000, 35)
empl2 = Employee(2, "Dragan", "Drumov", 2, "Sredno", 2500, 25)
empl3 = Employee(3, "Boiko", "Borisov", 1, "Osnovno", 2000, 20)

empl1.display_info()
empl2.display_info()
empl3.display_info()

empl1.bonus()
empl2.bonus()
empl3.bonus()