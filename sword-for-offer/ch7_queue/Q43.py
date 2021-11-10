from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.search_queue = deque()
        self.search_queue.append(self.root)
        while self.search_queue[0].left is not None and self.search_queue[0].right is not None:
            node = self.search_queue.popleft()
            self.search_queue.append(node.left)
            self.search_queue.append(node.right)

    def insert(self, v: int) -> int:
        add_node = TreeNode(val=v)
        parent = self.search_queue[0]
        if parent.left is None:
            parent.left = add_node
        else:
            parent.right = add_node
            self.search_queue.popleft()
            self.search_queue.append(parent.left)
            self.search_queue.append(parent.right)
        return parent.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
root = TreeNode(1)
obj = CBTInserter(root)
obj.insert(2)
obj.insert(3)
obj.get_root()
