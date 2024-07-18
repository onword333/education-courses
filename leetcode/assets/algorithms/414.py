"""414. Third Maximum Number"""


class Solution:
    def thirdMax(self, nums) -> int:
        uniq = set(nums)

        uniq_sorted = sorted(uniq, reverse=True)
        if len(uniq_sorted) < 3:
            return uniq_sorted[0]

        return uniq_sorted[2]


nums = [2, 2, 3, 1]

print(Solution().thirdMax(nums))
