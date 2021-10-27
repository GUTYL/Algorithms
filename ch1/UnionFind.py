class UnionFind:
    """union-find算法的API及初始化"""

    def __init__(self, n: int):
        # 分量id，初始化，以触点作为索引
        self._id = [i for i in range(n)]
        # 分量数量
        self._count = n

    def connected(self, p: int, q: int) -> bool:
        """如果p和q存在于同一个分量中则返回 True"""
        return self.find(p) == self.find(q)

    def count(self) -> int:
        """连通分量的数量"""
        return self._count

    def find(self, p: int) -> int:
        """p（0到 n-1）所在的分量的标识符"""
        pass

    def union(self, p: int, q: int):
        """在p和q之间添加一条连接"""
        pass


class QuickFind(UnionFind):
    """quick-find算法实现"""

    def find(self, p: int) -> int:
        return self._id[p]

    def union(self, p: int, q: int):
        p_id = self._id[p]
        q_id = self._id[q]
        if p_id == q_id:
            return
        # 将p的分量重命名为q的名称
        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id
        self._count -= 1


class QuickUnion(UnionFind):
    """quick-union算法实现"""

    def find(self, p: int) -> int:
        # 找出分量的名称
        while p != self._id[p]:
            p = self._id[p]
        return p

    def union(self, p: int, q: int):
        # 将p和q的根节点统一
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self._id[p_root] = q_root
        self._count -= 1


class WeightedQuickUnion(UnionFind):
    """加权quick-union算法实现"""

    def __init__(self, n: int):
        super().__init__(n)
        # （由触点索引的）各个根节点所对应的分量的大小
        self._sz = [i for i in range(n)]

    def find(self, p: int) -> int:
        # 跟随链接找到跟节点
        while p != self._id[p]:
            p = self._id[p]
        return p

    def union(self, p: int, q: int):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        # 将小树的根节点连接到大树的根节点
        if self._sz[i] < self._sz[j]:
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]
        self._count -= 1
