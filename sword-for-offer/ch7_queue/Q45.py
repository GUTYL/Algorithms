from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        """等价于返回最后一层的第一个节点"""
        # 保存当前层节点
        queue1 = deque()
        # 保存下一层节点
        queue2 = deque()
        queue1.append(root)
        left_value = queue1[0].val
        while queue1:
            # 弹出队列顶部节点
            node = queue1.popleft()
            if node.left is not None:
                queue2.append(node.left)
            if node.right is not None:
                queue2.append(node.right)
            # 当前层已经遍历完，且下一层节点数不为空
            if not queue1 and queue2:
                queue1 = queue2.copy()
                left_value = queue1[0].val
                queue2.clear()
        return left_value

root = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
root.left = node2
root.right = node3
s = Solution()

print(s.findBottomLeftValue(root))