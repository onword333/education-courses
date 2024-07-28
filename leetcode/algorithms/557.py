"""557. Reverse Words in a String III"""


class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        words = s.split()
        for w in words:
            res.append(w[::-1])

        return ' '.join(res)


s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))