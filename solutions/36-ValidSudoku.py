from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """        
        Time Complexity: O(1) - iterate through a 9x9 board once, so it's constant
        Space Complexity: O(1) - using 3 lists of 9 sets each, which is constant space
        
        Args:
            board: 9x9 list of lists representing the Sudoku board.
                  Empty cells are represented by '.' and filled cells contain '1' to '9'
        
        Returns:
            bool: True if the board is valid, False otherwise
        """
        # Initialize sets to keep track of numbers in rows, columns and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Iterate through each cell in the board
        for i in range(9):
            for j in range(9):
                # Skip empty cells
                if board[i][j] == '.':
                    continue
                    
                # Calculate box index (0-8)
                box_idx = (i // 3) * 3 + j // 3
                
                # Get current number
                num = board[i][j]
                
                # Check if number already exists in current row, column or box
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[box_idx]):
                    return False
                
                # Add number to respective sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_idx].add(num)
        
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
