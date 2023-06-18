from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money = MoneyMachine()

while(True):
    makeCoffee = CoffeeMaker()
    choice = input("Select an item from menu: " + menu.get_items() + ",'report' to report or 'exit' "
                                                                     "to turn off the machine: \n")
    if(choice == 'report'):

        makeCoffee.report()
        money.report()

    elif choice == 'exit':
        break

    else:
        itemToBeMade = menu.find_drink(choice)
        if makeCoffee.is_resource_sufficient(itemToBeMade):
            if money.make_payment(itemToBeMade.cost):
                makeCoffee.make_coffee(itemToBeMade)
                makeCoffee.report()
            continue
        continue
        print("Insuficient Money")

