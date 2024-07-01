"""
387. First Unique Character in a String
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_count = {}

        for ch in s:
            if ch in char_count:
                char_count[ch] += 1
            else:
                char_count[ch] = 1

        
        print(char_count)

        for i, v in enumerate(s):            
            if char_count[v] == 1:
                return i

        return -1

    def firstUniqChar_2(self, s: str) -> int:
        char_count = {}

        for ch in s:
            char_count[ch] = 1 + char_count.get(ch, 0)

        for n in range(len(s)):
            if char_count[s[n]] == 1:
                return n

        return -1

s = 'dddccdbba'

obj = Solution()
print(obj.firstUniqChar(s))