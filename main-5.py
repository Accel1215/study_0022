firstWordList = input('Input some words').split(",")

print("Count of word in list", len(firstWordList))

secondWordList = input('Input {} words'.format(len(firstWordList))).split(",")

if len(firstWordList) != len(secondWordList):
    print("Count of lists not match. Dictionary will create with size of first list")

d = dict(zip(firstWordList, secondWordList))

print(d)
