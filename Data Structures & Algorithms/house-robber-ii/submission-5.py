class Solution:
    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i-2]+nums[i])
        return nums[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        