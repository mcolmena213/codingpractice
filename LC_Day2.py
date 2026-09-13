# # COUNT NUMBERS GREATER THAN TARGET
# #
# # Given an array of integers called nums and an integer target,
# # return HOW MANY numbers are greater than target.
# #
# # Rules:
# # - Return the COUNT, not an index.
# # - Use ONE loop.
# #
# # Example:
# #
# # nums = [4, 12, 7, 20, 3, 15]
# # target = 10
# #
# # Expected output: 3
# #
# # Because:
# # 4  > 10 -> No
# # 12 > 10 -> Yes
# # 7  > 10 -> No
# # 20 > 10 -> Yes
# # 3  > 10 -> No
# # 15 > 10 -> Yes
# #
# # Three numbers are greater than 10.


# nums = [4, 12, 7, 20, 3, 15]
# target = 10


# def count_greater(nums, target):
#     # Write your solution here
#     larger_than_target = 0
#     for i in range(len(nums)):
#         if nums[i] > target:
#             larger_than_target += 1
#     return larger_than_target
 
# print(count_greater(nums, target))


# COUNT EVEN NUMBERS
#
# Given an array of integers called nums,
# return how many numbers are EVEN.
#
# Rules:
# - Return the COUNT.
# - Use ONE loop.
#
# nums = [3, 8, 12, 5, 7, 10, 4]
#
# Expected output: 4


# nums = [3, 8, 12, 5, 7, 10, 4]


# def count_even(nums):
#     # Your solution here
#     even_count = 0

#     for i in range(len(nums)):
#         if nums[i] %2 == 0:
#             even_count +=1 
#     return even_count
 
# print(count_even(nums))

# SUM ALL EVEN NUMBERS
#
# Given an array of integers called nums,
# return the SUM of all even numbers.
#
# Rules:
# - Return the sum, NOT the count.
# - Use ONE loop.
# - Do NOT use sum().
#
# Example:
#
# nums = [3, 8, 12, 5, 7, 10, 4]
#
# Even numbers:
# 8 + 12 + 10 + 4 = 34
#
# Expected output: 34


# nums = [3, 8, 12, 5, 7, 10, 4]


# def sum_even(nums):
#     # Your solution here
#     sum_even = 0
#     for i in range(len(nums)):
#         if nums[i] %2 == 0:
#             # nums[i] + nums[sum_even]
#             sum_even += nums[i]
#     return sum_even


# print(sum_even(nums))

# FIND THE AVERAGE OF EVEN NUMBERS
#
# Given an array of integers called nums,
# return the AVERAGE of all even numbers.
#
# Rules:
# - Use ONE loop.
# - Do NOT use sum().
# - Keep track of BOTH:
#       1. How many even numbers you've found
#       2. The sum of the even numbers
#
# Example:
#
# nums = [3, 8, 12, 5, 10, 4]
#
# Even numbers:
# 8, 12, 10, 4
#
# Sum = 34
# Count = 4
#
# Average = 34 / 4 = 8.5
#
# Expected output: 8.5


# nums = [3, 8, 12, 5, 10, 4]


# def average_even(nums):
#     # Your solution here
#     total = 0 
#     count = 0 
#     for i in  range(len(nums)):
#             if nums[i] %2 == 0:
#                 count += 1
#                 total += nums[i] 
                
#     return total / count


# print(average_even(nums))

# COLLECT NUMBERS GREATER THAN TARGET
#
# Given an array of integers called nums and an integer target,
# return a NEW LIST containing every number greater than target.
#
# Rules:
# - Return the VALUES, not their indices.
# - Use ONE loop.
# - Do not modify nums.
#
# Example:
#
# nums = [4, 12, 7, 20, 3, 15]
# target = 10
#
# Expected output:
# [12, 20, 15]


# nums = [4, 12, 7, 20, 3, 15]
# target = 10
# greater_than = []

# def greater_than_target(nums, target):
#     # Your solution here
#     for i in range(len(nums)):
#         if nums[i] > target:
#             greater_than.append(nums[i])
#             #we used append to add to the list
#     return greater_than
 

# print(greater_than_target(nums, target))

# DOUBLE THE EVEN NUMBERS
#
# Given an array of integers called nums,
# return a NEW LIST containing each EVEN number multiplied by 2.
#
# Rules:
# - Only include even numbers.
# - Multiply each qualifying number by 2.
# - Return the new list.
# - Use ONE loop.
# - Do not modify nums.
#
# Example:
#
# nums = [3, 8, 5, 12, 7, 4]
#
# Even numbers:
# 8, 12, 4
#
# Doubled:
# 16, 24, 8
#
# Expected output:
# [16, 24, 8]


# nums = [3, 8, 5, 12, 7, 4]
# # doubled = [] remove from globally
# even_nums = 0

# def double_evens(nums):
#     doubled = []
#     # Your solution here
#     for i in range(len(nums)):
#         if nums[i] %2 == 0:
            
            
#             doubled.append(nums[i]*2)
          
    
#     return doubled 
     
 

# print(double_evens(nums))


# FIND ALL NUMBERS BELOW THE AVERAGE
#
# Given an array of integers called nums,
# return a NEW LIST containing every number
# that is BELOW the average of all numbers.
#
# Rules:
# - Do NOT use sum().
# - Use loops.
# - Do not modify nums.
#
# Example:
#
# nums = [4, 8, 10, 2, 6]
#
# Total = 30
# Count = 5
# Average = 6
#
# Numbers below 6:
# 4, 2
#
# Expected output:
# [4, 2]


nums = [4, 8, 10, 2, 6]


def below_average(nums):

    total = 0

    for i in range(len(nums)):
        total += nums[i]

    average = total / len(nums)

    below = []
    for i in range(len(nums)):
        if nums[i] < average:
            below.append(nums[i])

    return below


print(below_average(nums))
