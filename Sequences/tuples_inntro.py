data = 1, 3, 5
a, b, c = data
print(a, b, c)


data_list = list(data)
print(data_list)

x, y, z = data_list
print(x, y, z)

data_list[2] = 7
print(x, y, z)
x, y, z = data_list
print(x, y, z)

data_list.append(9)
w, x, y, z = data_list
print(w, x, y, z)

data1 = ("Coffee Table", 36, 24, 18, 1500)
print(data1)
Name, Length, Width, Height, Price = data1
print(Name, Length, Width, Height, Price)
print("The dimensions of the {4} are {0} feet x {1} feet x {2} feet and costs Rs. {3}".format(Length/12, Width/12, Height/12, Price, Name))