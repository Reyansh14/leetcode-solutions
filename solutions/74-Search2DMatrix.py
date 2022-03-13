# Notes: Iterate through outer array to find an array that potentially has the target; if the target is in this targetArray, return True, else return False
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
