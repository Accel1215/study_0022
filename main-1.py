inputNumber = int(input("Введите число"))
border = int(input("Введите пограничное число"))

if inputNumber < border:
    print("Число меньше пограничного")
if inputNumber > (border * 3):
    print("Число более чем в 3 раза больше, чем пограничное число")
if inputNumber > border:
    print("Число больше пограничного.")



