dishes = [
    ("Kaju Katli", "Desi", "Dessert",
     (
         (1, "Cashew Nuts"),
         (2, "Mawa"),
         (3, "Sugar")
     )
     ),
    ("Machow Soup", "Chinese", "Soup",
     (
         (1, "Noodles"),
         (2, "Chicken"),
         (3, "Chopped Veggies"),
         (4, "Soya Sauce")
     )
     ),
    ("Hara bhara Kebab", "Desi", "Starters",
     (
         (1, "Spinach"),
         (2, "Corn"),
         (3, "Cheese"),
         (4, "Potatoes")
     )
     ),
    ("Tandoori Chicken", "Mughlai", "Starters",
     (
         (1, "Chicken"),
         (2, "Spices"),
         (3, "Butter")
     )
     ),
    ("Navratan Pulav", "Awadhi", "Main Course",
     (
         (1, "Mix Veggies"),
         (2, "Basmati Rice"),
         (3, "Dry Fruits")
     )
     ),
    ("Rogan Josh", "Kashmiri", "Main Course",
     (
         (1, "Mutton"),
         (2, "Spices"),
         (3, "Oil"),
         (4, "Onions")
     )
     ),
    ("Rosogolla", "Bengali", "Dessert",
     (
         (1, "Milk"),
         (2, "Sugar"),
         (3, "Water"),
         (4, "Rose essence")
     )
     ),
]

print(len(dishes))

print()

# for dish in dishes:
#     name, ingredients, category = dish
for name, cuisine, category, ingredients in dishes:
    # print("Name: {}, Ingredients: {}, Category: {}".format(dish[0], dish[1], dish[2]))
    print("Name: {}, Cuisine: {}, Category: {}, Ingredients: {}".format(name, cuisine, category, ingredients))

dish = dishes[1]
print(dish)
print()
ingredient = dish[3]
print(ingredient)

item = ingredient[1]
print(item)

print()
spitem = item[1]
print(spitem)
spitem1 = dishes[1][3][1][1]
print(spitem1)
print(dishes[1][3][1][1])

# for item in ingredient:
#     print(item)

