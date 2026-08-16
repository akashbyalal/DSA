class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        seen = defaultdict(list)

        for str in strs:
            sort = tuple(sorted(str))
            seen[sort].append(str)
        for val in seen.values():
            res.append(val)
        return res