class Solution:
    def isValid(self, s: str) -> bool:
        corr = {"[": "]", "{": "}", "(": ")"}
        open_br = ["[", "{", "("]
        stack = []
        for c in s:
            if c in open_br:
                stack.append(c)
            else:
                if len(stack) == 0 or corr[stack.pop()] != c:
                    return False
        return len(stack) == 0