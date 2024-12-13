n = int(input("Enter full number: "))
list_1 = []
list_3delitel = []
list_Negative1 = []
list_Positive1 = []
list_7delitel = []
list_Negative2 = []
new_list = []
while True:
    if n >= 3 and n <= 5:
        for i in range(0,n):
            b = int(input())
            if b > -100 and b < 100:
                list_1.append(b)
            else:
                print("Invalid input")
        for a in list_1:
            if a%3 == 0 and a%2 == 0:
                list_3delitel.append(a)
            if a < 0:
                list_Negative1.append(a)
            else:
                list_Positive1.append(a)
        if list_Negative1 != []:
            average = sum(list_Negative1) / len(list_Negative1)
            print(f"Average of negative {average:.2f}")
            print(f"Maximun number negative {max(list_Negative1):.2f}")
        print(f"Minimum number positive {min(list_Positive1):.2f}")
        for c in list_1:
            if c%7 == 0 and c%2 != 0 and c > 0:
                list_7delitel.append(c)
            elif c < 0 :
                list_Negative2.append(c)
        print(f"Multiplication : {max(list_7delitel)*min(list_7delitel):.2f}")
        print(f"Number of negatives: {len(list_Negative2)}")
        print(f"Length of first list: {len(list_3delitel)}")
        print(f"Length of second list: {len(list_7delitel)}")
        while len(list_3delitel) != len(list_7delitel):
            if len(list_3delitel) > len(list_7delitel):
                new_list = list_3delitel
                for delNum in range(len(list_7delitel), len(list_3delitel)):
                    new_list.pop(delNum-1)
                    if len(new_list) == len(list_7delitel):
                        break
            elif len(list_3delitel) < len(list_7delitel):
                new_list = list_7delitel
                for delNum in range(len(list_3delitel), len(list_7delitel)):
                    new_list.pop(delNum-1)
                    if len(new_list) == len(list_3delitel):
                        break
        print(f"First length: {len(list_3delitel)}")
        print(f"Second length: {len(list_7delitel)}")
        break
    else:
        print("Invalid input")
    continue