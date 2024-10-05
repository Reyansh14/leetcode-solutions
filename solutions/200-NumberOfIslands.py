from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # ### Approach 1 - BFS
        # Time Complexity:
        # 𝑂(𝑀 × 𝑁), where 𝑀 is the number of rows and 𝑁 is the number of columns.
        # Every cell is visited at most once, either when we start a new BFS or when it is marked as visited.
        #
        # Space Complexity:
        # 𝑂(min(𝑀, 𝑁)) — The space complexity is determined by the queue used in the BFS traversal.
        # In the worst case, the BFS queue can store all the cells of the smallest dimension of the grid (either rows or columns).
        
        # if not grid:
        #     return 0

        # m, n = len(grid), len(grid[0])
        # islands = 0

        # def bfs(row, col):
        #     queue = deque()
        #     queue.append((row, col))
        #     grid[row][col] = '0' # mark visited

        #     while queue:
        #         x, y = queue.popleft()
        #         # Explore neighbors
        #         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        #             new_x, new_y = x + dx, y + dy
        #             if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1':
        #                 queue.append((new_x, new_y))
        #                 grid[new_x][new_y] = '0'  # Mark as visited

        # for row in range(m):
        #     for col in range(n):
        #         if grid[row][col] == '1':
        #             bfs(row, col)
        #             islands += 1                 

        # return islands

        ### Approach 2 - DFS
        # Time Complexity:
        # 𝑂(𝑀 × 𝑁), where 𝑀 is the number of rows and 𝑁 is the number of columns.
        # Every cell is visited at most once during the DFS traversal, either when it is first encountered or when it is marked as visited.

        # Space Complexity:
        # 𝑂(𝑀 × 𝑁) in the worst case due to the recursion stack.
        # The space complexity depends on the maximum depth of the recursion stack, which in the worst case can be 𝑀 × 𝑁 (e.g., a grid filled entirely with land). 
        # However, if the islands are well-separated, the recursion depth will be much smaller, and the space complexity will be lower.
        if not grid:
            return 0

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != '1':
                return

            grid[i][j] = '0' # mark visited
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        m, n = len(grid), len(grid[0])
        islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        return islands