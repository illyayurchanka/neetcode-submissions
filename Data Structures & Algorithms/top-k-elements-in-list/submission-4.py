class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        distinct_nums = set(nums)

        buckets = { x: 0 for x in distinct_nums }
        for n in nums:
            buckets[n] += 1
        
        keys, values = zip(*sorted(zip(buckets.keys(), buckets.values()), reverse=True))
        res = dict(sorted(buckets.items(), key=lambda item: item[1], reverse=True))
        return list(res)[:k]


        


