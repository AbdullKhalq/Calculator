# This calculator will do basic operations including square root
import math


def basic_operations():
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)


def root_operation():
    num0 = float(input('Enter number: '))
    print(f'The square root of {num0} is ', math.sqrt(num0))


operator = input('Enter operation: ')
if operator != 'root':
    basic_operations()
elif operator == 'root':
    root_operation()
else:
    print('Invalid or unsupported operation, please try again')

