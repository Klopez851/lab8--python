#############################################
# Author: Keidy Lopez
# Filename: problem #6.py
# Description: program that takes integer input and prints if its prime or not
#############################################

# determines whether a number is prime and returns a bool variable
def isPrime(a):
    if a == 1:
        return False
    elif a < 0:
        return print('please enter a positive number')
    elif a > 1:
        for i in range (2,a):
            if (a % i) == 0:
                return False
        else:
            return True

def main():
    # welcome statement
    print('PRIME NUMBERS')
    num = int(input('please enter a positive number: '))

    # determines whther num if prime or not
    if isPrime(num) == True:
        print(str(num)+' is prime')
    else:
        print(str(num) + ' is not prime')


if __name__ == '__main__':
    main()