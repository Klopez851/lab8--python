#############################################
# Author: Keidy Lopez
# Filename: problem #2.py
# Description: program that prints out a random number in a given range
#############################################
import random

def main():
    # welcome statement
    print('RANDOM NUMBER GENERATOR')
    print('this program takes 2 numbers and returns a random number in that range')

    # maint interger values
    num1 = int(input('please enter the first number: '))
    num2 = int(input('please enter the second number: '))

    # checks if integers are positive
    if num1 < 0 or num2 < 0:
        print('please enter a positive value')
        return

    # prints put random number in the given range
    print('your random number between '+str(num1)+' and '+str(num2)+' is: '+str(getRandom(num1, num2)))

# function that returns a radom number the the range of two integers given
def getRandom(a:int, b:int)->int:
    rand_num = random.randint(a,b)
    return rand_num


if __name__ == '__main__':
    main()