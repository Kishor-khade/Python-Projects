from time import sleep
from art import logo

water = 500
coffee = 150
milk = 250
cost = 0


def deduct_quantity(dict):
    """Deduct the required quantity from the available resources"""
    global water; global coffee; global milk; global cost
    water -= dict['water']
    coffee -= dict['coffee']
    milk -= dict['milk']
    cost += dict['cost']
    return None


def process_coins(coins, coffee_type):
    """ Collects coins from the user And verifies that is that enough for choosen coffee type"""
    print("please! Insert coins ")
    one_ruppee  = int(input(" How many 1.Rs coins  : "))
    two_ruppee  = int(input(" How many 2.Rs coins  : "))
    five_ruppee = int(input(" How many 5.Rs coins  : "))
    ten_ruppee  = int(input(" How many 10.Rs coins : "))
    total = one_ruppee + two_ruppee*2 + five_ruppee*5 + ten_ruppee*10
    if total > coins:
        return f"Here is your {total - coins} in change. Please collect it. \n Here is your {coffee_type}  \u2615  Enjoy!"
    elif total == coins:
        return f"Here is your {coffee_type}  \u2615  Enjoy"
    else:
        return f"Sorry that's not enough money. Money refunded collect it"
    

def check_resource(dict):
    """ function that check's is there's enough resource to make a coffee or not"""
    if (water - dict['water'] < 0) or (coffee - dict['coffee'] < 0) or (milk - dict['milk'] < 0):
        return False
    else :
        return True


def Espresso():
    """Process the Espresso Coffee"""
    dict ={
        'water' : 50,
        'coffee':18,
        'milk':0,
        'cost' : 10,
    }
    if check_resource(dict):
        print(process_coins(dict['cost'], 'Espresso'))
        deduct_quantity(dict)
    else:
        print("Sorry! Resource not available ")
    return None


def Latte():
    """ Process the Latte Coffee """
    dict ={
        'water'  : 50,
        'coffee' : 18,
        'milk'   : 20,
        'cost'   : 20,
    }
    if check_resource(dict):
        print(process_coins(dict['cost'], 'Latte'))
        deduct_quantity(dict)
    else:
        print("Sorry! Resource not available ")
    return None


def Cappuccino():
    """ Process the Cappuccino coffee """
    dict ={
        'water'  : 50,
        'coffee' : 18,
        'milk'   : 25,
        'cost'   : 25,
    }
    if check_resource(dict):
        print(process_coins(dict['cost'], 'Cappuccino'))
        deduct_quantity(dict)
    else:
        print("Sorry! Resource not available ")
    return None


def report():
    """ Print the report of available resources """
    print(f"    Available water  : {water}ml")
    print(f"    Available coffee : {coffee}g")
    print(f"    Available Milk   : {milk}ml")
    print(f"    Available Cost   : {cost}.rs")
    return None
    

print(logo)
while(True):
    val = input("\nwhat would you like? (espresso/latte/cappuccino) : ")
    val = val.lower()
    if val == 'off':
        print("Shutting down Machine ...")
        sleep(5)
        break
    elif val == 'espresso':
        Espresso()
    elif val == 'latte':
        Latte()
    elif val == 'cappuccino':
        Cappuccino()
    elif val == 'report':
        report()
    else:
        print("----Please Enter correctly---")
    sleep(5)