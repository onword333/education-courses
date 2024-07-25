"""492. Construct the Rectangle"""


class Solution:
    def construct_rectangle(self, area: int):
        w = int(area ** 0.5)
        while area % w != 0:
            w -= 1

        return [area // w, w]


    def construct_rectangle_2(self, area: int):

        for n in range(int(area ** 0.5), 0, -1):
            if area % n == 0:
                return [area / n, n]

area = 122122
print(Solution().construct_rectangle(area))
print(Solution().construct_rectangle_2(area))