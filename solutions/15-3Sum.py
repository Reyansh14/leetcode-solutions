# Notes: 
# We essentially want a + b + c = 0.
# Sort the array first, making it easy to not get duplicates. Then, we have a for-loop for "a" and we can find "b" & "c" by
# doing Two-Sum II using a left & right pointer. 

# Time  Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    triplets.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return triplets