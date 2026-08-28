class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        res = 0
        y = x
        while y != 0:

            num = y % 10
            res = res*10 + num
            y= y // 10
        return x == res