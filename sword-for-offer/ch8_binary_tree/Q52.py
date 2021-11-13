class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        """递归实现二叉树中序遍历"""
        result = []
        self.inorder_traversal_dfs(root, result)
        root_node = None
        tmp_node = TreeNode()
        for i in range(0, len(result)):
            cur = TreeNode(result[i])
            if root_node is None:
                root_node = cur
            else:
                # 2 tmp_node的右子节点指向当前节点（将当前节点添加到上一节点中）
                tmp_node.right = cur
            # 1 tmp_node指向当前节点（更新）
            tmp_node = cur
        return root_node

    def inorder_traversal_dfs(self, root, result):
        if root:
            self.inorder_traversal_dfs(root.left, result)
            result.append(root.val)
            self.inorder_traversal_dfs(root.right, result)


root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node2
root.right = node3
node3.left = node4
node3.right = node5

s = Solution()
# ans = 281
print(s.increasingBST(root))
