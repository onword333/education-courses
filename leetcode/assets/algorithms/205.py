"""
205. Isomorphic Strings
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map1 = {}
        map2 = {}

        for ch1, ch2 in zip(s, t):

            if ch1 in map1:
                if map1[ch1] != ch2:
                    return False
            else:
                map1[ch1] = ch2

            if ch2 in map2:
                if map2[ch2] != ch1:
                    return False
            else:
                map1[ch2] = ch1

        return True


s = 'egg'
t = 'add'

print(Solution().isIsomorphic(s, t))