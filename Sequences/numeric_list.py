odd = [1, 3, 5, 7, 9,]
even = [2, 4, 6, 8]
empty_list = []

empty_list = even + odd
print(empty_list)

odd.extend(even)
print(odd)
another_list = odd
print(another_list)
odd.sort()
print(odd)
print()
#  create list by using list() built-in
list1 = list(empty_list)

#  create list by using slicing
list2 = empty_list[:]

#  create list by using copy() method
list3 = empty_list.copy()

print(list1)
print(list2)
print(list3)
print()
odd.sort(reverse=True)
print(odd)
print(another_list)
print()
digits = sorted("452967")
print(digits)

#  checking if the first list is the same as the second list i.e. pointing to the same
#  returns of type boolean
print(list3 is odd)

# checking if the first list has same elements/values as the second list
#  returns of type boolean
print(list3 == odd)