menu = [
    ["Eggs", "Sausages"],
    ["Eggs", "Sausages", "Toast"],
    ["Eggs", "Sausages", "Toast", "Coffee", "Whisky"],
    ["Eggs", "Sausages", "Toast", "Coffee"],
    ["Eggs", "Sausages", "Toast", "Tea"],
    ["Eggs", "Sausages", "Toast", "Tea", "Whisky"],
    ["Corn flakes", "Whisky", "Milk", "Fruit", "Whisky"],
    ["Whisky", "Idli", "Wada", "Whisky", "Dosa", "Whisky", "Fruit Juice", "Whisky"],
]

new_menu = []
item_list = []

for brfast in menu:
    for item in brfast:
        if item != "Whisky":
            item_list.append(item)
        else:
            continue
    new_menu.append(item_list)
    print(", ".join(item_list))
    item_list = []
print(new_menu)

# for bfast in menu:
#     # print(bfast)
#     # print()
#     if "Whisky" not in bfast:
#         #  print(bfast)
#         continue
#     else:
#         print("{0} contains {1} pegs of whisky".format(bfast, bfast.count("Whisky")))