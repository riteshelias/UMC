pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)
print(pangram)

numbers = [4.7, 3.9, 7.7, 9.1, 6.3, 1.2]
another_set = sorted(numbers)
print(another_set)

print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(another_set)

print()

string1 = sorted("The quick brown fox jumps over the lazy dog", key=str.casefold)
print(string1)

string2 = [
            "Michael",
            "john",
            "Eric",
            "santana",
            "Carlos",
            "adolf"
            ]

print(string2)
print(sorted(string2, key=str.casefold))
print(string2)