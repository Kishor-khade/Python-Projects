import random
from time import sleep
from art import logo
from clear import * 

def get_number():
    """It returns a random number between 1 to 100"""
    return random.randrange(1,100)

def find(number):
    """Check weather the given number is lesser or greater or equals to the guess or not """
    user_input = int(input("    Make a guess  :  "))
    if user_input == number:
        return 1
    elif user_input > number:
        print("\tguessed value is large")
        return 0
    elif user_input < number:
        print("\tguessed value is small")
        return 0

def easy(number):
    """Set's the difficulty mode to easy"""
    for i in range(10):
        print(f"    {10-i} rounds remaining")
        if find(number) == 0:
            pass
        else:
            return "You got it correctly \n \t------You Won------"
    return "You can't able to got it correctly \n \t------You Loose------"

def hard(number):
    """Set's the difficulty mode to hard"""
    for i in range (5):
        print(f"    {5-i} rounds remaining")
        if find(number) == 0:
            pass
        else:
            return "You got it correctly \n \t------You Won------"
    return "You can't able to got it correctly \n \t------You Loose------"
    

def play():
    print("  I'm thinking of a number between 1 and 100 ")
    print("  You have to guess it corectly ")
    level = input("  Enter a difficulty level 'easy' or 'hard' : ")
    number = get_number()
    if level == 'easy':
        print(easy(number))
    else:
        print(hard(number))
    sleep(5)
    
    

while(True):
    clear()
    print (logo)
    print("Welcome to Number guessing Game")
    val = input("Do you Want play game ? \n Enter 'Y' for yes and 'N' for no : ")
    if (val == 'Y') or (val == 'y'):
        play()
    else:
        print("\n\tThank You\n")
        break
