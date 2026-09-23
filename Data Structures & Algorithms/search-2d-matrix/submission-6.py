class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        first_last = [[row[0], row[-1]] for row in matrix]
        row = 0

        for i in range(len(first_last)):
            if target <= first_last[i][1] and target >= first_last[i][0]:
                row = i
                break
        else:
            return False
        
        lst = matrix[row]
        l = 0
        r = len(lst) - 1

        while l <= r:
            midpoint = l + (r - l) // 2
            if target > lst[midpoint]:
                l = midpoint + 1
            elif target < lst[midpoint]:
                r = midpoint - 1
            else:
                return True

        return False