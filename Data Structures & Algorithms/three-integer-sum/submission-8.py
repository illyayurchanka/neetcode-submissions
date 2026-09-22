class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []    
        nums = sorted(nums)
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1 
            r = length - 1
            while l < r:
                if nums[r] + nums[l] + nums[i] > 0:
                    r -= 1
                elif nums[r] + nums[l] + nums[i] < 0:
                    l += 1
                else:
                    ans = [nums[i], nums[l], nums[r]]
                    answer.append(ans)
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1


        return answer

