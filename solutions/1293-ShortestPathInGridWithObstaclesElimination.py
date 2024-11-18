from collections import deque
from typing import List
import heapq

"""
Time Complexity: O(N*M*K) where N,M are grid dimensions and K is number of obstacles that can be eliminated
- Each cell can be visited with different numbers of remaining eliminations (0 to k)
- In worst case, we might need to try each cell with each possible remaining elimination count

Space Complexity: O(N*M*K)
- Visited set stores states of (x, y, remaining_eliminations)
- Queue can contain at most N*M*K states
"""

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        
        # Edge case: already at destination
        if n == 1 and m == 1:
            return 0
        
        # Edge case: eliminate all obstacles if k is large enough and calc manhattan distance
        if k >= sum(sum(row) for row in grid):
            return n + m - 2
        
        queue = deque()
        queue.append((0, 0, 0, k))  # x, y, steps, eliminations left
        visited = set()
        visited.add((0, 0, k))
        
        while queue:
            x, y, steps, elims = queue.popleft()
            
            # Check if we've reached the target
            if (x, y) == (n - 1, m - 1):
                return steps
            
            # Explore neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m:
                    if grid[new_x][new_y] == 1 and elims > 0 and (new_x, new_y, elims - 1) not in visited:
                        queue.append((new_x, new_y, steps + 1, elims - 1))
                        visited.add((new_x, new_y, elims - 1))
                    elif grid[new_x][new_y] == 0 and (new_x, new_y, elims) not in visited:
                        queue.append((new_x, new_y, steps + 1, elims))
                        visited.add((new_x, new_y, elims))
        
        return -1

    def shortestPathAstar(self, grid: List[List[int]], k: int) -> int:
        """
        A* Search implementation using Priority Queue
        Time Complexity: O(N*M*K * log(N*M*K)) due to priority queue operations
        Space Complexity: O(N*M*K) for storing states
        
        The A* approach can be more efficient than BFS in practice because:
        1. Uses Manhattan distance heuristic to guide the search
        2. Explores paths that are more likely to reach the target first
        3. Can find the optimal path while exploring fewer cells
        """
        n, m = len(grid), len(grid[0])
        target = (n-1, m-1)
        
        # Edge cases
        if n == 1 and m == 1:
            return 0
        if k >= sum(sum(row) for row in grid):
            return n + m - 2
            
        # Manhattan distance heuristic
        def manhattan(x: int, y: int) -> int:
            return abs(target[0] - x) + abs(target[1] - y)
        
        # Priority queue: (f_score, steps, x, y, remaining_k)
        # f_score = steps + manhattan_distance (actual + heuristic)
        pq = [(manhattan(0, 0), 0, 0, 0, k)]
        # visited: (x, y, remaining_k) -> steps
        visited = {(0, 0, k): 0}
        
        while pq:
            f, steps, x, y, remain_k = heapq.heappop(pq)
            
            # If this path is longer than what we've seen, skip
            if steps > visited.get((x, y, remain_k), float('inf')):
                continue
                
            # Check if we've reached target
            if (x, y) == target:
                return steps
            
            # Explore neighbors
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < n and 0 <= new_y < m:
                    new_k = remain_k - grid[new_x][new_y]
                    if new_k >= 0:
                        new_steps = steps + 1
                        if new_steps < visited.get((new_x, new_y, new_k), float('inf')):
                            visited[(new_x, new_y, new_k)] = new_steps
                            f_score = new_steps + manhattan(new_x, new_y)
                            heapq.heappush(pq, (f_score, new_steps, new_x, new_y, new_k))
        
        return -1

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    def compare_solutions(grid, k, case_num):
        bfs_result = solution.shortestPath(grid, k)
        astar_result = solution.shortestPathAstar(grid, k)
        print(f"\nTest {case_num}:")
        print(f"BFS result: {bfs_result}")
        print(f"A* result: {astar_result}")
        assert bfs_result == astar_result, f"Results don't match for test {case_num}!"
    
    # Test Case 1: Simple path with one obstacle
    test1 = [[0,0,0],
             [1,1,0],
             [0,0,0]]
    compare_solutions(test1, 1, 1)
    
    # Test Case 2: Need all eliminations
    test2 = [[0,1,1],
             [1,1,1],
             [1,0,0]]
    compare_solutions(test2, 4, 2)
    
    # Test Case 3: No possible path
    test3 = [[0,1,1],
             [1,1,1],
             [1,0,0]]
    compare_solutions(test3, 1, 3)
    
    # Test Case 4: Larger grid
    test4 = [[0,0,0,0,0],
             [1,1,1,1,0],
             [0,0,0,0,0],
             [0,1,1,1,1],
             [0,0,0,0,0]]
    compare_solutions(test4, 2, 4)
