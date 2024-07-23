"""
202. Happy Number
1-st variant
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n

        while True:
            slow = self.sum_of_squares(slow)
            fast = self.sum_of_squares(self.sum_of_squares(fast))
            print(slow, ' ... ', fast)
            if fast == 1:
                return True

            if slow == fast:
                return False

    def sum_of_squares(self, num):
        return sum(
            int(digit) ** 2 for digit in str(num)
        )


s = Solution()

for n in range(10):
    print(n, ' -> ', s.isHappy(n))


"""
2-st variant
"""

class Solution_2:
    def sum_of_squares(self, num):
        return sum(int(digit) ** 2 for digit in str(num))

    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)
        return n == 1


s = Solution_2()

for n in range(10):
    print(n, ' -> ', s.isHappy(n))