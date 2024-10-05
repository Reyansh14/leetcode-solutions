class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity:
        # 𝑂(𝑚 × 𝑛) — We fill up an 𝑚 × 𝑛 matrix, visiting each cell once.
        # Space Complexity:
        # 𝑂(𝑚 × 𝑛) — A 2D array of size 𝑚 × 𝑛 is used to store the number of paths.

        # Create a 2D DP array initialized with 1s
        dp = [[1] * n for _ in range(m)]

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row][col - 1] + dp[row - 1][col]

        return dp[m - 1][n - 1]