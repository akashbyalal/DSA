class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = -float("inf")
        sum = 0

        for n in nums:
            sum += n
            maxSum = max(sum, maxSum)
            if sum < 0: sum = 0
        return maxSum