import random
from time import sleep
from art import logo
from clear import *

def get_card():
    """It return's one random card among 14 cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list):
    """calculate the score for the taken cards"""
    if sum(list)==21 and len(list)==2:
        return 21
    elif sum(list)>21 and 11 in list:
        list.remove(11)
        list.append(1)
        return sum(list)
    else :
        return sum(list)
        
def compare(user, comp):
    """It compare's both the total and declares the Result"""
    if (user > 21) or (comp > user):
        print("\n------You loose------")
    elif (comp > 21) or (comp < user):
        print("\n------You won------")
    else:
        print("\n------Match Draw------")


def play():
    user_cards = []
    comp_cards = []

    for _ in range(2):
        user_cards.append(get_card())
        comp_cards.append(get_card())

    """User's Turn"""
    while(True):
        user_score = calculate_score(user_cards)
        print (f"\nyou cards are {user_cards} , your score is {user_score}")
        print (f"Computer's first card is {comp_cards[0]}")
        val = input("\nif you want to add one card enter 'y' otherwise enter 'n' : ")
        if val=='y' or val=='Y':
            user_cards.append(get_card())
            pass
        else:
            break

    """Computer's Turn"""
    while(True):
        comp_score = calculate_score(comp_cards)
        if comp_score < 17:
            comp_cards.append(get_card())
        else:
            break

    print(f"computer has {comp_cards},  And total score is {comp_score}")
    print(f"You have {user_cards},  And total score is {user_score}")

    compare(user_score, comp_score)
    
while(True):
    clear()
    print(logo)
    inp = input("\nIf you want to play game enter 'y' ,otherwise enter 'n' : ")
    if (inp == 'y') or (inp == 'Y'):
        play()
    else:
        break
    print("\nx-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    sleep(10)