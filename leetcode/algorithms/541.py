"""541. Reverse String II"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        res = []
        for n in range(0, len(s), 2 * k):
            part = s[n : n + 2 * k]
            res.append(part[:k][::-1] + part[k:])
        return ''.join(res)
    

s = 'abcdefg'
k = 2
print(Solution().reverseStr(s, k))