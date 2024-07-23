"""
125. Valid Palindrome
"""

import re


def isPalindrome(s):
    new_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return new_str == new_str[::-1]


s = 'A man, a plan, a canal: Panama'
print(isPalindrome(s))
