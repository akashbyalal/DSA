class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if nums[l] == target: return l
        if nums[r] == target: return r
        while l < r:
            k = (l+r)//2
            if nums[k] == target: return k
            elif nums[l] < nums[k]:
                if nums[l] <= target and nums[k] >= target:
                    r = k
                else: l = k + 1
            else:
                if nums[k] <= target and target <= nums[r]: l = k + 1
                else: r = k
        return -1