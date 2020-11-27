phrase = "The quick brown fox jumps over the lazy dog"

print(phrase.split())

numbers1 = "221 55 665 293 71 868 104"
numbers = numbers1.split()
numbers2 = []

for num in numbers:
    numbers2.append(int(num))
    #  print(type(num))
print(numbers2)
print(type(numbers2))