# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """序列化 Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 使用#代表空节点

    def deserialize(self, data):
        """反序列化 Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node2
root.right = node3
node3.left = node4
node4.right = node5


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
