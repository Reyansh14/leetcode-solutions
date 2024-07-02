# Notes: 
# 
# Time  Complexity: O(n)
# Space Complexity: O(1)
#
# In the first pass, calculate ans[i] to be the product of all elements to the left of element i (aka prefix)
# Update prefix by multiplying by nums[i]
# In the second pass, calculate ans[i] to be the product of prefix (already calculated) and all elements to the right of element i (aka postfix)
# Update postfix by multiplying by nums[i]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans

        
        