class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Time Complexity: O(N x M), where N = amount, M = num of diff coin denominations
        # Space Complexity: O(N)
        
        # Step 1: Create a DP array to store the number of combinations for each amount
        dp = [0] * (amount + 1)
        dp[0] = 1  # There's one way to make up amount 0 (using no coins)

        # Step 2: Iterate over each coin and update the DP array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        # Step 3: Return the number of combinations to make up the given amount
        return dp[amount]