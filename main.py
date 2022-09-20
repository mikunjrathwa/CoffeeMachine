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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def are_resources_sufficient(selected_drink):
    global resources
    needed_resources = selected_drink["ingredients"]
    for item in needed_resources:
        if needed_resources[item] > resources[item]:
            print(f"Sorry there is no enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated dollar value from inserted coins."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received == drink_cost:
        profit += drink_cost
        return True
    elif money_received > drink_cost:
        change_amount = round(money_received - drink_cost, 2)
        print(f"Here is ${change_amount} dollars in change.")
        profit += drink_cost
        return True
    else:
        print(f"Not enough money.")
        return False


def make_coffee(selected_drink):
    global resources
    needed_resources = selected_drink["ingredients"]
    for item in needed_resources:
        resources[item] -= needed_resources[item]
    print(f"Enjoy your {selected_drink}")


def add_resources():
    resources["water"] = int(input("Water: "))
    resources["coffee"] = int(input("Coffee: "))
    resources["milk"] = int(input("Milk: "))


is_on = True
profit = 0


while is_on:
    choice = input("What would you like? 😒 (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if are_resources_sufficient(drink):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink)



