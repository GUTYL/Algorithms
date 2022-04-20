# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    node_vals = []

    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    #     stack = []
    #     while root or stack:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()
    #         k -= 1
    #         print(root.val)
    #         if k == 0:
    #             return root.val
    #         root = root.right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dft(root)
        self.node_vals.sort()
        return self.node_vals[k - 1]

    def dft(self, root):
        """中序遍历二叉树"""
        if not root:
            return

        self.node_vals.append(root.val)
        self.dft(root.left)
        self.dft(root.right)


root = TreeNode()
node2 = TreeNode()
node3 = TreeNode()
node4 = TreeNode()
node5 = TreeNode()
node6 = TreeNode()
root.val = 5
root.left = node2

node2.val = 3
node2.left = node3
node3.val = 2
node2.right = node4
node4.val = 4

node3.right = node5
node5.val = 1

root.right = node6
node6.val = 6

s = Solution()
print(s.kthSmallest(root, 3))
print(s.node_vals)
