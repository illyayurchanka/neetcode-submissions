class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        res = [0] * length
        i = length - 1
        while i > 0:
            j = i - 1
            while temperatures[i] > temperatures[j] and j >= 0:
                res[j] = i - j
                j -= 1
            i -= 1
        return res