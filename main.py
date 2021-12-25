MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


profit = 0

resources = {"water": 300, "coffee": 300,  "milk": 300}


def print_report():
    print(f"We are left with {resources['water']}ml of water, ")
    print(f"and {resources['coffee']} gms of coffee, ")
    print(f"and {resources['milk']} ml of milk.")


def check_resources(drink):
    if drink == "latte":
        if resources['water'] >= MENU['latte']['ingredients']['water']:
            if resources['milk'] >= MENU['latte']['ingredients']['milk']:
                if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                    return True
            return False
        return False
    elif drink == "espresso":
        if resources['water'] >= MENU['espresso']['ingredients']['water']:
            if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                return True
            return False
        return False

    elif drink == "cappuccino":
        if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
            if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
                if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                    return True
            return False
        return False


def deduct_resources(drink):
    if drink == "latte":
        resources['water'] -= MENU['latte']['ingredients']['water']
        resources['milk'] -= MENU['latte']['ingredients']['milk']
        resources['coffee'] -= MENU['latte']['ingredients']['coffee']
    elif drink == "espresso":
        resources['water'] -= MENU['espresso']['ingredients']['water']
        resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
    elif drink == "cappuccino":
        resources['water'] -= MENU['cappuccino']['ingredients']['water']
        resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
        resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
    return


def process_coins(drink):
    quarters = int(input("Please insert the quarters:\n"))
    dimes = int(input("Please insert the dimes:\n"))
    nickles = int(input("Please insert the nickles:\n"))
    pennies = int(input("Please insert the pennies:\n"))
    total = quarters*0.25 + dimes*0.1 + nickles * 0.05 + pennies * 0.01
    return total


def process_drink(drink):
    if check_resources(drink):
        cash = process_coins(drink)
        print(f"The total coins insert are : ${cash}")
        if cash >= MENU[drink]['cost']:
            global profit
            profit += MENU[drink]['cost']
            cash_back = round(cash - MENU[drink]['cost'], 2)
            deduct_resources(drink)
            print(f"Enjoy your {drink}!")
            if cash_back > 0:
                print(f"Here's your remaining cash {cash_back}")
        else:
            print("Sorry! That's not enough money")
            print("Here's your ${cash}.")
    else:
        print(f"Sorry, We don't have the resources to provide {drink}")


while True:
    prompt = input("What would you like to have?\n")
    if prompt not in ["report", "OFF"]:
        process_drink(prompt)
    elif prompt == "report":
        print_report()
    elif prompt == "OFF":
        break
    else:
        print("Please enter a proper drink!")

