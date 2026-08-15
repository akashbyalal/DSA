class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float('inf')
        l, r = 0, 0
        cur = 0

        while r < len(nums):
            cur += nums[r]

            while cur >= target:
                cur -= nums[l]
                minSize = min(minSize, r - l + 1)
                l += 1
            r += 1
        return minSize if minSize != float('inf') else 0