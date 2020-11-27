lower_limit = 1
upper_limit = 1000
print("Please think of a number between {0} and {1}".format(lower_limit, upper_limit))
guesses = 1
input("Please press the 'Enter' key to start: ")
while lower_limit != upper_limit:
    guess = lower_limit + ((upper_limit - lower_limit) // 2)
    print("My guess is {}".format(guess))
    hi_low = input("If I guessed correct then press 'c',"
                   " if I need to guess lower then press 'l' "
                   "and if I need to guess higher then press 'h': ".casefold())
    if hi_low == 'h':
        lower_limit = guess + 1
    elif hi_low == "l":
        upper_limit = guess - 1
    elif hi_low == "c":
        print("Wow! I guessed correctly in {} times".format(guesses))
        break
    else:
        print("Please enter 'c', 'h' or 'l'")
    guesses += 1
else:
    print("You chose {}".format(lower_limit))
    print("I guessed that in {} tries".format(guesses))