# Notes: 
# Use binary search on matrix array to first find the targetRow; if it doesn't give us a targetRow return False.
# Then, if targetRow was found, run binary search again but on targetRow this time to find target and return True if found.
# Else, return False

# Space Complexity: O(1)
# Time  Complexity: O(log(m * n))
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowTop, rowBot = 0, len(matrix) - 1
        targetRow = -1
        while rowTop <= rowBot:
            rowMid = (rowTop + rowBot) // 2
            if matrix[rowMid][0] > target:
                rowBot = rowMid - 1
            elif matrix[rowMid][-1] < target:
                rowTop = rowMid + 1
            else:
                targetRow = rowMid
                break
        if targetRow == -1:
            return False

        targetArr = matrix[targetRow]
        low, high = 0, len(targetArr) - 1
        while low <= high:
            mid = (low + high) // 2
            if targetArr[mid] < target:
                low = mid + 1
            elif targetArr[mid] > target:
                high = mid - 1
            else:
                return True
        return False

