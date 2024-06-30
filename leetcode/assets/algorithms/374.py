"""
374. Guess Number Higher or Lower
"""


class Solution:
    def guess(self, num):
        pick = 2
        if num == pick:
            return 0
        elif num > pick:
            return -1
        else:
            return 1

    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n

        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            pick = self.guess(mid)

            if pick == 0:       # your guess is equal to the number I picked 
                return mid
            elif pick < 0:      # Your guess is higher than the number I picked 
                right = mid - 1
            else:
                left = mid + 1  # Your guess is lower than the number I picked