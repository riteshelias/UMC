parts_list = ["CPU", "Monitor", "Keyboard", "Mouse", "Printer", "Webcam", "HDMI Cable", "Exit"]
change_parts = ["Plotter", "Projector"]
print(parts_list)
print()

# replace specific item at given index
parts_list[7] = "Scanner"
print(parts_list)

# replace range using slicing

parts_list[4:6] = change_parts
print(parts_list)

#  deleting part of list using slicing
del parts_list[4:6]
print(parts_list)

#  deleting part of list using negative index in slicing

del parts_list[-2:]
print(parts_list)

