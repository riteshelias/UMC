task_list = ["Read a book", "Learn coding", "Get a snack", "Go Swimming", "Take a nap", "Exit"]
# print("Please select one of the below options")
#
# for index in range(1, len(task_list)):
#     print("{0}.\t{1}".format(index, task_list[index]))

selection = "*"  # input("Please enter your choice: ")

while selection != "5":  # True:
    # if selection == "5":
    #     print("You chose to exit. Bye!")
    #     break
    if selection in "1,2,3,4":
        print("You chose to {}".format(task_list[int(selection)]))
        break
    else:
        print("Please select one of the below options")
        for i in range(1, len(task_list)):
            print("{0}.\t{1}".format(i, task_list[i]))
        selection = input("Please enter your choice: ")


# quote = """
# Alright, but apart from the Sanitation, the Medicine, Education, Wine,
# Public Order, Irrigation, Roads, the Fresh-Water System,
# and Public Health, what have the Romans ever done for us?
# """

# # Use a for loop and an if statement to print just the capitals in the quote above.
# caps = ""
# for char in quote:
#     if char.isupper():
#         caps = caps + char
#
# print(caps)
#
# print()
#
# for i in range(0, 20):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     else:
#         print(i)


for x in range(30):
    if x % 3 != 0 and x % 5 != 0:
      #  continue
        print(x)