# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Notes: Recursive Depth-First Search (DFS) Solution, base cases -> if both nodes are null return true, if both are non-null and same value, return true, else return false. recursively call on left and right subtrees for both p and q.
# Space Complexity: O(p + q)
# Time  Complexity: O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
