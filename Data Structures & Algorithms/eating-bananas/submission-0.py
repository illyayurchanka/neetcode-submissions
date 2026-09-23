class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToEat(k: int, piles: List[int] = piles):
            time = 0
            for p in piles:
                time += math.ceil(float(p) / k)
            return time
        
        l = 1
        r = max(piles)

        res = r

        while l <= r:
            k = l + (r - l) // 2

            time = timeToEat(k)
            if time <= h:
                r = k - 1
                res = k
            else:
                l = k + 1
        return res