# Notes: 
# Create a stack and a dict with opening and closing brackets, iterate through the chars in the string s. 
# If opening bracket -> append to stack; if closing bracket and matches the top value in stack -> pop from stack;
# else, if it doesn't match, return false. 
# After iterating, if stack is empty, return true, else return false.

# Space Complexity: O(n)
# Time  Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paretheses = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in paretheses.keys():
                stack.append(char)
            elif char in paretheses.values():
                if stack and (paretheses[stack[-1]] == char):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
