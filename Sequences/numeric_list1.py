odd = [11, 13, 15, 17, 19,]
even = [22, 24, 26, 28]

empty_list = []

empty_list = [even, odd]
print(empty_list)

for number_list in empty_list:
    print(number_list)
    for value in number_list:
        print(value)