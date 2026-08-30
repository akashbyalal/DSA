class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []

        hashMap = Counter(nums)
        j = 0
        
        for i in range(3):
            while hashMap[i] > 0:
                nums[j] = i
                hashMap[i] -= 1
                j += 1
        
        return nums


