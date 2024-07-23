"""
168. Excel Sheet Column Title
"""


def convertToTitle(columnNumber):
    result = ""
    while columnNumber > 0:
        columnNumber, remainder = divmod(columnNumber - 1, 26)
        result = chr(65 + remainder) + result
    return result


nums = 701
print(convertToTitle(nums))