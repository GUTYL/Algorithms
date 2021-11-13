# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pruneTree(self, root: TreeNode) -> list:
        if not root:
            return root
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root

    def pruneTree_update(self, root):
        stack = []
        cur_node = root
        prev = None
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack[-1]
            if cur_node.right and cur_node.right != prev:
                cur_node = cur_node.right
            else:
                stack.pop()
                if not root.left and not root.right and root.val == 0:
                    return None
                prev = cur_node
                cur_node = None
        return root