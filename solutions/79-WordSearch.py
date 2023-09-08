# Notes: 
# Keep track of visited tiles in the path set. In the dfs function, return true if charIdx reaches len of word; 
# return false if out of bounds, or if char doesn't match current tile, or if tile is in path.

# Time  Complexity: O(n * m * 4^(word.length))
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()

        def dfs(row, col, charIdx):
            if charIdx == len(word):
                return True

            if (row < 0 or col < 0
                or row >= rows or col >= cols
                or word[charIdx] != board[row][col]
                    or (row, col) in path):
                return False

            path.add((row, col))

            result = (dfs(row + 1, col, charIdx + 1) or
                      dfs(row - 1, col, charIdx + 1) or
                      dfs(row, col + 1, charIdx + 1) or
                      dfs(row, col - 1, charIdx + 1))

            path.remove((row, col))

            return result

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
