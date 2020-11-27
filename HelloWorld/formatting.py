# Default print
for i in range(1,15):
    print("The No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

print()

# Set column width
for i in range(1,15):
    print("The No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

#Set column width with left alignment
for i in range(1,15):
    print("The No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print()

#Set column width with centre alignment
for i in range(1,15):
    print("The No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("Pi is approximately : {0}".format(22/7))
print("Pi is approximately : {0:12}".format(22/7))
print("Pi is approximately : {0:12f}".format(22/7))
print("Pi is approximately : {0:12.50f}".format(22/7))
print("Pi is approximately : {0:52.50f}".format(22/7))
print("Pi is approximately : {0:62.50f}".format(22/7))
print("Pi is approximately : {0:82.50f}".format(22/7))
