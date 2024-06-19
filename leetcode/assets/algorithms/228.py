"""
228. Summary Ranges
"""


class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return nums

        ranges = []
        start = nums[0]
        end = nums[0]

        for n in range(1, len(nums)):

            if nums[n] == end + 1:
                end = nums[n]
            else:
                if start == end:
                    ranges.append(f'{start}')
                else:
                    ranges.append(f'{start}->{end}')

                start = nums[n]
                end = nums[n]

        if start == end:
            ranges.append(f'{start}')
        else:
            ranges.append(f'{start}->{end}')

        return ranges


l = [0, 1, 2, 4, 5, 7]

obj = Solution()
print(obj.summaryRanges(l))