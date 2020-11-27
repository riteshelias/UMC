for i in range(1,16):
    print('The No. {0} squared is {1:3} and cubed is {2:4}'.format(i, i ** 2, i **3))
print('*' * 60)

print()

for i in range(1,16):
    print('The No. {0} squared is {1:3} and cubed is {2:4}'.format(i, i ** 2, i **3))
    print('*' * 60)

print()

name = input("Please enter your name: ")
# age = input("Please enter your age {0}: ".format(name))
age = int(input("Please enter your age {0}: ".format(name)))

if age < 18:
    print("Sorry {0}, you're too young. Please try after {1} years".format(name, 18 - age))
elif age > 100:
    print("Sorry {0}, you're a relic for this shit.".format(name))
else:
    print("Yo {0}, you're in your prime at {1} years".format(name, age))