def makeDict():
    first_word_list = input('Input some words').split(",")

    print("Count of word in list", len(first_word_list))

    second_word_list = input('Input {} words'.format(len(first_word_list))).split(",")

    if len(first_word_list) != len(second_word_list):
        print("Count of lists not match. Dictionary will create with size of first list")

    return dict(zip(first_word_list, second_word_list))


fileName = input("Input file name")
file = open(fileName, 'w')
file.write(makeDict().__str__())
file.close()
