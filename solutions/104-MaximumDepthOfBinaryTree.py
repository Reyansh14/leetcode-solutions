# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Notes: Recursive Depth-First Search (DFS) Solution, base case -> if current node is null, return 0, recursive case -> return 1 + the max between depth of left subtree and depth of right subtree.
# Space Complexity: O(n)
# Time  Complexity: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Notes: Iterative Depth-First Search (DFS) Solution, use pre-order DFS, start at root -> add it to the stack and take its depth (depth = 1 for root), then pop it from the stack and add its left and right children to the stack -> take their depth (depth = 2 now, if it exists), and keep on going
# Space Complexity: O(n)
# Time  Complexity: O(n)
# class Solution:


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result


# Notes: Breadth First Search (BFS) Solution, go level by level in the tree using a deque, pop the current node, and append the left and right nodes to the deque
# Space Complexity: O(n)
# Time  Complexity: O(n)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        level = 0
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return level
