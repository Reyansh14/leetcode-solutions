# Notes: 
# Iterate through outer array to find an array that potentially has the target; 
# if the target is in this targetArray, return True, else return False

# Space Complexity: O(n)
# Time  Complexity: O(n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetArr = []
        for subArr in matrix:
            if (subArr[0] <= target) and (target <= subArr[-1]):
                if (subArr[0] == target) or (target == subArr[-1]):
                    return True
                else:
                    targetArr = subArr.copy()

        return True if target in targetArr else False


# Notes: 
# Use binary search to find the correct row, and binary search on that correct row,
# to see if the target exists within that subarray.

# Space Complexity: O(log n)
# Time  Complexity: O(log n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows - 1

        while top <= bottom:
            middleRow = (top + bottom) // 2
            print(middleRow, top, bottom)
            if target > matrix[middleRow][-1]:
                top = middleRow + 1
            elif target < matrix[middleRow][0]:
                bottom = middleRow - 1
            else:
                break

        if not (top <= bottom):
            return False

        row = (top + bottom) // 2
        l = 0
        r = cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
