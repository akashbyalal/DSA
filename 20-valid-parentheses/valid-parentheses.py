class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0: return False

        hashMap = {")":"(", "}":"{", "]": "["}
        stack = []

        for i in range(len(s)):
            if s[i] in hashMap:
                if stack and stack[-1] == hashMap[s[i]]:
                    stack.pop()
                else: return False
            else: stack.append(s[i])
        
        return False if stack else True

