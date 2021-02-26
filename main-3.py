import math
import random

mathMethod = ""
result = 0

while True:

    mathMethod = input("Choose a math operation (+, -, *, /, **, random, abs, factorial, asin)")

    if (mathMethod == '+') or (mathMethod == '-') or (mathMethod == '*') or (mathMethod == '/') or (mathMethod == "**"):

        numberOne = input("Input first number")
        numberTwo = input("Input second number")

        try:
            numberOne = float(numberOne)
            numberTwo = float(numberTwo)
        except ValueError:
            print("Incorrect input values.")
            continue

        if mathMethod == '+':
            result = numberOne + numberTwo
        elif mathMethod == '-':
            result = numberOne - numberTwo
        elif mathMethod == '*':
            result = numberOne * numberTwo
        elif mathMethod == '/':
            result = numberOne / numberTwo
        elif mathMethod == "**":
            result = numberOne ** numberTwo

        break

    elif (mathMethod == "asin") or (mathMethod == "abs") or (mathMethod == "factorial"):

        number = input("Input number")

        try:
            number = float(number)
        except ValueError:
            print("Incorrect input value.")
            continue

        if mathMethod == "asin":
            result = math.asin(number)
        elif mathMethod == "abs":
            result = abs(number)
        elif mathMethod == "factorial":
            result = math.factorial(number)

        break

    elif mathMethod == "random":
        result = random.randint(0, 100)
        break

    print("Incorrect math method.")

print("Result of", mathMethod, "is", result)