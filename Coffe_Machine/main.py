MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def insert_coins(type_of_coffee, cost_of_coffee):

    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    if total > cost_of_coffee:
        change = round(total - cost_of_coffee, 2)
        resources['money'] += cost_of_coffee
        print(f"Here is ${change} in change.")
        print(f"Here is your {type_of_coffee} ☕️. Enjoy!")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False 


def check_resources(type_of_coffee):
    water = MENU[type_of_coffee]['ingredients']['water']
    milk = MENU[type_of_coffee]['ingredients']['milk']
    coffee = MENU[type_of_coffee]['ingredients']['coffee']
    cost = MENU[type_of_coffee]['cost']

    water_resources = resources['water']
    milk_resources = resources['milk']
    coffee_resources = resources['coffee']

    water_sufficient = False
    milk_sufficient = False
    coffee_sufficient = False

    if water_resources - water >= 0:
        water_sufficient = True
    if milk_resources - milk >= 0:
        milk_sufficient = True
    if coffee_resources - coffee >= 0:
        coffee_sufficient = True

    if water_sufficient and milk_sufficient and coffee_sufficient:

        payment = insert_coins(type_of_coffee, cost)

        if payment:
            resources['water'] = water_resources - water
            resources['milk'] = milk_resources - milk
            resources['coffee'] = coffee_resources - coffee

    else:
        if not water_sufficient:
            print("Sorry there is not enough water.")
        elif not milk_sufficient:
            print("Sorry there is not enough milk.")
        elif not coffee_sufficient:
            print("Sorry there is not enough coffee.")


def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


answer = ''
while answer != 'off':
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if 'report' in answer:
        report()
    elif 'espresso' in answer or 'latte' in answer or 'cappuccino' in answer:
        check_resources(answer)
