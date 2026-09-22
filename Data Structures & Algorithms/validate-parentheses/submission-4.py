class Solution:
    def isValid(self, s: str) -> bool:
        corr = {"[": "]", "{": "}", "(": ")"}
        stack = []
        for c in s:
            if c in corr.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or corr[stack.pop()] != c:
                    return False
        return len(stack) == 0