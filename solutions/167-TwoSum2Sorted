# Notes: 
# Since input array is already sorted, we can just keep 2 pointers (l and r) and adjust l and r based on their sum being
# smaller or larger than the target

# Time  Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l + 1, r + 1]