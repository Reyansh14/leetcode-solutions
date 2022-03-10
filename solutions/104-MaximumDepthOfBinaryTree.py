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
