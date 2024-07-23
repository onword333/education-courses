"""
292. Nim Game
"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


pattern = 'abba'
n = 4

obj = Solution()
print(obj.canWinNim())