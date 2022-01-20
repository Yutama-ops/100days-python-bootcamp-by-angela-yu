import menu
total_money = 0

# print(menu.MENU["espresso"]["ingredients"])
def ingredients_count(coffi, t_money):
    for x in menu.MENU[coffee]["ingredients"]:

        if menu.resources[x] < menu.MENU[coffi]["ingredients"][x]:
            return print(f"Sorry there is not enough {x}")
        else:
            menu.resources[x] -= menu.MENU[coffee]["ingredients"][x]
    money = coin_count(coffi)
    if money == 0:
        return print("Sorry that's not enough money, Money refunded")
    else:
        print(f"Here is ${money} in change")
        t_money += money



def coin_count(coff):
    """counting coin"""
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total < menu.MENU[coff]["cost"]:
        return 0
    else:
        total -= menu.MENU[coff]["cost"]
        return total
program = True
while program:
    coffee = input("What would you like? (espresso, latte, capuccino): ")
    if coffee != "report":
        ingredients_count(coffee, total_money)
    else:
        print(menu.resources)
    program = input("Do you still want to buy a coffee:'y' or 'no' ")
