class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        leftMost = [-1] * l
        rightMost = [l] * l
        stack = []
        for i in range(l):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(l - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i, height in enumerate(heights):
            area = (rightMost[i] - leftMost[i] - 1) * height
            max_area = max(max_area, area)
        
        return max_area