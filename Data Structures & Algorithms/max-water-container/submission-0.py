class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        
        def get_area(l, r):
            l_height = heights[l]
            r_height = heights[r]
            return min(l_height, r_height) * (r - l)
        
        max_area = get_area(l, r)

        while l < r:
            if heights[l] > heights[r]:
                r -= 1
                max_area = max(max_area, get_area(l, r))
            else:
                l += 1
                max_area = max(max_area, get_area(l, r))
        
        return max_area


        