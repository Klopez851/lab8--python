#############################################
# Author: Keidy Lopez
# Filename: problem #5.py
# Description: program that tells user its tax income
#############################################

def taxIncome(m,i):
    # determines if married or single and subtracs correct amount
    if m == 1:
        income = i-5000
    else:
        income = i-8000

    # determines what tax rate to use depending on what the income is
    if income <= 12500:
        income = income*.03
        return income
    elif 12500<income<=20000:
        income = income*.12
        return income
    elif 20000<income<=52000:
        income = income*.23
        return income
    elif 52000<income<=80000:
        income = income*.31
        return income
    elif 80000<income<=100000:
        income = income*.33
        return income
    elif 100000<income:
        income = income*.35
        return income

def main():
    print('TAX INCOME CALCULATOR')
    name = input('What is your name? ')
    year = input('What tax year are you looking to calculate? ')
    income = int(input('What is your yearly income(no commas)?'))
    marital_status = int(input('What is you marital status? (enter 1 if single/2 if married) '))
    print(name+' your tax income for the year '+year+' is '+str(taxIncome(marital_status,income)))


if __name__ == '__main__':
    main()