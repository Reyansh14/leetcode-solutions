'''
Notes:
For boxes, the formula is box_idx = (i // 3) * 3 + (j // 3).
Dividing the row index i by 3 gives the "row group" the cell belongs to:
- Rows 0, 1, 2 → group 0.
- Rows 3, 4, 5 → group 1.
- Rows 6, 7, 8 → group 2.
Each row group contains 3 sub-boxes horizontally, so we multiply the row 
group index by 3 to shift to the correct sub-box row section. 
Dividing the column index j by 3 gives the position within the current row 
group, like an offset. Then, we just add the two together to get the mapping.

Time Complexity: O(81) = O(1) or O(n^2) if it was an n x n board
Space Complexity: O(81) = O(1) or O(n) if it was an n x n board
'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board)):
                cell = board[i][j]
                if cell == ".":
                    continue

                box_idx = (i // 3) * 3 + (j // 3)

                if cell in rows[i] or cell in cols[j] or cell in boxes[box_idx]:
                    return False

                rows[i].add(cell)
                cols[j].add(cell)
                boxes[box_idx].add(cell)

        return True


def test_valid_sudoku():
    solution = Solution()
    
    # Test Case 1: Valid Sudoku board
    valid_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(valid_board) == True, "Test case 1 failed: Valid board should return True"
    
    # Test Case 2: Invalid Sudoku board (duplicate in row)
    invalid_row_board = [
        ["5","3",".",".","7",".","5",".","."],  # Duplicate 5 in row
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(invalid_row_board) == False, "Test case 2 failed: Board with duplicate in row should return False"
    
    # Test Case 3: Invalid Sudoku board (duplicate in 3x3 box)
    invalid_box_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6","5",".","1","9","5",".",".","."],  # Duplicate 5 in top-middle box
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert solution.isValidSudoku(invalid_box_board) == False, "Test case 3 failed: Board with duplicate in 3x3 box should return False"
    
    print("All test cases passed!")

# Run tests
if __name__ == "__main__":
    test_valid_sudoku()
