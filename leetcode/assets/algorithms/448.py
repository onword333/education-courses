"""448. Find All Numbers Disappeared in an Array"""


class Solution:
    def find_disappeared_numbers_1(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))

    def find_disappeared_numbers_2(self, nums):
        seen=set(nums)
        ans=[]
        for i in range(1,len(nums)+1):
            if i not in seen: ans.append(i)
        return ans


nums = [4, 3, 2, 7, 8, 2, 3, 1]
#nums = [1, 2, 4, 6]
print(Solution().findDisappearedNumbers(nums))
print(Solution().find_disappeared_numbers_2(nums))
