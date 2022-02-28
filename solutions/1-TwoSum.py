# Notes: iterate through nums array, use hash map to check if it contains the difference value (target - value at current index). If it contains the difference value, return array of index of that difference value and current index. Else, map will add that value and index pair to the dictionary (val : index)
# Space Complexity: O(n)
# Time  Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}  # (val : index)
        for i, n in enumerate(nums):
            diff = target - n
            if (diff) in dict:
                return [dict[diff], i]
            dict[n] = i
        return
