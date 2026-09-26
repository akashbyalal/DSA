class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        res = set()

        for n in nums:
            if n in res: return True
            else: res.add(n)
        return False

