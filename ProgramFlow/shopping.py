shopping_list = ["Milk", "Eggs", "Noodles", "Spam", "Bread", "Butter"]
find_item = "Spam"
found_at = None
bal_list = ""

for index in range(len(shopping_list)):
    if shopping_list[index] == find_item:
        found_at = index
        #        continue
        break
    else:
        if bal_list == "":
            bal_list = shopping_list[index]
        else:
            bal_list = bal_list + ", " + shopping_list[index]

print("The correct shopping list is: " + bal_list)
print()
print("{0} found at number {1}".format(find_item, found_at))

# Alternative Method
found_at = None

if find_item in shopping_list:
    found_at = shopping_list.index(find_item)

print("{0} found at number {1}".format(find_item, found_at))

print()


