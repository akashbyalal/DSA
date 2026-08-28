class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        d = { ")" : "(", "}": "{", "]":"["}

        for i in s:
            if i in d:
                if stack and stack[-1] == d[i]: stack.pop()
                else : return False
            else: stack.append(i)
        return True if not stack else False