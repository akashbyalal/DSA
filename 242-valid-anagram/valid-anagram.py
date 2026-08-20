class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        res = Counter(s)

        for i in t:
            if i not in res: return False
            if i in res: res[i] -= 1
            if res[i] < 0: return False
        return True
