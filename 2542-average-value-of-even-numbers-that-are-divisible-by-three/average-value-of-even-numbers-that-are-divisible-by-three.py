class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count, total = 0, 0
        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                total += n
                count += 1
        return total // count if count else 0