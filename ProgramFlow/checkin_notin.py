word = "Norwegian Blue"
letter = input("Please enter a letter: ")

if letter in word:
    print("{0} is in {1}".format(letter, word))
else:
    print("The letter {0} does not exist in {1}".format(letter, word))