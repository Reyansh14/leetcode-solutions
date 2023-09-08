# Notes: 
# Printed out the elements of a matrix in spiral order by keeping track of a top, bottom, left, and right pointer 
# and adjusting them as each row/column is read.

# Time  Complexity: O(n * m)
# Space Complexity: O(1) (not counting output array)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        l, r = 0, len(matrix[0])
        up, down = 0, len(matrix)

        while l < r and up < down:
            for i in range(l, r):
                spiral.append(matrix[up][i])
            up += 1

            for i in range(up, down):
                spiral.append(matrix[i][r - 1])
            r -= 1

            if not (l < r and up < down):
                break

            for i in range(r - 1, l - 1, -1):
                spiral.append(matrix[down - 1][i])
            down -= 1

            for i in range(down - 1, up - 1, -1):
                spiral.append(matrix[i][l])
            l += 1

        return spiral
            