import math
import random
import sys

zeroArgs = {'random'}
oneArgs = {'asin', 'abs', 'factorial'}
twoArgs = {'+', '-', '*', '/', '**'}


def calculate(operator, a=0.0, b=0.0):
    if operator in oneArgs:
        if operator == 'asin':
            return math.asin(a)
        elif operator == 'abs':
            return abs(a)
        elif operator == 'factorial':
            return math.factorial(a)

    elif operator in twoArgs:
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            try:
                a / b
            except ZeroDivisionError:
                print('Zero division')
                return None
            return a / b
        elif operator == '**':
            return a ** b

    elif operator in zeroArgs:
        return random.randint(0, 100)

    return None


mathMethod = input("Choose a math operation (+, -, *, /, **, random, abs, factorial, asin)")
result = 0

if mathMethod in oneArgs:
    number = input("Input number")

    try:
        number = float(number)
    except ValueError:
        print("Incorrect number")
        sys.exit(1)

    result = calculate(mathMethod, number)

elif mathMethod in twoArgs:
    numberOne = input("Input first number")
    numberTwo = input("Input second number")

    try:
        numberOne = float(numberOne)
        numberTwo = float(numberTwo)
    except ValueError:
        print("Incorrect numbers")
        sys.exit(1)

    result = calculate(mathMethod, numberOne, numberTwo)

elif mathMethod in zeroArgs:
    result = calculate(mathMethod)

else:
    print("No such math operator")
    sys.exit(1)

if result is not None:
    print("Result of", mathMethod, "is", result)
