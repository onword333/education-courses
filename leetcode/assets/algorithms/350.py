"""
350. Intersection of Two Arrays II
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for n1 in nums1:
            if n1 in nums2:
                res.append(n1)
                nums2.remove(n1)

        return res