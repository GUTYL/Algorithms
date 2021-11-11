import sys
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        # 保存当前层节点
        queue1 = deque()
        # 保存下一层节点
        queue2 = deque()
        if root:
            queue1.append(root)
        # 保存每层最大值
        result = []
        # 初始化当前层最小值
        max_val = -sys.maxsize
        while queue1:
            # 弹出队列顶部节点
            node = queue1.popleft()
            max_val = max(max_val, node.val)
            if node.left is not None:
                queue2.append(node.left)
            if node.right is not None:
                queue2.append(node.right)
            if not queue1:
                queue1 = queue2.copy()
                # 保存当前层最大值
                result.append(max_val)
                # 重置最小值
                max_val = -sys.maxsize
                queue2.clear()
        return result
