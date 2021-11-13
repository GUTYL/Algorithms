# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """前序遍历实现序列化 Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 使用'#'代表None，','分割节点
        if not root:
            return '#'
        left_str = self.serialize(root.left)
        right_str = self.serialize(root.right)
        return str(root.val)+','+left_str+','+right_str

    def deserialize(self, data):
        """反序列化 Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        node_str = data.split(',')
        i = [0]
        return self.dfs(node_str, i)

    def dfs(self, node_str, i):
        cur_str = node_str[i[0]]
        i[0] += 1
        if cur_str == '#':
            return None
        node = TreeNode(int(cur_str))
        node.left = self.dfs(node_str, i)
        node.right = self.dfs(node_str, i)
        return node


root = TreeNode(1)

node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node2
root.right = node3
node3.left = node4
node3.right = node5


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))
