# Efficient Solution:


# Inefficient Solution:
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        matches = []

        def dfs(row, col, charIdx, word, path):
            if charIdx == len(word):
                return True

            if (row < 0 or col < 0
                or row >= rows or col >= cols
                or word[charIdx] != board[row][col]
                    or (row, col) in path):
                return False

            path.add((row, col))

            result = (dfs(row + 1, col, charIdx + 1, word, path) or
                      dfs(row - 1, col, charIdx + 1, word, path) or
                      dfs(row, col + 1, charIdx + 1, word, path) or
                      dfs(row, col - 1, charIdx + 1, word, path))

            path.remove((row, col))

            return result

        for word in words:
            for row in range(rows):
                for col in range(cols):
                    if dfs(row, col, 0, word, set()):
                        matches.append(word)

        return sorted(set(matches))
