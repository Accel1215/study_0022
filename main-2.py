inputString = input("Введите строку")

counter = 1
cIsInString = False

for i in inputString:
    if counter == 3:
        counter += 1
        continue

    if i == 'c':
        cIsInString = True

    if len(inputString) == counter:
        break

    print(i, end='')

    counter += 1

print(end="\n")

if cIsInString:
    print("This string contains the c")
