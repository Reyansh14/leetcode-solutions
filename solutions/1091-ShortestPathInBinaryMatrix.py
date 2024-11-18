class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1

        queue = deque()
        queue.append(((0,0), 1))

        while queue:
            coords, curr_len = queue.popleft()
            if coords == (n - 1, m - 1):
                return curr_len

            directions = [(1,1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
            x, y = coords
            
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if (0 <= new_x < n) and (0 <= new_y < m) and grid[new_x][new_y] != 1:
                    queue.append(((new_x, new_y), curr_len + 1))
                    grid[new_x][new_y] = 1 

        return -1

