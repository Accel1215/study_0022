vegetableOne = input("Input name of first vegetable")
vegetableTwo = input("Input name of second vegetable")
vegetableThree = input("Input name of third vegetable")

print('\n')

print(vegetableOne.lower(), vegetableTwo.lower(), vegetableThree.lower(), '', sep='\n')

print(vegetableOne.upper(), vegetableTwo.upper(), vegetableThree.upper(), '', sep='\n')

print(vegetableOne.capitalize(), vegetableTwo.capitalize(), vegetableThree.capitalize(), '', sep='\n')

numberOfVegetableOne = input("Input count of first vegetables")
numberOfVegetableTwo = input("Input count of second vegetables")
numberOfVegetableThree = input("Input count of third vegetables")

print('\n')

print("{0:>20}{1:>15}\n{2:>20}{3:>15}\n{4:>20}{5:>15}".format(vegetableOne, numberOfVegetableOne, vegetableTwo,
                                                              numberOfVegetableTwo, vegetableThree,
                                                              numberOfVegetableThree))
