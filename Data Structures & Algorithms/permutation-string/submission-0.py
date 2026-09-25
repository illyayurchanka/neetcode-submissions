class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        def count_freq(s) -> list:
            abc = [0] * 26
            for c in s:
                abc[ord(c) - ord('a')] += 1
            return abc

        k = len(s1) #window

        s1_freq = count_freq(s1)

        for i in range(len(s2) - k + 1):
            if count_freq(s2[i: i + k]) == s1_freq:
                return True
        else:
            return False
            
