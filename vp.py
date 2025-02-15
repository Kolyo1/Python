# Zad 1
# import random
# try:
#     n=int(input())
#     if 10<abs(n)<50 :
#         a = random.randint(-2500,-1300)
#         b = random.randint(1111,4444)
        
#         if a > b:
#             a,b = b,a
        
#         mylst_1 = []
#         for i in range(n):
#             while True:
#                 number = int(input(f"Въведете число: interval {a}-  {b}"))
#                 mylst_1.append(number)
#                 break
#     print(mylst_1)
#     count = 0
#     for c in mylst_1:
#         if c %4 == 0 or c%5 == 0 and c < 0: 
#             count += 1
#     print(count)
#     avg_lst = [x for x in mylst_1 if 10 < x and x < 100 and x%2 == 0]
#     if avg_lst:
#         print(f"Average {sum(avg_lst)/len(avg_lst)}")

#     mylst_2 = []
#     for m in mylst_1:
#         if 99<abs(c)<1000 and c %3 == 0:
#             mylst_2.append(c)
    
#     count2 = 0
#     for l in range(len(mylst_2)):
#         if l<0 and mylst_2[l] %2 == 0:
#             count2 += 1
#     print(count2)

#     for e in range(len(mylst_2)):
#         if e%2 == 1:
#             mylst_2[e] = 13

#     if len(mylst_1) != len(mylst_2):
#         if len(mylst_1) > len(mylst_2):
#             longer = mylst_1
#         else:
#             longer = mylst_2
#         print("Before",longer)
#         longer.pop(0)
#         longer.pop(-1)
#         print("After",longer)
#     else:
#         print("Ednakvi spisyci")
# except:
#     print("Грешка")

class Market:
    def __init__(self,barcod,name,manufacturer,price,quantity):
        self.barcod = barcod
        self.name = name
        self.manucaturer = manufacturer
        self.price = price
        self.quantity = quantity

    def sale(self,quantity):
        if quantity <= self.quantity:
            self.quantity -=quantity
        else:
            print("Not enough")
        
    def discount(self): 
        if 30<self.price<50:
            self.price *=0.95
        elif 10<self.price<30:
            self.price *= 0.93
        else:
            print("Няма отстъпка")
        
    def info(self):
        return f"Barcod {self.barcod}, Name {self.name}, Manufacturer {self.manucaturer}, Price {self.price}, Quantity {self.quantity}"

product_list = []
n = int(input())
for i in range(n):
    barcod=int(input())
    name=input()
    manufacturer=input()
    price=float(input())
    quantity=int(input())
    market = Market(barcod,name,manufacturer,price,quantity)
    product_list.append(market)

for product in product_list:
    print(market.info())

barcode = int(input())
def search_by_barcod(barcode, product_list):
    for market in product_list:
        if barcode == market.barcode:
            print(market.info)
        else:
            print("Wrong barcode I!!")
            print(product_list)

search_by_barcod(barcode,product_list)

manufactuer = input()
def search_by_manufacturer(manufacturer, product_list):
    for market in product_list:
        if manufactuer == market.manucaturer:
            new_list = [x for x in product_list if sum(market.price)/market.quantity >= market.price]
    return new_list

filtered = search_by_manufacturer(manufacturer,product_list)
if filtered:
    for items in filtered:
        print(market.info())

def sort_by_quantity(product_list):
    return sorted(product_list(key = lambda market: market.quantity,reverse = True))

new_list = sort_by_quantity(product_list)
if new_list:
    for items in new_list:
        print(market.info())

def delete_by_name(name, product_list):
    product_list[:] = [product for product in product_list if not(product == market.name and market.quantity <= 3)]
    return product_list

new_lst = delete_by_name(name, product_list)
if new_lst:
    for items in new_lst:
        print(market.info)
