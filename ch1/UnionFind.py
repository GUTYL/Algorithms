class QuickFind:
    """quick-find算法实现"""

    def __init__(self, n: int):
        # 分量id
        self._id = [i for i in range(n)]
        # 分量数量
        self._count = n

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def find(self, p: int) -> int:
        return self._id[p]

    def count(self):
        return self._count

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


class QuickUnion:
    """quick-union算法实现"""

    def __init__(self, n: int):
        # 分量id
        self._id = [i for i in range(n)]
        # 分量数量
        self._count = n

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def find(self, p: int) -> int:
        # 找出分量的名称
        while p != self._id[p]:
            p = self._id[p]
        return p

    def count(self):
        return self._count

    def union(self, p: int, q: int):
        # 将p和q的根节点统一
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self._id[p_root] = self._id[q_root]
        self._count -= 1


def main_read_file():
    """从文件中读取数据"""
    with open('../algs4-data/tinyUF.txt', 'r') as f:
        n = int(f.readline().strip())
        # 1.5.2.1 quick-find算法
        # uf = QuickFind(n)

        # 1.5.2.3 quick-union算法
        uf = QuickUnion(n)
        while i := f.readline():
            p, q = map(int, i.split())
            if uf.connected(p, q):
                continue
            uf.union(p, q)
            print(f"{p}  {q}")
        print(f"{uf.count()} components")


def main_input():
    """从输入中获取数据"""
    n = int(input())
    # 1.5.2.1 quick-find算法
    uf = QuickFind(n)
    while in_str := input():
        p, q = map(int, in_str.split())
        if uf.connected(p, q):
            continue
        uf.union(p, q)
        print(f"{p}  {q}")
    print(f"{uf.count()} components")


if __name__ == '__main__':
    main_read_file()
