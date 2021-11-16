import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lens = k
        self.nums = []
        heapq.heapify(self.nums)
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        if len(self.nums) < self.lens:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)
        return self.nums[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)