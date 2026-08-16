# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n

        while l < r:
            k = (l+r)//2

            if isBadVersion(k):
                r = k
            else:
                l = k + 1
        return l