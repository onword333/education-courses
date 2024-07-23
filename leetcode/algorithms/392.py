"""
392. Is Subsequence
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)
        j = 0

        if s_len == 0:
            return True

        for val in t:
            if j < s_len and val == s[j]:
                j += 1

        if j == s_len:
            return True
        else:
            return False

s = "acb"
t = "ahbgdc"

obj = Solution()
print(obj.isSubsequence_2(s, t))