import heapq
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result_dict = defaultdict(int)
        for i in nums:
            result_dict[i] += 1
        min_heap = []
        heapq.heapify(min_heap)
        for num, times in result_dict.items():
            # 数字，次数倒序插入
            if len(min_heap) < k:
                heapq.heappush(min_heap, (times, num))
            elif times > min_heap[0][0]:
                heapq.heapreplace(min_heap,(times, num) )
                # heapq.heappop(min_heap)
                # heapq.heappush(min_heap, (times, num))
        result = []
        for m in min_heap:
            result.append(m[1])
        return result


s = Solution()
print(s.topKFrequent(
    [4, 1, -1, 2, -1, 2, 3], 2))
