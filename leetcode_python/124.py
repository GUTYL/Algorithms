# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_sum = float('-inf')

    def maxPathSum(self, root: TreeNode) -> int:
        self.get_sum(root)
        return self.max_sum

    def get_sum(self, root):
        if not root:
            return 0
        left = max(self.get_sum(root.left), 0)
        right = max(self.get_sum(root.right), 0)
        self.max_sum = max(self.max_sum, left + root.val + right)
        return root.val + max(left, right)
