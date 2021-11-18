import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        for i in nums1[:1000]:
            for j in nums2[:1000]:
                min_heap.append([i, j])
        return heapq.nsmallest(k, min_heap, key=lambda x: x[0] + x[1])


s = Solution()
print(s.kSmallestPairs([1, 1, 11], [1, 4, 6], 2))
