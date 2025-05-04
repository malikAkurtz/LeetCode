"""You are given a a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true
"""

def isValidSudoku(board: list[list[str]]) -> bool:
    # check every row for duplicates
    for i in range(0,9):
        nums_in_row = [element for element in board[i] if element != "."]
        if len(nums_in_row) != len(set(nums_in_row)):
            return False
    
    # for every column
    for j in range(0, 9):
        nums_in_col = []
        for i in range(0, 9):
            if board[i][j] != ".":
                nums_in_col.append(board[i][j])
        if len(nums_in_col) != len(set(nums_in_col)):
            return False
    

    
    # for every box, right to left, top to bottom
    for k in range(0,9):
        nums_in_box = set()
        for i in range(0,3):
            for j in range(0, 3):
                row = (k // 3) * 3 + i
                col = (k % 3) * 3 + j
                if board[row][col] == ".":
                    continue
                if board[row][col] in nums_in_box:
                    return False
                nums_in_box.add(board[row][col])
    

    return True


print(isValidSudoku(board = 
[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]))