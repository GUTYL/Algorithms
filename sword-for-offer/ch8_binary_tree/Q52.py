class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        """中序遍历获取所有val列表，再根据列表重新生成树"""
        result = []
        self.inorder_traversal_dfs(root, result)
        # 实现一：
        # root_node = None
        # tmp_node = TreeNode()
        # for i in result:
        #     cur = TreeNode(i)
        #     if root_node is None:
        #         root_node = cur
        #     else:
        #         # 2 tmp_node的右子节点指向当前节点（将当前节点添加到上一节点中）
        #         tmp_node.right = cur
        #     # 1 tmp_node指向当前节点（更新）
        #     tmp_node = cur
        # return root_node

        # 实现二：
        # 初始化root节点
        root_node = TreeNode()
        cur_node = root_node
        for i in result:
            cur_node.right = TreeNode(i)
            cur_node = cur_node.right
        return root_node.right

    def inorder_traversal_dfs(self, root, result):
        if root:
            self.inorder_traversal_dfs(root.left, result)
            result.append(root.val)
            self.inorder_traversal_dfs(root.right, result)

    def increasingBST_update(self, root: TreeNode) -> TreeNode:
        """在中序遍历的过程中改变节点指向，直接得到树"""
        pass


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
print(s.increasingBST(root))
