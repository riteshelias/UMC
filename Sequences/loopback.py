nums = [109, 169, 4, 122, 103, 244, 23, 127,
        155, 199, 107, 44, 305, 114]

min_val = 100
max_val = 200

# for index in range(len(nums) - 1, -1, -1):
#     if nums[index] <= min_val or nums[index] >= max_val:
#         del nums[index]
#         print(index, nums)
top_index = len(nums) - 1

for index, value in enumerate(reversed(nums)):
    if value < min_val or value > max_val:
        print(top_index - index, value)
        del nums[top_index - index]
print()
print(nums)