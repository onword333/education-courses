"""
231. Power of Two
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

    def isPowerOfTwo_2(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1


l = 16

obj = Solution()
print(obj.isPowerOfTwo(l))
