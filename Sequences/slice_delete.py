#  Remove lower & upper range values using two step elimination
#  This is the fastest way to delete/work with very large lists
#  BUT MIND - This works with an ordered list only
#  So if one has an unsorted list then order it first using
#  either the sorted() function or the list.sort() method

#  nums = [2, 6, 23, 45, 101, 117, 122, 145, 165, 179, 190, 193, 202, 251, 299]
nums1 = [109, 169, 4, 122, 103, 244, 23, 127,
        155, 199, 107, 44, 305, 114]
#  nums.sort()
nums = sorted(nums1)
print(nums)

print()

min_val = 100
max_val = 200

#  First step is to eliminate the lower range in one go by using slice
stop_index = 0

for index, value in enumerate(nums):
    if value > min_val:
        stop_index = index
        print(index, stop_index, value)
        break
del nums[:stop_index]
print(nums)

print()
# Second step is to eliminate the upper range in one go by using slice

start_index = 0

for index in range(len(nums) - 1, -1, -1):
    if nums[index] < max_val:
        #  Setting start_index to index + 1 so as to set the start
        #  position of the delete to the next of the last index found
        start_index = index + 1
        print(index, start_index, nums[index])
        break
del nums[start_index:]
print(nums)