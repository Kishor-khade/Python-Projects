# 
import random


def get_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def print_fun(comp, user):
    print("\ncomputer has ", comp)
    print("you have ",user)
    return

def check(card):
    if card >21:
        return 0
    elif card == 21:
        return 1
    else :
        return 2

def play(user, comp):
    while (True):
        score = check(user)
        if score == 0:
            print_fun(comp, user)
            print("you got more than 21 \n ------You loose------")
            return
        if score == 1:
            print_fun(comp, user)
            print("you got 21 \n ------You Won------")
            return
        print("you have ", user)
        choice = input(" If you want to take another one card enter 'y' otherwise enter 'n'")
        if choice == 'y' or choice == 'Y':
            user += get_card()
        else:
            break
    
    while (True):
        if check(comp) == 0:
            print_fun(comp, user)
            print ("computer score is more than 21 \n ------You Won------")
            return
        if comp < 17: comp += get_card()
        else : 
            print_fun(comp, user)
            if comp <= user:print("\n ------Computer loose------")
            else: print("------Computer Won------")
            return

def start():
    #1st round
    user, comp = 0,0
    comp += get_card()
    user += get_card()
    show = comp

    #2nd round
    user += get_card()
    comp += get_card()
    print_fun(show, user)
    play(user, comp)

while(True):
    inp = input("\nIf you want to play game enter 'y' ,otherwise enter 'n' : ")
    if inp == 'y' or inp == 'Y':
        start()
        print("yes")
    else:
        print("No")
        break