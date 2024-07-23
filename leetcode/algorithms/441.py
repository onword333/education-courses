"""441. Arranging Coins"""
import math

class Solution:

    
    def arrange_coins(self, n: int) -> int:
        """
        Метематический подход. Формула:
        (- 1 + sqrt(1 + 8 * n)) // 2
        """
        k = int((-1 + math.sqrt(1 + 8 * n)) // 2)
        return k


    def arrange_coin_bs(self, n: int) -> int:
        """Решение с помощью бинарного поиска"""
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            cur = mid * (mid + 1) // 2

            if cur == n:
                return mid
            elif cur < n:
                left = mid + 1
            else:
                right = mid - 1

        return right

n = 8

print(Solution().arrange_coins(n))
print(Solution().arrange_coins(n))
