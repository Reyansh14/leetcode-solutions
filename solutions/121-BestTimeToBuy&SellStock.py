# Notes: 
# example of Sliding Window algorithm - keeps track of left and right pointers. 
# iterate through prices array, keep track of left pointer called currMin. 
# if currProfit > maxProfit, set maxProfit = currProfit. 
# if the right pointer (prices[i]) < left pointer (currMin), set currMin to the right pointer and keep going. 
# at the end, return maxProfit

# Space Complexity: O(n)
# Time  Complexity: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        currMin = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            currProfit = (prices[i] - currMin)
            if (currProfit > maxProfit):
                maxProfit = currProfit
            if (prices[i] < currMin):
                currMin = prices[i]
        return maxProfit
