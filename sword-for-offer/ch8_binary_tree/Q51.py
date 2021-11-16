# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = [-sys.maxsize]
        self.postorder_traversal_dfs(root, max_sum)
        return max_sum[0]

    def postorder_traversal_dfs(self, root, max_sum):
        if root is None:
            return 0
        max_sum_left = [-sys.maxsize]
        left = max(0, self.postorder_traversal_dfs(root.left, max_sum_left))

        max_sum_right = [-sys.maxsize]
        right = max(0, self.postorder_traversal_dfs(root.right, max_sum_right))
        max_sum[0] = max(max_sum_left[0], max_sum_right[0], root.val + left + right)

        return root.val + max(left, right)
