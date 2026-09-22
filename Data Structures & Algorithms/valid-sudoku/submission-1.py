class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        columns = [{str(i): 0 for i in range(1, 10, 1)} for _ in range(9)] # j
        rows = [{str(i): 0 for i in range(1, 10, 1)} for _ in range(9)] # i
        square = [{str(i): 0 for i in range(1, 10, 1)} for _ in range(9)] # (row / 3) * 3 + (col / 3)
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                columns[j][num] += 1
                if columns[j][num] > 1:
                    print(columns[j][num])

                    return False

                rows[i][num] += 1
                if rows[i][num] > 1:
                    print("lol1")

                    return False
                
                sq_id = (i // 3) * 3 + (j // 3)
                square[sq_id][num] += 1
                if square[sq_id][num] > 1:
                    print("lol3")
                    return False


        return True