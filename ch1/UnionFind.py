class UnionFind:
    def __init__(self, n: int):
        self.id = [i for i in range(n)]
        self.count = n

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def find(self, p: int) -> int:
        pass

    def union(self, p: int, q: int):
        pass


if __name__ == '__main__':
    n = int(input())
    uf = UnionFind(n)
    while in_str := input():
        p, q = map(int, in_str.split())
        if uf.connected(p, q):
            continue
        uf.union(p, q)
        print(p + " " + q)
    print(f"{uf.count} components")
