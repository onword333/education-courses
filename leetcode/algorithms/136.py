"""
136. Single Number
"""


def singleNumber(nums):
    answer = 0
    for n in nums:
        answer ^= n
    return answer


nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))