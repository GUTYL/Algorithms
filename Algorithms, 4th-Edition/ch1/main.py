from ch1.UnionFind import *


def main_read_file():
    """从文件中读取数据"""
    with open('../algs4-data/largeUF.txt', 'r') as f:
        n = int(f.readline().strip())
        # 1.5.2.1 quick-find算法
        # uf = QuickFind(n)

        # 1.5.2.3 quick-union算法
        # uf = QuickUnion(n)

        # 1.5.2.6 加权quick-union算法
        uf = WeightedQuickUnion(n)
        while i := f.readline():
            p, q = map(int, i.split())
            if uf.connected(p, q):
                continue
            uf.union(p, q)
            # print(f"{p}  {q}")
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
