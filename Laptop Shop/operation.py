from write import laptop_table, shop_name, order_billing, buy_billing
from read import file_read
import datetime
def shipping(actual_price):
    while True:
        ship = input("Do you want your laptop to be shipped? (Y/N):").lower()
        if ship == 'y':
            shipping_price = 5
            with_shipping = actual_price + shipping_price
            return [shipping_price, str(with_shipping), ship]
        elif ship == 'n':
            return [0, str(actual_price), ship]
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
def price_with_vat(actual_price):
    vat = 0.13
    price_vat = float(actual_price)+float(actual_price) * float(vat)
    float(price_vat)
    return [vat, price_vat]

def buy():
    try:
        customer_name = input("Enter your name: ")
        customer_phone = input("Enter your phone number: ")
        customer_address = input("Enter your address: ")
        actual_price = 0
        laptop_brand = ""
        while True:
            try:
                key_id = int(input("Enter the laptop ID: "))
                break
            except ValueError:
                print("Invalid ID. Please enter an integer value")
                my_dictionary = file_read()
                if key_id not in my_dictionary.keys():
                    print("Laptop ID not found. Please enter a valid ID")
                    return buy()
                laptop_name = my_dictionary[key_id][0]
                laptop_cost = my_dictionary[key_id][5].replace('$', '').strip()
                laptop_quantity = int(my_dictionary[key_id][6])
                print(f"Laptop quantity available: {laptop_quantity}")
                while True:
                    try:
                        product_quantity = int(input("Enter the quantity you want to buy: "))
                        if product_quantity > laptop_quantity:
                            print("Insufficient quantity. Please enter a lower quantity.")
                        else:
                            break
                    except ValueError:
                        print("Invalid quantity. Please enter an integer value")
                        while True:
                            answer = input("Are you sure you want to Buy this laptop? (Y/N)").lower()
                            if answer != 'y' and answer != 'n':
                                print("Invalid input. Please enter the value 'Y' or 'N'")
                            else:
                                if answer == 'y':
                                    actual_price = int(laptop_cost) * product_quantity
                                    my_dictionary[key_id][6] = str(laptop_quantity - product_quantity)
                                    with open("laptop.txt", "w") as file:
                                        for index, values in my_dictionary.items():
                                            file.write(','.join(values) + '\n')
                                    laptop_brand = my_dictionary[key_id][1]
                                    break
                                elif answer == 'n':
                                    return menu()
                        return [customer_name, customer_phone, laptop_name, actual_price, customer_address, laptop_brand]
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    
def order_laptop():
    try:
        customer_name = input("Enter your name: ")
        customer_phone = input("Enter your phone: ")
        customer_address = input("Enter your address: ")
        my_dictionary = file_read()
        actual_price = 0 # Initialize actual_price with a default value
        while True:
            try:
                key_id = int(input("Enter the laptop ID: "))
                break
            except ValueError:
                print("Invalid ID. Please enter an integer value")
        if key_id not in my_dictionary.keys():
            print("Laptop ID not found. Please enter a valid ID")
            return order_laptop()
        laptop_name = my_dictionary[key_id][0]
        laptop_brand = my_dictionary[key_id][1]
        laptop_cost = my_dictionary[key_id][5].replace('$', '').strip()
        while True:
            try:
                product_quantity = int(input("Enter the quantity you want to order: "))
                break
            except ValueError:
                print("Invalid quantity. Quantity should be a number")
                answer = input("Are you sure you want to order this laptop? (Y/N)").lower()
            while True:
                try:
                    if answer == 'y':
                        actual_price = int(laptop_cost) * product_quantity
                        my_dictionary[key_id][6] = str(int(my_dictionary[key_id][6]) +
                        product_quantity)
                        with open("laptop.txt", "w") as file:
                            for index, values in my_dictionary.items():
                                file.write(','.join(values) + '\n')
                        break
                    elif answer == 'n':
                        return menu()
                    else:
                        print("Invalid input")
                        break
                except Exception as e:
                    print(f"Error occurred: {e}")
                    return
        return [laptop_name, laptop_brand, actual_price, customer_address, customer_name, customer_phone]
    except Exception as e:
        print(f"Error occurred: {e}")
    return

def menu():
    while True:
        print("--------------------------------------------------------------------------------------------------------------------")
        print("Press 1 to buy from the shop")
        print("Press 2 to order the laptop")
        print("Press 3 to exit from the shop")
        try:
            system_option = input("Please enter your choice: ")
            if system_option == '1':
                print("Welcome to the buy menu")
                while True:
                    details = buy()
                    customer_name = details[0]
                    customer_phone = details[1]
                    customer_address = details[4]
                    laptop_name = details[2]
                    actual_price = details[3]
                    laptop_brand = details[5]
                    shipping_money = shipping(actual_price)
                    ship = shipping_money[2]
                    with_shipping = shipping_money[1]
                    shipping_price = shipping_money[0]
                    buy_billing(datetime, customer_name, customer_phone,
                    customer_address, laptop_name, laptop_brand,
                    actual_price, ship, with_shipping)
                    choice = input("Do you want to buy another laptop? (Y/N)")
                    if choice.upper() != 'N':
                        break
            elif system_option == '2':
                print("Welcome to the laptop ordering menu")
                details_order = order_laptop()
                laptop_name_order = details_order[0]
                laptop_brand_order = details_order[1]
                actual_price_order = details_order[2]
                customer_address_order = details_order[3]
                customer_name_order = details_order[4]
                customer_phone_order = details_order[5]
                vat_money = price_with_vat(actual_price_order)
                vat = vat_money[0]
                price_vat = vat_money[1]
                order_billing(customer_name_order, datetime, customer_phone_order, customer_address_order, laptop_name_order, laptop_brand_order, actual_price_order, price_vat)
                break
            elif system_option == '3':
                print("Thank you. Please visit again")
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Please enter the given option only")
