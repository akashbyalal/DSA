class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1
        if target > nums[r]: return len(nums)
        
        while l < r:
            k = (l+r)//2
            if nums[k] == target: return k
            elif nums[k] > target:
                r = k
                
            else:
                l = k + 1
        return l
                
        