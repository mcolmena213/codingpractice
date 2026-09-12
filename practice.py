# TWO SUM
#
# Given an array of integers called nums and an integer called target,
# return the INDICES of the two numbers that add up to target.
#
# Rules:
# - There is exactly one solution.
# - You cannot use the same element twice.
# - Return the indices, NOT the actual numbers.
#
# Example:
# nums = [2, 7, 11, 15]
# target = 9
#
# Expected output: [0, 1]
# Because nums[0] + nums[1] = 2 + 7 = 9


# nums = [2, 7, 11, 15]
# target = 9


# def two_sum(nums, target):
#     # Write your solution here
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 if nums[i] + nums[j] == target:
#                     return [i , j]

# print(two_sum(nums, target))


# FIND A PAIR WITH A DIFFERENCE
#
# Given an array of integers called nums and an integer called target,
# return the INDICES of two DIFFERENT numbers whose difference equals target.
#
# Rules:
# - You cannot use the same element twice.
# - Return the indices, NOT the values.
# - Assume exactly one solution exists.
#
# Example:
# nums = [4, 9, 2, 7]
# target = 5
#
# Expected output: [0, 1]
# Because:
# nums[1] - nums[0] = 9 - 4 = 5


# nums = [4, 9, 2, 7]
# target = 5


# def find_difference(nums, target):
#     # Write your solution here
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 if nums[i] - nums[j] == target:
#                     return [i, j]


# print(find_difference(nums, target))

# FIND THE FIRST NUMBER GREATER THAN TARGET
#
# Given an array of integers called nums and an integer called target,
# return the INDEX of the FIRST number that is greater than target.
#
# Rules:
# - Return the index, NOT the value.
# - Stop as soon as you find the first number greater than target.
# - You only need ONE loop.
#
# Example:
# nums = [3, 5, 12, 7, 20]
# target = 10
#
# Expected output: 2
#
# Because:
# nums[0] = 3  -> not greater than 10
# nums[1] = 5  -> not greater than 10
# nums[2] = 12 -> greater than 10
#
# So return index 2.


# nums = [3, 5, 12, 7, 20]
# target = 10


# def first_greater(nums, target):
#     # Write your solution here
#     for i in range(len(nums)):
#         if nums[i] > target:
#             return i


# print(first_greater(nums, target))

# FIND THE FIRST EVEN NUMBER
#
# Given an array of integers called nums,
# return the INDEX of the FIRST even number.
#
# Rules:
# - Return the index, NOT the value.
# - Stop as soon as you find the first even number.
# - You only need ONE loop.
#
# Hint:
# A number is even if:
# number % 2 == 0
#
# Example:
# nums = [3, 7, 9, 12, 5, 8]
#
# Expected output: 3
#
# Because:
# nums[0] = 3  -> odd
# nums[1] = 7  -> odd
# nums[2] = 9  -> odd
# nums[3] = 12 -> even
#
# So return index 3.


# nums = [3, 7, 9, 12, 5, 8]


# def first_even(nums):
#     for i in range(len(nums)):
#         if nums[i] %2 == 0:
#             return i
# print(first_even(nums))

# FIND THE LARGEST NUMBER
#
# Given an array of integers called nums,
# return the INDEX of the LARGEST number.
#
# Rules:
# - Return the index, NOT the value.
# - Use ONE loop.
# - Do NOT use max().
#
# Example:
#
# nums = [4, 9, 2, 15, 7]
#
# Expected output: 3
#
# Because nums[3] = 15, which is the largest number.


# nums = [4, 9, 2, 15, 7]


# def largest_index(nums):
#     # Write your solution here
#     largest_index = 0 # need a index that we are comparing from.
#     for i in range(len(nums)):
#     # for j in range(len(nums)):
#     #     if nums[i] != nums[j]:
#     #         if nums[i] > nums[j]:
#     #             return i 
#     #         else:
#     #            nums[i] < nums[j]
#     #         return j
#     # if nums[i] > 14:
#     #     return i
#         if nums[i] > nums[largest_index]:
#             largest_index = i
#     return largest_index
# print(largest_index(nums))
        
# FIND THE SMALLEST NUMBER
#
# Given an array of integers called nums,
# return the INDEX of the SMALLEST number.
#
# Rules:
# - Return the index, NOT the value.
# - Use ONE loop.
# - Do NOT use min().
#
# Example:
#
# nums = [8, 5, 12, 3, 9]
#
# Expected output: 3
#
# Because:
# nums[3] = 3, which is the smallest number.


nums = [8, 5, 12, 3, 9]


def smallest_index(nums):
    # Write your solution here
    smallest_index = 0

    for i in range(len(nums)):
        if nums[smallest_index] > nums[i]:
            smallest_index = i
    return smallest_index
    

print(smallest_index(nums))
