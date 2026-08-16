class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1

        while l < r:
            k = (l+r)//2

            if arr[k] < arr[k+1]: l = k+1
            else: r = k
        return l