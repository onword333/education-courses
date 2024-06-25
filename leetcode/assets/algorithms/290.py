"""
290. Word Pattern
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(words) != len(pattern):
            return False

        p2w = {}
        w2p = {}

        for p, w in zip(pattern, words):      
            if p not in p2w and w not in w2p:
                p2w[p] = w
                w2p[w] = p

            if p2w.get(p) != w or w2p.get(w) != p:
                return False

        return True


pattern = 'abba'
s = 'dog cat cat dog'

obj = Solution()
print(obj.wordPattern(pattern, s))
