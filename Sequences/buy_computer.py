parts_list = ["CPU", "Monitor", "Keyboard", "Mouse", "Printer", "Webcam", "HDMI Cable", "Exit"]
selection = "-"
selected_parts = []
ind_list = []
for index in range(0, len(parts_list)):
    ind_list.append(str(index))

#  print(ind_list)

while selection != "0":
    if selection in ind_list:
        part = parts_list[int(selection) - 1]
        if part in selected_parts:
            print("Part removed: {}".format(selected_parts[int(selection) - 1]))
            selected_parts.remove(part)
            selection = "-"
        else:
            selected_parts.append(parts_list[int(selection) - 1])
            print("Part added: {}".format(parts_list[int(selection) - 1]))
        selection = "-"
        print(selected_parts)
    else:
        print("Welcome to the computer store")
        print("Please select from the below parts:")
        # for i in range(0, len(parts_list)):
        #     if i == 7:
        #         print("0:\t{}".format(parts_list[i]))
        #     else:
        #         print("{0}:\t{1}".format(i + 1, parts_list[i]))
        for num, part in enumerate(parts_list):
            if num == 7:
                print("0:\t{}".format(part))
            else:
                if part in selected_parts:
                    print("{0}:\t{1} - *Select again to remove*".format(num + 1, part))
                else:
                    print("{0}:\t{1}".format(num + 1, part))
        selection = input("Please enter your choice: ")
else:
    print("Your final list is: {}".format(selected_parts))
    print("Thanks for your order! Have a nice day!")