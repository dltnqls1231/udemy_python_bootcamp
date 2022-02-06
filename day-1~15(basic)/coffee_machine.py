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


def resources_sufficient(w, m, c, coffee_name):
    need_water = MENU[coffee_name]["ingredients"]["water"]
    need_coffee = MENU[coffee_name]["ingredients"]["coffee"]
    if coffee_name == "espresso":
        need_milk = 0
    else:
        need_milk = MENU[coffee_name]["ingredients"]["milk"]

    ## 아래의 if문 여러개를 for item in dictionay: 형태로 바꾸어서 쓰면 간단한 코드로 하나씩 비교가능!
    if w <= need_water:
        print("Sorry there is not enough water")
        need_water = False
    if m <= need_milk:
        print("Sorry there is not enough milk")
        need_milk = False
    if c <= need_coffee:
        print("Sorry there is not enough coffee")
        need_coffee = False
    return need_water, need_milk, need_coffee


def coin_sufficient(coffee_menu):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*0.25 + dimes*0.1 + nickels*0.05 + pennies*0.01
    if MENU[coffee_menu]["cost"] <= total:
        change = total - MENU[coffee_menu]["cost"]
        print(f"Here is ${change:.2f} in change.")
        print(f"Here is your {coffee_menu} Enjoy!")
        return MENU[coffee_menu]["cost"]
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = 0
    while True:
        coffee_name = input("What would you like? (espresso/latte/cappuccino)")
        if coffee_name == "off":
            break
        elif coffee_name == "report":
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${money}")
        else:
            water_t, milk_t, coffee_t = resources_sufficient(water, milk, coffee, coffee_name)
            if water_t and milk_t >= 0 and coffee_t:
                water -= water_t
                milk -= milk_t
                coffee -= coffee_t
                coin_t = coin_sufficient(coffee_name)
                if coin_t:
                    money += coin_t
                else:
                    continue
            else:
                continue


make_coffee()