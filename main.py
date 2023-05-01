from data import MENU, code_words, resources

def print_menu():
    print("***MENU***")
    for drink in MENU:
        print(f"{drink} - ${MENU[drink]['cost']:.2f}")
def check_resourses(choise):
    for item in choise["ingredients"]:
        if not resources[item] >= choise["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def coffee_machine():
    go = True
    while go:
        print_menu()
        user_drink = input("What would you like? (espresso/latte/cappuccino):").lower()
        while not user_drink in code_words:
            user_drink = input("What would you like? (espresso/latte/cappuccino):")

        if user_drink == "off":
            go = False
        elif user_drink == "report":
            print("------Report------")
            for item in resources:
                if item == "milk" or item == "water":
                    print(f"{item}: {resources[item]}ml")
                elif item == "coffee":
                    print(f"{item}: {resources[item]}g")
                else:
                    print(f"{item}: ${resources[item]:.2f}")
            print(f"------------------\n")
        else:
            choice = MENU[user_drink]
            if check_resourses(choice):
                print("Please insert coins.")
                quaters = int(input("how many quarters?: ")) * 0.25
                dimes = int(input("how many dimes?: ")) * 0.1
                nickles = int(input("how many nickles?: ")) * 0.05
                pennies = int(input("how many pennies?: ")) * 0.01
                user_paid = quaters + dimes + nickles + pennies
                user_change = (user_paid) - choice["cost"]
                if user_change < 0:
                    print("Not enough money inserted. Coins are refunded.")
                else:
                    resources["money"] += user_paid
                    resources["money"] -= user_change
                    if user_change > 0:
                        print(f"Here is ${user_change : .2f} in change.")
                    print(f"Your {user_drink} ☕️. Enjoy!")
                    for item in choice["ingredients"]:
                        resources[item] -= choice["ingredients"][item]
            else:
                go = False
                print("Out of order")

coffee_machine()


