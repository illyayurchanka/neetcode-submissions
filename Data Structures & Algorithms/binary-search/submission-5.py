class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def med_point(l, r):
            return l + (r - l) // 2
        
        i = 0
        j = len(nums) - 1
        med = med_point(i, j)
        if nums[med] == target:
            return med
        count = 0
        while i <= j and count < 10:
            if nums[med] > target:
                j = med - 1
                med = med_point(i, j)
            elif nums[med] < target:
                i = med + 1
                med = med_point(i, j)
            else:
                return med
        return -1
