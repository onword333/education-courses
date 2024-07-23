"""
345. Reverse Vowels of a String
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        slist = list(s)

        # two point
        left, right = 0, len(s) - 1

        while left < right:
            print(3)
            if slist[left] not in vowels:
                left += 1
            elif slist[right] not in vowels:
                right -= 1
            else:
                slist[left], slist[right] = slist[right], slist[left]
                left += 1
                right -= 1

        return ''.join(slist)


s = 'leetcode'
obj = Solution()
print(obj.reverseVowels(s))
