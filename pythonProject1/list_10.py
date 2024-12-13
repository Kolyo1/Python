n = 10
list_10 = []
for i in range(0,n+1):
    b = float(input())
    if b > 0 and b%1 == 0:
        list_10.append(int(b))
print(list_10)
odd_list = []
for a in list_10:
    if a % 2 == 1:
        odd_list.append(a)
print("Odd list",len(odd_list))
print(f"Average {sum(list_10) / len(list_10) : .2f}")
list_5 = []
for m in range(0, len(list_10)):
    if list_10[m] % 2 == 0:
            list_5.append(list_10[m])
list_5 = sorted(list_5,reverse=True)[:5]
list_55 = []
print(f"List 5{list_5}")
c = 0
for c in range(0, len(list_5)):
    if c%2:
        list_55.append(list_5[c])
print(f"New list {list_55}")