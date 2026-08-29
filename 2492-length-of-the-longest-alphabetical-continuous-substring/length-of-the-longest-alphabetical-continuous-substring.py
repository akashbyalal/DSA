class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        maxCount = 1
        count = 1
        for i in range(1, len(s)):
            
            if ord(s[i-1]) + 1 == ord(s[i]) : count+=1
            else: count = 1
            maxCount = max(maxCount, count)
        return maxCount