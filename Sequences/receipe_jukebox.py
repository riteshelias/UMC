# Importing the dishes tuple from the receipe.py file
from receipes import dishes

name = cuisine = category = ingredients = None
receipe_list = (name, cuisine, category, ingredients)
print("Please the dishes:")
while True:
    for index, receipe_list in enumerate(dishes):
        print(index + 1, receipe_list[0])
    break

