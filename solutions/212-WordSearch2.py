# Efficient Solution:
# Notes: Use a trie data structure to store the given words and use back tracking on each tile of the board to see if the given words exist in the board
# Time  Complexity: O(rows*cols*4^(words.length))
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]

        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        matches, visited = set(), set()

        def dfs(row, col, node, word):
            if (row < 0 or col < 0 or
                row == rows or col == cols or
                    (row, col) in visited or board[row][col] not in node.children):
                return

            visited.add((row, col))

            node = node.children[board[row][col]]
            word += board[row][col]
            if node.isWord:
                matches.add(word)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            visited.remove((row, col))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(matches)


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
