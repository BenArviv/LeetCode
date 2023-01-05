'''
    Valid Sudoku:
    
    Determine if a 9x9 Sudoku board is valid.
    Only the filled cells need to be validated according to the following rules:
        1. Each row must contain the digits 1-9 without repetition.
        2. Each column must contain the digits 1-9 without repetition.
        3. Each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    
    Note:
        * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        * Only the filled cells need to be validated according to the mentioned rules.
'''

def isValidSudoku(board: list[list[str]]) -> bool:
    test_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    # Row check
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if not board[i][j] in test_list:
                    return False
                else:
                    index = test_list.index(board[i][j])
                    test_list[index] = "0"
        test_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Reset test list
    
    # Column check
    for j in range(9):
        for i in range(9):
            if board[i][j] != '.':
                if not board[i][j] in test_list:
                    return False
                else:
                    index = test_list.index(board[i][j])
                    test_list[index] = "0"
        test_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Reset test list
    
    # Sub-boxes check
    for n in [0, 3, 6]:
        for i in range(n, n + 2):
            for j in range(0, 3):
                if board[i][j] != '.':
                    if not board[i][j] in test_list:
                        return False
                    else:
                        index = test_list.index(board[i][j])
                        test_list[index] = "0"
        test_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Reset test list

        for i in range(n, n + 3):
            for j in range(3, 6):
                if board[i][j] != '.':
                    if not board[i][j] in test_list:
                        return False
                    else:
                        index = test_list.index(board[i][j])
                        test_list[index] = "0"
        test_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Reset test list

        for i in range(n, n + 3):
            for j in range(6, 9):
                if board[i][j] != '.':
                    if not board[i][j] in test_list:
                        return False
                    else:
                        index = test_list.index(board[i][j])
                        test_list[index] = "0"
        test_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Reset test list

    
        
    return True

# Testing examples
board = [[".",".",".",".","5",".",".","1","."],
         [".","4",".","3",".",".",".",".","."],
         [".",".",".",".",".","3",".",".","1"],
         ["8",".",".",".",".",".",".","2","."],
         [".",".","2",".","7",".",".",".","."],
         [".","1","5",".",".",".",".",".","."],
         [".",".",".",".",".","2",".",".","."],
         [".","2",".","9",".",".",".",".","."],
         [".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board))