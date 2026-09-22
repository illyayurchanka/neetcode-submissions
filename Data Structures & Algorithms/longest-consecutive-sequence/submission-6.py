class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in uniq_nums:
                length = 1
                while num + length in uniq_nums:
                    length += 1
                if length > max_length:
                    max_length = length
        return max_length
                