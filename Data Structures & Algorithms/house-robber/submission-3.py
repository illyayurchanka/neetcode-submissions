class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        nums[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums) - 3, -1, -1):
            nums[i] = max(nums[i+1], nums[i+2]+nums[i])
        return nums[0]
