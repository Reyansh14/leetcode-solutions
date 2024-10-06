# Notes: 
# example of Sliding Window algorithm - keeps track of left and right pointers. 
# initialize l, r pointers at first 2 positions of array.
# while r pointer < len(prices), we check for 2 things:
#  - if price on day r > price on day l, we calculate profit and update currMax if profit > currMax and then increment r
#  - if price on day r < price on day l, we shift l to r's spot because we found a new minima and we want to increment r 
#      so we can keep finiding new maxima to maximize profit
#
# at the end, return maxProfit

# Time  Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ### Approach 1
        # currMax = 0
        # l, r = 0, 1
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         currMax = max(profit, currMax)
        #     else:
        #         l = r
        #     r += 1

        # return currMax

        ### Approach 2
        if len(prices) < 2:
            return 0

        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            profit = price - minPrice

            if profit > maxProfit:
                maxProfit = profit

        return maxProfit
