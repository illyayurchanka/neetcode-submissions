class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length < 3:
            return 0
        
        left_r = [0] * length
        right_l = [0] * length

        l = 0
        r = 1

        tmp_height = height[0]

        while r < length:
            if height[l] > height[r]:
                left_r[l] = 0
                while height[l] >= height[r] and r < length - 1:
                    left_r[r] = height[l] - height[r]
                    r += 1
                l = r
                r += 1
            else:
                l += 1
                r += 1

        r = length - 1
        l = length - 2
        while l > 0:
            if height[r] >= height[l]:
                right_l[r] = 0
                while height[r] > height[l] and l >= 0:
                    right_l[l] = height[r] - height[l]
                    l -= 1
                r = l
                l -= 1
            else:
                l -= 1
                r -= 1
        return sum([min(rl, lr) for rl, lr in zip(right_l, left_r)])


