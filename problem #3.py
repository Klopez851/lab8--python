#############################################
# Author: Keidy Lopez
# Filename: problem #3.py
# Description:
#############################################
import random

# Write a function which simulates a throw of a single die called rollDie. The function returns a
# random number from 1 to 6. Use the above function in the main program to roll two die until you
# get doubles. Print each roll of dice and also the number of rolls required to get the double.

def main():
    # welcome statement
    print('DICE SIMULATOR')
    print('this program will print a set of dice rolls until a double is rolled')
    # condition for while loop
    my_condition = True

    # while loop that prints cice rolls and stops at doubles
    counter = 0 # counts the number of rools before doubles are rolled
    while my_condition:
        roll1 = rollDie()
        roll2 = rollDie()
        if roll1 != roll2:
            print('roll:', roll1,roll2)
            counter+=1
        else:
            print('roll:', roll1, roll2)
            print('Doubles!')
            counter+=1
            print(str(counter)+' dice were rolled before doubles were rolled')
            my_condition =False

# function that returns a random int between 1 and 6
def rollDie():
    roll = random.randint(1,6)
    return roll



if __name__ == '__main__':
    main()