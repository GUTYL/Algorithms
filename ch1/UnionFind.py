class UnionFind:
    def __init__(self, n: int):
        # 分量id
        self._id = [i for i in range(n)]
        # 分量数量
        self._count = n

    def connected_quick_find(self, p: int, q: int) -> bool:
        return self.find_quick_find(p) == self.find_quick_find(q)

    def find_quick_find(self, p: int) -> int:
        return self._id[p]

    def count(self):
        return self._count

    def union_quick_find(self, p: int, q: int):
        p_id = self._id[p]
        q_id = self._id[q]
        if p_id == q_id:
            return
        # 将p的分量重命名为q的名称
        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id
        self._count -= 1


def main_read_file():
    with open('../algs4-data/tinyUF.txt', 'r') as f:
        n = int(f.readline().strip())
        uf = UnionFind(n)
        while i := f.readline():
            p, q = map(int, i.split())
            if uf.connected_quick_find(p, q):
                continue
            uf.union_quick_find(p, q)
            print(f"{p}  {q}")
        print(f"{uf.count()} components")


def main_input():
    n = int(input())
    uf = UnionFind(n)
    while in_str := input():
        p, q = map(int, in_str.split())
        if uf.connected_quick_find(p, q):
            continue
        uf.union_quick_find(p, q)
        print(p + " " + q)
    print(f"{uf.count()} components")


if __name__ == '__main__':
    # quick_find 算法
    main_read_file()
