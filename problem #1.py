#############################################
# Author: Keidy Lopez
# Filename: problem #1.py
# Description: program that determines whether a number is odd or even using a function
#############################################

def main():
    # welcome statement
    print('ODD OR EVEN')

    # condition for while loop
    my_condition =  True

    # while loop that asks the user for integer input ad determines whether the integer is even or add and continues
    # until they are done
    while my_condition:
        num = int(input('Please enter an integer: '))
        if isEven(num) == True:
            print('your number is even :D')
            answer = input('Would you like to enter another number? (Y/N) ')
            if answer.upper()!='Y':
                my_condition = False
        elif isEven(num) == False:
            print('your number is odd :D')
            answer = input('Would you like to enter another number? (Y/N) ')
            if answer.upper() != 'Y':
                my_condition = False

# function that determines whether input is odd or even and returns a bool variable
def isEven(a:int)->bool:
    modulo = a % 2
    if modulo == 1:
        return False
    elif modulo == 0:
        return True


if __name__ == '__main__':
    main()