class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]  #used list comprehension here  |
        boxes=[]                        #                              |
        for i in range(9):              # same thing writen in this  <-- 
            boxes.append(set())         #          format
        for row in range(9):
            for col in range(9):
                num=board[row][col]
                if num == ".":
                    continue           # it will skip blank box
                #box number from (0-8)
                box_number=(row//3)*3+(col//3) # we multipled 3 by row because row skips by 3 
                if num in rows[row]:
                    return False
                if num in cols[col]:
                    return False
                if num in boxes[box_number]:
                    return False
                rows[row].add(num)
                cols[col].add(num)
                boxes[box_number].add(num)
        return True