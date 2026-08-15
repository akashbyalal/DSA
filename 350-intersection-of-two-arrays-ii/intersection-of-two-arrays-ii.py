class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = Counter(nums2)
        ans = []
        

        for n in nums1:
            if res[n] > 0:
                ans.append(n)
                res[n] -=1
    
            
                
        return ans