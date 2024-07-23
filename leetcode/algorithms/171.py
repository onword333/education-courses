"""
171. Excel Sheet Column Number
"""


def titleToNumber(columnTitle):
    res = 0
    for ch in columnTitle:
        res = res * 26 + ord(ch) - ord('A') + 1
    return res


column = 'ZY'
print(titleToNumber(column))
