from collections import deque


class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def add_ping(self, t):
        start = t - 3000
        self.counter.append(t)
        while self.counter:
            if self.counter[0] >= start:
                break
            self.counter.popleft()


    def ping(self, t: int) -> int:
        self.add_ping(t)
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
