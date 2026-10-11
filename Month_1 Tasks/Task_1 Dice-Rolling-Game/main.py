# Task 1 Dice-Rolling-Game

import random 

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2


def show_result(die1 ,die2):
    print(f"Die 1: {die1} , Die 2: {die2}")
    # print("Die 1: " , die1)
    # print("Die 2: ", die2)
    print("Total: ", die1 + die2)


def ask_roll_again():
    while True:
        answer = input("Roll again? (yes/no): ").strip().lower()
        if answer == "yes" or answer == "y":
            return True
        elif answer == "no" or answer == "n":
            return False
        else:
            print("Invalid Input, Please Type yes or no")



def main():
    print("Welcome Dice-Rolling-Game")
    while True:
        die1 , die2 = roll_dice()
        show_result(die1, die2)
        if ask_roll_again() is False:
            break
    print("Goodbye")

if __name__ == "__main__":
    main()
