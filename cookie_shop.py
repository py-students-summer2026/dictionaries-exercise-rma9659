"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""
import csv

def bake_cookies(filepath):
    cookies = []
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cookie = {
                'id': int(row['id']),
                'title': row['title'],
                'description': row['description'],
                'price': float (row['price'].replace('$', ''))
            }
            cookies.append(cookie)
    return cookies


def welcome():
    print("Welcome to the Python Cookie Shop!")
    print("We feed each according to their need.")
   


def display_cookies(cookies):
    print("\nHere are the cookies we have in the shop for you:\n")

    for cookie in cookies:
        print(f"  #{cookie['id']} - {cookie['title']}")
        print(f"  {cookie['description']}")
        print(f"  Price: ${cookie['price']:.2f}\n")
    


def get_cookie_from_dict(id, cookies):
    for cookie in cookies:
        if cookie['id'] == id:
            return cookie


def solicit_quantity(id, cookies):
    cookie = get_cookie_from_dict(id, cookies)

    while True:
        quantity = input(f"How many {cookie['title']} would you like? ")

        if quantity.isdigit():
            quantity = int(quantity)
            subtotal = quantity * cookie['price']
            print(f"Your subtotal for {quantity} {cookie['title']} is ${subtotal:.2f}.")
            return quantity
        
        print("Please enter a valid integer quantity.")


def solicit_order(cookies):
    order = []

    valid_ids = [cookie['id'] for cookie in cookies]

    while True:
        response = input("\nPlease enter the numbeer of any cookie you would like to purchase: ").strip().lower()

        if response in ['finished', 'done', 'quit', 'exit']:
            break

        if not response.isdigit():
            print("Please enter a valid cookie number.")
            continue

        cookie_id = int(response)

        if cookie_id not in valid_ids:
            print("That cookie does not exist.")
            continue

        quantity = solicit_quantity(cookie_id, cookies)

        order.append({'id': cookie_id, 'quantity': quantity})


    return order





def display_order_total(order, cookies):
    total = 0
    print("\nThank you for your order. You have ordered:\n")

    for item in order:
        cookie = get_cookie_from_dict(item['id'], cookies)
        print(f"-{item['quantity']} {cookie['title']}")
        total += item['quantity'] * cookie['price']

    print(f"\nYour total is ${total:.2f}.")
    print("Please pay with Bitcoin before picking-up.\n")
    print("Thank you!")
    print("-The Python Cookie Shop Robot.")

    


def run_shop(cookies):
    welcome()
    display_cookies(cookies)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
