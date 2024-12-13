import re
import struct

def IceCreamAvailability(iceCreamList, char):
    total_price = 0
    found = False
    for iceCream in iceCreamList:
        product_name = iceCream.get("Product Name", "")
        price_per_kg = iceCream.get("Price KG", None)
        weight = iceCream.get("Weight", None)

        if product_name and product_name[0].lower() == char.lower() and price_per_kg and weight:
            total_price += float(price_per_kg) * int(weight) / 1000
            found = True

    return total_price if found else 0

def validate_Id():
    while True:
        id = input("\nEnter ID in Format A2: ")
        if re.match(r'^[A-Z]\d+$', id):
            return id
        else:
            print(
                "Invalid ID format. Please enter an ID in the format 'A2', where 'A' is a letter and '2' is a number.")

def validate_product_name():
    while True:
        product_name = input("\nEnter product name: ")[:20]
        if product_name.strip() != "":
            return product_name
        else:
            print("Product name cannot be empty. Please enter a valid product name.")

def validate_weight():
    while True:
        weight = input("\nEnter product weight: ")
        if weight.isdigit() and int(weight) >= 0:
            return weight
        else:
            print("Invalid weight. Please enter a valid non-negative weight.")

def validate_price_kg():
    while True:
        price_KG = input("\nEnter price per KG: ")
        try:
            price = float(price_KG)
            if price >= 0:
                return f"{price:.2f}"
            else:
                print("Price per KG must be a non-negative number.")
        except ValueError:
            print("Invalid price. Please enter a valid number for price per KG.")

def write_to_bin_file(iceCreamList):
    try:
        with open('icecream.bin', 'wb') as file:
            for ice_cream in iceCreamList:
                # Get ice cream details
                unique_code = ice_cream["ID"]
                product_name = ice_cream["Product Name"]
                weight = int(ice_cream["Weight"])  # Convert to integer
                price = float(ice_cream["Price KG"])  # Convert to float

                # Encode the unique code (1 letter + 1 digit)
                code_data = unique_code.encode('utf-8')  # Should be 3 bytes

                # Encode the product name and get its length
                name_length = len(product_name)
                product_name_data = product_name.encode('utf-8')

                # Write the unique code (3 bytes)
                file.write(code_data)

                # Write product name length (1 byte)
                file.write(struct.pack('B', name_length))  # 1 byte for length

                # Write product name
                file.write(product_name_data)

                # Write weight (4 bytes integer)
                file.write(struct.pack('I', weight))

                # Write price per KG (4 bytes float)
                file.write(struct.pack('f', price))

        print("Binary file 'icecream.bin' has been created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_ice_cream_info(unique_code):
    try:
        with open('icecream.bin', 'rb') as file:
            while True:
                code_data = file.read(3)
                if not code_data:
                    break
                unique_code_in_file = code_data.decode('utf-8')

                name_length_data = file.read(1)
                if not name_length_data:
                    break
                name_length = struct.unpack('B', name_length_data)[0]


                product_name_data = file.read(name_length)
                product_name = product_name_data.decode('utf-8')

                weight_data = file.read(4)
                weight = struct.unpack('I', weight_data)[0]

                price_data = file.read(4)
                price = struct.unpack('f', price_data)[0]

                if unique_code_in_file == unique_code:
                    print(f"Unique Code: {unique_code_in_file}")
                    print(f"Product Name: {product_name}")
                    print(f"Weight: {weight} grams")
                    print(f"Price per KG: {price:.2f}")
                    return
            print(f"No ice cream found with code {unique_code}.")
    except FileNotFoundError:
        print("Error: icecream.bin file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

n= int(input("Enter a number between 5 and 15 : "))
while True:
    if n > 1 and n <15:
        iceCreamList = []
        for i in range(n):
            iceCream = {}

            iceCream["ID"] = validate_Id()
            iceCream["Product Name"] = validate_product_name()
            iceCream["Weight"] = validate_weight()
            iceCream["Price KG"] = validate_price_kg()

            iceCreamList.append(iceCream)

        print("\nIce Cream Details:")
        for iceCream in iceCreamList:
            for key, value in iceCream.items():
                print(f"{key}: {value}")
            print()

        char = input("Enter the starting character for ice cream names: ")
        total_price = IceCreamAvailability(iceCreamList, char)

        if total_price == 0:
            print(f"No ice creams found starting with '{char}'. Total price is 0.")
        else:
            print(f"Total price of ice creams starting with '{char}': {total_price:.2f}\n")

        unique_code = input("Enter the unique code to search for (Format A2): \n")
        get_ice_cream_info(unique_code)

        write_to_bin_file(iceCreamList)

        break
    else:
        print("Invalid number of ice creams. Please enter a value between 2 and 14.")
        n = int(input("Enter the number of ice creams (between 2 and 14): "))

        continue
with open("info.txt", "w") as file:
    for iceCream in iceCreamList:
        for key, value in iceCream.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")
print("Ice Cream has been saved in info.txt:")