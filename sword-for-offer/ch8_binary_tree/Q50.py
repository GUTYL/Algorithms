class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:  # 深度优先搜索，前序遍历
        # prev_sum 路径表示数字
        path = 0
        map = {0: 1}
        return self.dfs(root, targetSum, map, path)

    def dfs(self, root, targetSum, map, path) -> int:
        if root is None:
            return 0
        path += root.val
        count = map.get(path - targetSum, 0)
        map[path] = map.get(path, 0) + 1
        count += self.dfs(root.left, targetSum, map, path)
        count += self.dfs(root.right, targetSum, map, path)

        map[path] = map[path] - 1
        return count
