class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [ [] for _ in range(n+1)]

        dic = defaultdict(int)
        for num in nums:
            dic[num] += 1

        for value, count in dic.items():
            freq[count].append(value)
        
        answer = []

        while k > 0:
            ans = freq.pop()
            answer += ans
            k -= len(ans)

        return answer
        

        