# word = "Norwegian Blue"
#
# for alphabet in word:
#     print(alphabet)

# number = "1,2,4555,32,1134.001"

number = input("Please enter a random series of numbers with separators :")

separators = ""
digits = ""
total = 0

for char in number:
    if char.isnumeric():
        digits = digits + char
        total = total + int(char)
    else:
        separators = separators + char
        char.isupper()
print(digits)
print(total)
print(separators)
