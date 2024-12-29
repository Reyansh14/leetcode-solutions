class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Approach #1 Notes:
        We can traverse in reverse order and just use the answer array instead
        of a separate stack to save space by jumping forward to the next candidate
        day for comparison. This lets us skip to the next best day and compresses the
        search space. We also track hottest since there can be no hotter day
        if temp[curr_day] >= hottest, letting us set answer[curr_day] to 0 instantly.

        Time Complexity: O(n)
        Space Complexity: O(1), not counting answer array
        '''
        n = len(temperatures)
        answer = [0 for _ in range(n)]
        hottest = 0

        for curr_day in range(n - 1, -1, -1):
            curr_temp = temperatures[curr_day]
            if curr_temp >= hottest:
                hottest = curr_temp
                continue
            
            days = 1
            while temperatures[curr_day + days] <= curr_temp:
                # Use the info in the answer array to skip unnecessary comparisons
                days += answer[curr_day + days]
            answer[curr_day] = days

        return answer
        
        '''
        Approach #2 Notes:

        Time Complexity: O(n)
        Space Complexity: O(n)
        '''

        n = len(temperatures)
        answer = [0] * n
        stack = [] # stack to hold indices of temperatures

        for i in range(n):
            # while stack is not empty and the current temperature is greater than the temperature
            # at the index stored at the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pop_index = stack.pop()
                answer[pop_index] = i - pop_index # calculate days until warmer temperature
            
            stack.append(i) # push the current day's index onto the stack

        return answer