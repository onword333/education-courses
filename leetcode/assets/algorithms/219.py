"""
219. Contains Duplicate II
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        hashmap = {}

        for i, v in enumerate(nums):

            if v in hashmap and i - hashmap[v] <= k:
                return True

            hashmap[v] = i

        return False


k = 3
nums = [1, 2, 3, 1]

# k = 1
# nums = [1, 0, 1, 1]

# k = 2
# nums = [1, 2, 3, 1, 2, 3]

print(Solution().containsNearbyDuplicate(nums, k))