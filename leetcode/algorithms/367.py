"""
367. Valid Perfect Square
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left, right = 1, num

        while left < right:
            # mid = (left + right) // 2
            mid = left + (right - left) // 2
            mid_square = mid * mid

            if mid_square == num:
                return True
            elif mid_square < num:
                left = mid + 1
            else:
                right = mid

        return False


n = 104976
obj = Solution()
print(obj.isPerfectSquare(n))