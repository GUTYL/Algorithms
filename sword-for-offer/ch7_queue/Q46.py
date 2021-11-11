from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """等价于返回每一次最后一个节点
        使用两个队列实现"""
        if root is None:
            return []
        # 保存当前层节点
        queue1 = deque()
        # 保存下一层节点
        queue2 = deque()
        queue1.append(root)
        result = []
        while queue1:
            # 弹出队列顶部节点
            node = queue1.popleft()
            # 如果当前层为空
            if not queue1:
                result.append(node.val)
            if node.left is not None:
                queue2.append(node.left)
            if node.right is not None:
                queue2.append(node.right)
            # 当前层已经遍历完，且下一层节点数不为空
            if not queue1 and queue2:
                queue1 = queue2.copy()
                queue2.clear()
        return result

    def rightSideView_update1(self, root: TreeNode) -> List[int]:
        """等价于返回每一次最后一个节点
        使用一个队列实现"""
        if root is None:
            return []
        # 保存当前层节点
        queue1 = deque()
        queue1.append(root)
        # 记录当前遍历这一层中位于队列之中的节点数目
        current = 1
        # 记录下一层中位于队列之中的节点数目
        next_ = 0
        result = []
        while queue1:
            # 弹出队列顶部节点
            node = queue1.popleft()
            current -= 1
            if node.left is not None:
                queue1.append(node.left)
                next_ += 1
            if node.right is not None:
                queue1.append(node.right)
                next_ += 1
            # 遍历这一层中位于队列之中的节点数目为0，node即为当前层的最后一个结点
            if current == 0:
                result.append(node.val)
                current = next_
                next_ = 0
        return result


root = TreeNode(2)
node2 = TreeNode(1)
node3 = TreeNode(3)
root.left = node2
root.right = node3
s = Solution()

print(s.rightSideView_update1(root))
