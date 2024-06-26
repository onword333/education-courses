"""
338. Counting Bits
"""


class Solution:
    def countBits(self, n: int) -> []:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


n = 15
obj = Solution()
print(obj.countBits(n))
