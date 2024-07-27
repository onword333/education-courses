"""506. Relative Ranks"""


class Solution:
    def findRelativeRanks(self, score):
        sorted_score = sorted(score, reverse=True)
        ranks = {}

        for k, v in enumerate(sorted_score):
            if k == 0:
                ranks[v] = 'Gold Medal'
            elif k == 1:
                ranks[v] = 'Silver Medal'
            elif k == 2:
                ranks[v] = 'Bronze Medal'
            else:
                ranks[v] = str(k + 1)

        return [ranks[s] for s in score]


score = [5, 4, 3, 2, 1]

print(Solution().findRelativeRanks(score))