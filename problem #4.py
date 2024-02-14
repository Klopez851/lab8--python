#############################################
# Author: Keidy Lopez
# Filename: problem #4.py
# Description: program that prints out how many even or odd rolls were rolled in 100 dice rolls
#############################################
import random

# simulates a dice roll
def rollDie():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1, 6)
    roll = roll2+roll1
    return roll

# determines whether a number is even or odd
def isOdd(a:int)->bool:
    modulo = a % 2
    if modulo == 1:
        return False
    elif modulo == 0:
        return True

def main():
    # WELCOME STATEMENT
    print('DICE SIMULATOR')
    print('this program will tell you have many odd and even were rolled in 100 dice rolls')

    # counter to keep track of even and odd numbers rolled
    even_counter = 0
    odd_counter = 0

    # for loop that will roll die 100 times and determines if odd or even
    for i in range(100):
        if isOdd(rollDie()) == False:
            odd_counter += 1
        else:
            even_counter += 1

    # prints out results of 100 rolls
    print(even_counter,'of the rolls were even')
    print(odd_counter, 'of the rolls were odd')

if __name__ == '__main__':
    main()