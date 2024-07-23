"""
263. Ugly Number
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        # O(log n)
        if n <= 0:
            return False

        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime

        return n == 1
    
    def isUgly_2(self, n: int) -> bool:
        # O(log n)
        if n <= 0:
            return False

        while n >= 1:
            if n % 2 == 0:
                n //= 2
            elif n % 3 == 0:
                n //= 3
            elif n % 5 == 0:
                n //= 5
            elif n == 1:
                return True
            else:
                return False


obj = Solution()
num = 6
print(obj.isUgly(num))
print(obj.isUgly_2(num))
