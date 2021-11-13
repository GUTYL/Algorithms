class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # 深度优先搜索，前序遍历
        # prev_sum 路径表示数字
        prev_sum = 0
        return self.dfs(root, prev_sum)

    def dfs(self, root, path_sum) -> int:
        if root is None:
            return 0
        path_sum = path_sum * 10 + root.val
        if root.right is None and root.left is None:
            return path_sum
        return self.dfs(root.left, path_sum) + self.dfs(root.right, path_sum)


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
print(s.sumNumbers(root))
