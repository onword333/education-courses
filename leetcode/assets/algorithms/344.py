"""
344. Reverse String
"""


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left, right = 0, len(s) - 1

        while left < right:            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1



s =  ["h", "e", "l", "l", "o"]

obj = Solution()
obj.reverseString(s)
