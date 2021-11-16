# 二叉树的遍历

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorder_traversal_recursion(self, root: TreeNode) -> list:
        """递归实现二叉树中序遍历"""
        result = []
        self.inorder_traversal_dfs(root, result)
        return result

    def inorder_traversal_dfs(self, root, result):
        if root:
            self.inorder_traversal_dfs(root.left, result)
            result.append(root.val)
            self.inorder_traversal_dfs(root.right, result)

    def inorder_traversal_iter(self, root: TreeNode) -> list:
        """迭代，使用栈实现二叉树中序遍历"""
        result = []
        stack = []
        # 当前节点
        cur_node = root
        # 当前节点非空，或栈非空
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                # 获取left节点
                cur_node = cur_node.left
            cur_node = stack.pop()
            result.append(cur_node.val)
            # 获取当前节点的right子节点，如果right子节点为空，将会获取父节点
            cur_node = cur_node.right
        return result

    def preorder_traversal_recursion(self, root: TreeNode) -> list:
        """递归实现二叉树前序遍历"""
        result = []
        self.preorder_traversal_dfs(root, result)
        return result

    def preorder_traversal_dfs(self, root, result):
        if root:
            result.append(root.val)
            self.preorder_traversal_dfs(root.left, result)
            self.preorder_traversal_dfs(root.right, result)

    def preorder_traversal_iter(self, root: TreeNode) -> list:
        """迭代实现二叉树前序遍历"""
        result = []
        stack = []
        # 当前节点
        cur_node = root
        # 当前节点非空，或栈非空
        while cur_node or stack:
            while cur_node:
                result.append(cur_node.val)
                stack.append(cur_node)
                # 获取left节点
                cur_node = cur_node.left
            cur_node = stack.pop()
            # 获取当前节点的right子节点，如果right子节点为空，将会获取父节点
            cur_node = cur_node.right
        return result

    def postorder_traversal_recursion(self, root: TreeNode) -> list:
        """递归实现二叉树后续遍历"""
        result = []
        self.postorder_traversal_dfs(root, result)
        return result

    def postorder_traversal_dfs(self, root, result):
        if root:
            self.postorder_traversal_dfs(root.left, result)
            self.postorder_traversal_dfs(root.right, result)
            result.append(root.val)


    def postorder_traversal_recursion_iter(self, root):
        """迭代实现二叉树后续遍历"""
        result = []
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
                result.append(cur_node.val)
                prev = cur_node
                cur_node = None
        return result

root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

s = Solution()
print("# 中序遍历：")
print(s.inorder_traversal_recursion(root))
print(s.inorder_traversal_iter(root))
print("# 前序遍历：")
print(s.preorder_traversal_recursion(root))
print(s.preorder_traversal_iter(root))
print("# 后序遍历：")
print(s.postorder_traversal_recursion(root))
print(s.postorder_traversal_recursion_iter(root))