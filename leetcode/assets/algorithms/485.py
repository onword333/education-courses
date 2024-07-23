"""485. Max Consecutive Ones"""


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        max_seq = 0
        i = 0

        for n in nums:
            if n != 1:
                i = 0
            else:
                i += 1

            if i > max_seq:
                max_seq = i

        return max_seq


nums = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums))