# i = 0
# while i < 10:
#     print("value of i is: {}".format(i))
#     i += 1

import random

print("Lets play the Rock Scissors Paper game!")
available_values = ["rock", "paper", "scissor"]
ai_selection_index  = random.randint(0, 2)
ai_selection_value = available_values[ai_selection_index]
#  print("The computer selected: {}".format(ai_selection_value))
chosen = input("Please enter your choice between the 3: ").casefold()

if chosen in available_values:
    if chosen == ai_selection_value:
        print("You entered {}".format(chosen))
        print("The computer selected {}".format(ai_selection_value))
        print("Oops! Its a draw as both chose the same! Try again")
    else:
        if ai_selection_value == "rock":
            if chosen == "scissor":
                print("You entered {}".format(chosen))
                print("The computer selected {}".format(ai_selection_value))
                print("Oh no! You lost!!")
            else:
                print("You entered {}".format(chosen))
                print("The computer selected {}".format(ai_selection_value))
                print("Wow! You won mate!!")
        elif ai_selection_value == "paper":
            if chosen == "scissor":
                print("You entered {}".format(chosen))
                print("The computer selected {}".format(ai_selection_value))
                print("Wow! You won mate!!")
            else:
                print("You entered {}".format(chosen))
                print("The computer selected {}".format(ai_selection_value))
                print("Oh no! You lost!!")
        else:
            if chosen == "rock":
                print("You entered {}".format(chosen))
                print("The computer selected {}".format(ai_selection_value))
                print("Wow! You won mate!!")
            else:
                print("You entered {}".format(chosen))
                print("The computer selected {}".format(ai_selection_value))
                print("Oh no! You lost!!")
else:
    print("You never played Rock Paper Scissor huh? C'mon enter a proper value, start again!")



