#############################################
# Author: Keidy Lopez
# Filename: problem #7.py
# Description:
#############################################
import random

# displays menu options for player, makes sure the option is valid, and returns that choice
def menuDisplay():
    my_condition = True
    while my_condition:
        print('1. Over Seven\n2. Lucky Seven\n3. Under Seven')
        choice = int(input('Please choose an option (1,2 or 3): '))
        if choice > 3 or choice <= 0:
            print('please enter a valid choice number')
        elif choice == 1 or choice == 2 or choice == 3:
            my_condition = False
            return choice

# rolls a dice and returns its sum
def rollDie()->tuple:
    roll3 = random.randint(1,6)
    roll2 = random.randint(1, 6)
    roll = roll2 +roll3
    return roll

# decides if the player won or not based on the roll and choice
def isWinner(choice:int, rollsum:int)->bool:
    if choice==1 and rollsum > 7:
        return True
    elif choice==2 and rollsum ==7:
        return True
    elif choice == 3 and rollsum < 7:
        return True
    elif choice==1 and rollsum <= 7:
        return False
    elif choice==2 and rollsum !=7:
        return False
    elif choice == 3 and rollsum >= 7:
        return False



def main():
    # welcome statements
    print('DICE GAME AGAINST COMPUTER')
    print("In this game you will have to guess whether a dice roll if over 7, under seven, or exactly seven\nIf your "
          "prediction is right, you win! if not, the computer wins!\nWhat is your guess?")
    my_condition = True   # condition for while loop
    while my_condition:   # while loop that displays many, displays option and rollsum, and tells player whether they win or loose
        choice = menuDisplay()
        roll_sum=rollDie()
        print('you choose:', choice)
        print('the roll sum is:', roll_sum)
        if isWinner(choice,roll_sum) == True:
            print('You are a Winner and get a Chicken Dinner!')
        else:
            print('You Lose – don’t be sad.  Play again!')

        answer=input('Would you like to play again(Y/N): ')  # allows the user to play again is desired
        if answer.upper() != 'Y':
            print('Thanks for playing!')
            my_condition=False





if __name__=='__main__':
    main()