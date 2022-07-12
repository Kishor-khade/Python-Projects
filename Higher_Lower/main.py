import random
from art import logo, symbol
from time import sleep
from data import *
from clear import *

def get_number():
    return random.randint(0,21)

def get_data(number):
    return data[number]

def play():
    val1 = get_data(get_number())
    total = 0
    is_correct = True
    while (is_correct == True):
        clear()
        val2 = get_data(get_number())
        print(logo)
        print(f" Score : {total} ")
        print(f"Compare A : {val1['name']} , {val1['description']} from {val1['country']}")
        print(symbol)
        print(f"Compare B : {val2['name']} , {val2['description']} from {val2['country']}")
        ans = input("Compare who has more followers A or B :   ")
        if (ans == 'A') and (val1['followers'] >= val2['followers']):
            total += 1
        elif (ans == 'B') and (val1['followers'] <= val2['followers']):
            total += 1
        else:
            is_correct = False
            break
        val1 = val2
    print(f"Sorry, that's wrong . final score : {total}")


while(True):
    clear()
    print(logo)
    val = input("If you want to play game enter 'Y', else enter 'N'  :  ")
    if (val == 'Y') or (val == 'y'):
        play()
        sleep(10)
    else:
        break