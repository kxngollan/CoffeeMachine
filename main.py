from replit import clear

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

clear()

money = 0



def revenue(pennies, nickles, dimes, quarters):
  return (pennies * 0.01) + (nickles * 0.05) + (dimes * 0.1) + (quarters * 0.25)

def check_resources(drink): 
  for item in drink["ingredients"]:
    if drink["ingredients"][item] > resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

def changeAmount(amountSpent, drink):
  if amountSpent > MENU[drink]["cost"]:
    change = amountSpent - MENU[drink]["cost"]
    print(f"Here is ${change} in change.")
    return change
  elif amountSpent == MENU[drink]["cost"]:
    print("There is no change")
    return 0
  else:
    print("Sorry that was not enough money. Money refunded.")

def makeDrink(drink):
  for item in drink["ingredients"]:
    resources[item] -= drink["ingredients"][item]
  print("Here is your drink. Enjoy!")

ordering = True

while ordering:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "report":
      print(f"Water: {resources['water']}ml")
      print(f"Milk: {resources['milk']}ml")
      print(f"Coffee: {resources['coffee']}g")
      print(f"Money: ${money}")
    elif drink in MENU:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        
        amountSpent = revenue(pennies, nickles, dimes, quarters)
        change = changeAmount(amountSpent, drink)
        if change >= 0:
            enoughResources = check_resources(MENU[drink])
            money += MENU[drink]["cost"]
            if enoughResources:
                makeDrink(MENU[drink])
    elif drink == "off":
       ordering = False
    else:
      print("This isn't a valid selection")