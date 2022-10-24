from os import system

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

resources = {"water": 300,
             "milk": 200,
             "coffee": 100,
             }

w = resources['water']
m = resources['milk']
c = resources['coffee']

# coins


mn = 0
ts = False

power = "on"

while power == "on":
    system('cls')
    x = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    # Transaction

    def user_money():
        usr_mny = int(input("Please Enter Coins : "))
        return usr_mny

    if x == "espresso":
        print("espresso")
        if w >= 50 and c >= 18:
            cost = MENU["espresso"]['cost']
            print(cost)

            um = user_money()
            print(um)

            if um == cost:
                print(f"Transaction Successful")
                ts = True
                mn += cost
                w -= 50
                c -= 18
            elif um > cost:
                change = um - cost
                print(
                    f"Transaction Successful\nHere is your Change : {change}")
                ts = True
                mn += cost
                w -= 50
                c -= 18
            else:
                print("Insuficient Money")
        else:
            print("Insufficient Resources")
    elif x == "latte":
        print("latte")
        if w >= 200 and m >= 150 and c >= 24:
            print("can")
            cost = MENU["latte"]['cost']
            print(cost)

            um = user_money()
            print(um)

            if um == cost:
                print("Valid")
                ts = True
                mn += cost
                w -= 200
                c -= 150
                m -= 24
            elif um > cost:
                change = um - cost
                print(
                    f"Transaction Successful\nHere is your Change : {change}")
                ts = True
                mn += cost
                w -= 200
                c -= 150
                m -= 24
            else:
                print("Insuficient Money")
        else:
            print("Insufficient Resources")

    elif x == "cappuccino":
        print("cappuccino")
        if w >= 250 and m >= 100 and c >= 24:
            print("can")
            cost = MENU["cappuccino"]['cost']
            print(cost)

            um = user_money()
            print(um)

            if um == cost:
                print("Valid")
                ts = True
                mn += cost
                w -= 250
                c -= 100
                m -= 24

            elif um > cost:
                change = um - cost
                print(
                    f"Transaction Successful\nHere is your Change : {change}")
                ts = True
                mn += cost
                w -= 250
                c -= 100
                m -= 24

            else:
                print("Insuficient Money")
        else:
            print("Insufficient Resources")

    elif x == "report":
        print("Your report")
        print(f"Water : {w}")
        print(f"Milk : {m}")
        print(f"Coffee : {c}")
        print(f"Collected money : ${mn}")
    else:
        print("Wrong Input !")

    if w <= 0:
        w = 0
    if m <= 0:
        m = 0
    if c <= 0:
        c = 0

    power = input(
        "Press button to Toggle Machine !(Enter on / off) : ").lower()
