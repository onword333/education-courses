"""
303. Range Sum Query - Immutable
"""


class NumArray:

    def __init__(self, nums):
        self._nums = nums        

    def sumRange(self, left: int, right: int) -> int:        
        return sum(self._nums[left: right+1])


class NumArray_2:
    # O(1)
    def __init__(self, nums):
        self.nums = nums
        self.prefix_sums = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

        print(self.prefix_sums)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)
param_1 = obj.sumRange(0, 2)
print(param_1)


obj = NumArray_2(nums)
param_1 = obj.sumRange(0, 2)
print(param_1)
