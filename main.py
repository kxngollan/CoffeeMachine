from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

ordering = True

while ordering:
    # To show drinks available
    items = menu.get_items()

    ordered_drink = input(f"What drink would you like to order? {items} \n").lower()
    if ordered_drink == "report":
        coffee_maker.report()
        money.report()
    elif ordered_drink == "off":
        ordering = False
    else:
        drink = menu.find_drink(ordered_drink)
        if drink is None:
            continue
        elif coffee_maker.is_resource_sufficient(drink):
            cost = drink.cost
            if money.make_payment(cost):
                coffee_maker.make_coffee(drink)