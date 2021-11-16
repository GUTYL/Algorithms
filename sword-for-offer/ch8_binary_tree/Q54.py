# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """两次遍历
        第一次遍历得到二叉树的所有节点之和total
        第二次遍历得到二叉树更新值（total-到目前为止的节点和（不含当前节点））"""
        total = [0]
        self.inorder_traversal_dfs(root, total)
        sum_ = [0]
        self.inorder_traversal_dfs1(root, total, sum_)

        return root

    def inorder_traversal_dfs(self, root, total):
        if root is None:
            return 0
        self.inorder_traversal_dfs(root.left, total)
        total[0] += root.val
        self.inorder_traversal_dfs(root.right, total)
        return total[0]

    def inorder_traversal_dfs1(self, root, total, sum_):
        if root is None:
            return 0
        self.inorder_traversal_dfs1(root.left, total, sum_)
        tmp = root.val
        root.val = total[0] - sum_[0]
        sum_[0] += tmp
        self.inorder_traversal_dfs1(root.right, total, sum_)
        return root.val

    def convertBST_update1(self, root: TreeNode) -> TreeNode:
        """一次颠倒的中序遍历实现"""
        curr_sum = 0
        stack = []
        # 当前节点
        cur_node = root
        # 当前节点非空，或栈非空
        while cur_node or stack:
            while cur_node:
                stack.append(cur_node)
                # 获取left节点
                cur_node = cur_node.right
            cur_node = stack.pop()
            curr_sum += cur_node.val
            cur_node.val = curr_sum
            cur_node = cur_node.left
        return root


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node3.left = node2
node2.left = node1
node3.right = node5
node5.left = node4

s = Solution()
print(s.convertBST(node3))
