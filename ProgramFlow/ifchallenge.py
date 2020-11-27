name = input("Please enter your name: ")
age = int(input("Please enter your age, {}: ".format(name)))

if 18 < age < 31:
    print("Welcome {} on this wonderful holiday!".format(name))
else:
    print("Sorry to inform you that you're not eligible for this holiday")