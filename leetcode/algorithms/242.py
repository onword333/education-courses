"""
242. Valid Anagram
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for ch in zip(s, t):
            count_s[ch[0]] = count_s.get(ch[0], 0) + 1
            count_t[ch[1]] = count_t.get(ch[1], 0) + 1

        return count_s == count_t


obj = Solution()

s = 'aacc'
t = 'ccac'

# s = 'anagram'
# t = 'nagaram'

print(obj.isAnagram(s, t))