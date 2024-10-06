from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ### Approach 1

        # # Step 1: Calculate the frequency of each task
        # task_counts = Counter(tasks)
        
        # # Step 2: Find the maximum frequency of any task
        # max_freq = max(task_counts.values())
        
        # # Step 3: Count how many tasks have this maximum frequency
        # max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
        
        # # Step 4: Calculate the minimum number of intervals required
        # min_intervals = (max_freq - 1) * (n + 1) + max_freq_count
        
        # # Step 5: Return the maximum of min_intervals and total tasks length
        # return max(min_intervals, len(tasks))

        ### Approach 2 - O(n * m), m = idleTime

        # Step 1: Calculate frequencies of each task
        taskCounts = Counter(tasks)
        
        # Step 2: Create a max heap with negative frequencies (since heapq is a min-heap in python)
        maxHeap = [-cnt for cnt in taskCounts.values()]
        heapq.heapify(maxHeap)

        # Step 3: Queue to keep track of tasks that are in their cooldown period
        cooldownQueue = deque()  # Stores pairs of (-frequency, ready_time)
        
        # Step 4: Track time intervals
        time = 0

        # Step 5: Process tasks until no tasks remain in heap or cooldown queue
        while maxHeap or cooldownQueue:
            time += 1

            # If the heap is not empty, pop the most frequent task
            if maxHeap:
                # Get the most frequent task and decrement its count
                cnt = heapq.heappop(maxHeap) + 1 # +1 cuz it's a negative value
                if cnt != 0: # If there are remaining counts, add to cooldown
                    # Add this task to cooldown with its next available time
                    cooldownQueue.append((cnt, time + n))

            # Check if a task is ready to return from cooldown
            if cooldownQueue and cooldownQueue[0][1] == time:
                heapq.heappush(maxHeap, cooldownQueue.popleft()[0])

        return time


