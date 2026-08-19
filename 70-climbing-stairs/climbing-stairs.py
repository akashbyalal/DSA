class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def fibo(n):
            if n in memo:
                return memo[n]
            else:

                memo[n] =  fibo(n-1) + fibo(n-2)
                return memo[n]
        return fibo(n)
