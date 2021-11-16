# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """递归中序遍历得到所有val，再遍历得到节点"""
        result = []
        self.inorder_traversal_dfs(root, result)
        for i in range(len(result) - 1):
            if result[i] == p.val:
                return TreeNode(result[i + 1])
        return None

    def inorder_traversal_dfs(self, root, result):
        if root:
            self.inorder_traversal_dfs(root.left, result)
            result.append(root.val)
            self.inorder_traversal_dfs(root.right, result)

    def inorderSuccessor_update1(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """迭代实现中序遍历，返回p节点的下一节点"""
        stack = []
        found = False
        # 当前节点
        cur_node = root
        # 当前节点非空，或栈非空
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            cur_node = stack.pop()
            if found:
                break
            elif p == cur_node:
                found = True
            cur_node = cur_node.right
        return cur_node

    def inorderSuccessor_update2(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        """O(h)复杂度的解法"""
        pass