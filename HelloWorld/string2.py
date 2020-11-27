parrot = 'Norwegian Blue'

#STRING INDEX

print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

# STRING NEGATIVE INDEX

print()
print(parrot)
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print(parrot)
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

#STRING SLICING

print()
print(parrot)
print(parrot[10:14])
print(parrot[10:])
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print(parrot[:6] + parrot[6:])

print(parrot[:])

letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[0:5])
print(letters[0] + letters[15] + letters[15] + letters[11] + letters[4])


#STRING SLICING WITH NEGATIVE INDEX

print(parrot[-14:-5])
print(parrot[-14:9])
print(parrot[-14:14])
print(parrot[-14:-5])


#STRING SLICING WITH STEPS

print(parrot[0:6:2])
print(parrot[0:6:3])


number = "6,778,651,439,551,098,805"
print(number[1::4])
