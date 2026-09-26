class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = max(nums)
        if n < len(nums): return len(nums)

        sum = n*(n+1)/2
        summ = 0
        for i in nums:
            summ += i
        return abs(int(summ - sum))