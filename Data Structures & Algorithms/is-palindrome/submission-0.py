class Solution:
    def isPalindrome(self, s: str) -> bool:
        fltr = "abcdefghijklmoprstuvwxyz123457890"
        def filt(c):
            return c in fltr
        s = list(''.join(s.lower().split()))
        s = list(filter(filt, s))
        print(s)

        l = len(s)
        for i in range(l // 2):
            j = l - i - 1
            if s[i] != s[j]:
                return False
        return True