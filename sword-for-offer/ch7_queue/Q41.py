from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.window = deque(maxlen=size)
        self.sum_ = 0
        self.size = size

    def next(self, val: int) -> float:
        self.sum_ += val
        if len(self.window) == self.window.maxlen:
            self.sum_ -= self.window.popleft()
        self.window.append(val)
        return self.sum_ / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))
