class ClothesShop:
    def __init__(self, Id, type, brand, price, quantity):
        self.Id = Id
        self.type = type
        self.brand = brand
        self.price = price
        self.quantity = quantity

    def ClotheInfo(self):
        return f"ClotheId {self.Id}. Type {self.type}. Brand {self.brand}. Price {self.price} lv. Quantity {self.quantity}."

    def ChangePrice(self, newPrice):
        self.price = newPrice

    def ChangeQuantity(self,newQuantity):
        self.quantity = newQuantity
clothes1 = ClothesShop(1,"T-Shirt","Gucci",2000, 15)
clothes2 = ClothesShop(2,"Jeans","Versace",2500,20)
clothes3 = ClothesShop(3,"Jacket","Nort Face",1500,30)

clothesList = [clothes1, clothes2, clothes3]
Id = int(input("Vyvedete tyrsenoto ID"))
def SearchById(clothesList,Id):
    for clothes in clothesList:
        if Id == clothes.Id:
            print(clothes.ClotheInfo())
            return
        print("No Product with that Id")
SearchById(clothesList,Id)

brand = input()
def SearchByBrand(brand,clothesList):
    for clothes in clothesList:
        if brand == clothes.brand:
            print(clothes.ClotheInfo())
            return
        print("No Product with that Brand")
SearchByBrand(brand,clothesList)

quantity = int(input())
def SellClotheById(Id, quantity,clothesList):
    for clothes in clothesList:
        if Id == clothes.Id:
            if quantity <= clothes.quantity:
                clothes.quantity = clothes.quantity - quantity
                print("Uspeshna Prodajba")
                return
            print("Not enough quantity")

            return
        print("No Product with that Id")
SellClotheById(Id, quantity,clothesList)