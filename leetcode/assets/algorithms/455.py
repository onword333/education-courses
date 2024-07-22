"""455. Assign Cookies"""

class Solution:

    def find_content_children(self, g, s) -> int:
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0
        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        return content_children


g = [1, 2]
s = [1, 2, 3]

print(Solution().find_content_children(g, s))
