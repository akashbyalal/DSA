class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minPro = maxPro = res = nums[0]

        for n in nums[1:]:
            if n < 0:
                minPro, maxPro = maxPro, minPro
            
            maxPro = max(n, n*maxPro)
            minPro = min(n, n*minPro)
           
            res = max(maxPro, res)
        return res