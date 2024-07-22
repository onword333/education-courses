"""459. Repeated Substring Pattern"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        twice_s = (s + s)[1:-1]
        return s in twice_s
    

s = 'abab'
print(Solution().repeatedSubstringPattern(s))