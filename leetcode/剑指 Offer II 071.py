from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.arr = w
        self.sum = sum(self.arr)

    def pickIndex(self) -> int:
        if len(self.arr) == 1:
            return 0
        from random import randint
        random_index = randint(0, self.sum - 1)
        index = -1
        for i, value in enumerate(self.arr):
            index += value
            if index >= random_index:
                return i


w = [3, 1, 2, 4]
obj = Solution(w)
while True:
    print(obj.pickIndex())
