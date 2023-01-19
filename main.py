from Menu import MENU, resources


# TODO 1. Print report.
# TODO 2. Check resources sufficient.
# TODO 3. Process coins.
# TODO 4. Check transaction successful.
# TODO 5. Make Coffee.


def check_resources(drink):
    for item in resources:
        if resources[item] < drink['ingredients'][item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


def pay():
    global profit
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = int(quarters + dimes + nickles + pennies)

    if total >= drink['cost']:
        change = round(total - drink['cost'], 2)
        profit += drink['cost']
        for item in resources:
            resources[item] -= drink['ingredients'][item]
            print(f"Here is ${change} in change.")
        return True
    else:
        return False


is_on = True
profit = 0
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} mL")
        print(f"Milk: {resources['milk']} mL")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink) is True:
            if pay() is True:
                print(f"Here is your {choice} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
