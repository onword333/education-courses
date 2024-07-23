"""
169. Majority Element
"""


def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]


def majorityElement_2(nums):
    # Алгоритм большинства голосов Бойера — Мура

    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [3, 2, 3]
print(majorityElement(nums))
print(majorityElement_2(nums))
