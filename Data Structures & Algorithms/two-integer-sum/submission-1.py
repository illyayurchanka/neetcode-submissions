class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[target - num] = i
        
        for j, num in enumerate(nums):
            if num in dic:
                i = dic[num]
                if i > j:
                    return [j, i]
                elif i < j:
                    return [i, j]

        