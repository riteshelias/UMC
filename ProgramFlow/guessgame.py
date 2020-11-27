import random

answer = random.randint(1, 10)
print(answer)
tries = 1
print()
print("Lets play a guessing game, you can exit by pressing 0")
guess = int(input("try count - {}. Please enter a number between 1 and 10: ".format(tries)))
while guess != answer:
    if guess == 0:
        print("Bye, have a nice day!")
        break
    if tries == 5:
        print("You have reached your guess limit. Bye!")
        break
    tries += 1
    guess = int(input("try count - {}. Please enter a number between 1 and 10: ".format(tries)))
else:
    if tries == 1:
        print("Wow, correct guess at the first time!")
    else:
        tries += 1
        print("You took {} tries to guess right!".format(tries))

# if guess == answer:
#     print("Woah! You got that right at the first go!")
# else:
#     if guess < answer:
#         print("Please guess a higher number")
#     else:
#         print("Please guess a lower number")
#     guess = int(input("Try again: "))
#     if guess == answer:
#         print("You get it finally")
#     else:
#         print("Oops! Still wrong!")


# if guess != answer:
#     if guess < answer:
#         print("Please guess a higher number")
#     else:
#         print("Please guess a lower number")
#     guess = int(input("Guess again: "))
#     if guess == answer:
#         print("You finally got it")
#     else:
#         print("Sorry, you still didn't get it")
# else:
#     print("Woah! You got it right the first time")

# if guess < 1 or guess > 10:
#     print("The entered number is not in the requested range")
# elif guess < answer:
#     print("Please guess a higher number")
# elif guess > answer:
#     print("Please guess a lower number")
# else:
#     print("You guessed right!")
