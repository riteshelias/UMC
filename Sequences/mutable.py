shopping_list = [
                "bread",
                "eggs",
                "pasta",
                "cheese",
                "herbs"
                ]
print(shopping_list)
print(id(shopping_list))
another_list = shopping_list
print(id(another_list))
print()
shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
print(another_list)
print()
a = b = c = shopping_list
print(a)
b.append("noodles")
print(c)
print(another_list)