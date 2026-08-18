class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if len(nums) == 1: return l
        while l<r:
            k = (l+r)//2

            if nums[k] < nums[k+1]: l = k + 1
            else: r = k
        return l