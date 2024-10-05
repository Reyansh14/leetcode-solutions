from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ### Approach 1 - DFS (check for cycles)
        # Time Complexity:
        # 𝑂(𝑉 + 𝐸), where 𝑉 is the number of courses and 𝐸 is the number of prerequisite pairs.
        # Space Complexity:
        # 𝑂(𝑉) due to the recursion stack and the visitSet.

        # # map each course to prereq list (key:course, val:[prereqs])
        # prereqMap = { i:[] for i in range(numCourses) }
        # for course, prereq in prerequisites:
        #     prereqMap[course].append(prereq)


        # # stores all courses along current DFS path
        # visitSet = set()
        # def dfs(course):
        #     if course in visitSet:
        #         return False
        #     if prereqMap[course] == []:
        #         return True

        #     visitSet.add(course)
        #     for prereq in prereqMap[course]:
        #         if not dfs(prereq):
        #             return False
        #     visitSet.remove(course)
        #     prereqMap[course] = [] # don't need to do DFS on it again if it's already processed
        #     return True

        # for course in range(numCourses):
        #     if not dfs(course):
        #         return False
        
        # return True

        ### Approach 2 - BFS (Topological Sort using Kahn's Algorithm)
        # Time Complexity:
        # 𝑂(𝑉 + 𝐸), where 𝑉 is the number of courses and 𝐸 is the number of prerequisite pairs.
        # Space Complexity:
        # 𝑂(𝑉 + 𝐸) for storing the graph and the in-degrees.

        # Step 1: Initialize the graph
        graph = defaultdict(list)  # adjacency list
        in_degree = [0] * numCourses  # in-degree for each course

        # Step 2: Build the graph and calculate in-degree of each node
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # Step 3: Initialize the queue with all nodes having in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        # Step 4: Perform BFS
        visited_courses = 0
        while queue:
            course = queue.popleft()
            visited_courses += 1 # Count each course visited

            # For each neighboring course, reduce its in-degree by 1
            for neighbour in graph[course]:
                in_degree[neighbour] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)

        # If we visited all courses, return True. Otherwise, there's a cycle.
        return visited_courses == numCourses


