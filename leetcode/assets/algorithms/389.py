"""
389. Find the Difference
"""
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # 1 variant
        # diff = []
        # for n in range(len(t)):
        #     t_char = t[n]
        #     if t_char not in s:
        #         diff.append(t_char)

        #     s = s.replace(t_char, '', 1)

        # return ''.join(diff)

        # 2 variant
        for n in range(len(s)):           
            t_char = s[n]
            t = t.replace(t_char, '', 1)
            
        # 3 variant
        # for n in t:
        #     if s.count(n) != t.count(n):
        #         return n
            

        return t




s = "a"
t = "aa"

obj = Solution()
print(obj.findTheDifference(s, t))
