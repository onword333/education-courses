"""
217. Contains Duplicate
"""


class Solution:
    # 1-st variant
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))

    # 2-end variant
    def containsDuplicate_2(self, nums) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False


nums = [1, 2, 3, 1]

print(Solution().containsDuplicate(nums))
print(Solution().containsDuplicate_2(nums))