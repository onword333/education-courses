"""
278. First Bad Version

Для решения будем использовать бинарный поиск
"""


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if self.isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left

    def isBadVersion(self, n) -> bool:
        if n == 4:
            return True
        else:
            False


obj = Solution()
num = 5
print(obj.firstBadVersion(num))
