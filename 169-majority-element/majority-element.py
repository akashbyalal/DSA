class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        res = Counter(nums)
        
        for n in nums:
            if res[n] > len(nums)/2: return n
        return -1