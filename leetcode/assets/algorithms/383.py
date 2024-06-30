"""
383. Ransom Note
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            if ch not in magazine:
                return False
            
            magazine = magazine.replace(ch, ' ', 1)

        return True


ransomNote = 'aaa'
magazine = 'aaa'

obj = Solution()
print(obj.canConstruct(ransomNote, magazine))