from collections import deque
from typing import List

"""
Time Complexity: O(N*M) where N and M are the dimensions of the grid
- In worst case, we might need to visit all cells in the grid
- Each cell is visited at most once since we mark visited cells

Space Complexity: O(N*M)
- Queue can contain at most N*M cells in worst case
- No additional visited set needed since we modify input grid
"""

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1

        queue = deque()
        queue.append(((0,0), 1))

        while queue:
            coords, curr_len = queue.popleft()
            if coords == (n - 1, m - 1):
                return curr_len

            directions = [(1,1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
            x, y = coords
            
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if (0 <= new_x < n) and (0 <= new_y < m) and grid[new_x][new_y] != 1:
                    queue.append(((new_x, new_y), curr_len + 1))
                    grid[new_x][new_y] = 1 

        return -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Simple path exists
    test1 = [[0,1,0],[0,0,0],[0,0,0]]
    print("Test 1:", solution.shortestPathBinaryMatrix(test1))  # Expected: 3
    
    # Test Case 2: No path exists
    test2 = [[1,0,0],[0,0,0],[0,0,0]]
    print("Test 2:", solution.shortestPathBinaryMatrix(test2))  # Expected: -1
    
