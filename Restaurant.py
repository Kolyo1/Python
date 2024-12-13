class Restaurant:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.menu = {}

    def get_order_data(self):
        number_of_table = input("Enter table number: ")
        ordered_dishes = input("Enter ordered dishes(divided by ,): ").split(', ')
        return number_of_table, ordered_dishes

    def calculate_order_value(self, order):
        order_value = 0
        for dish_name in order:
            for dish in self.menu:
                if dish_name == dish:
                    order_value += self.menu[dish]
        return order_value

    def generate_receipt(self,order):
        print("\n ------Receipt------")
        print(f"Restaurant Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Table Number: {order[0]}")
        print("Ordered items: ")
        total = 0
        for dish_name in order[1]:
                if dish_name in self.menu:
                    price = self.menu[dish_name]
                    print(f"- {dish_name}: {price:.2f} lv")
                    total += price
        print(f"Total: {total:.2f} lv")
        print(" ---- Thank you for coming! ---- \n")

restaurant_name = input("Enter restaurant name: ")
restaurant_address = input("Enter restaurant address: ")
restaurant = Restaurant(restaurant_name, restaurant_address)

print("\n Enter menu: ")
while True:
    dish_name = input("Enter dish name(END with end): ")
    if dish_name.lower() == "end":
        break
    dish_price = float(input(f"Enter dish price for {dish_name}: "))
    restaurant.menu[dish_name] = dish_price

order = restaurant.get_order_data()
restaurant.generate_receipt(order)