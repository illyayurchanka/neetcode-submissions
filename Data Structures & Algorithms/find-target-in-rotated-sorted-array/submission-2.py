class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        fh = nums[0] < target
        min_id = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[mid - 1]:
                min_id = mid
                break
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        def binary_search(l, r, target):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        if min_id > 0:
            if fh:
                l, r = 0, min_id - 1
            else:
                l, r = min_id, len(nums) - 1
            return binary_search(l, r, target)
        elif min_id == 0:
            l, r = 0, len(nums) - 1
            return binary_search(l, r, target)
        else:
            return -1
                