from typing import List


class Solution:
    def findMinDifference_old(self, timePoints: List[str]) -> int:
        """排序后比较最小时间差"""
        minutes = []
        for i in timePoints:
            hour, minute = map(int, i.split(':'))
            minutes.append(hour * 60 + minute)
        minutes.sort()
        min_diff = 24 * 60
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        min_diff = min(min_diff, minutes[0] + 24 * 60 - minutes[-1])
        return min_diff

    def findMinDifference(self, timePoints: List[str]) -> int:
        """数组模拟哈希表优化, 1440=24*60"""
        if len(timePoints) > 1440:
            return 0
        minute_flag = [False] * 1440
        for i in timePoints:
            hour, minute = map(int, i.split(':'))
            now_min = hour * 60 + minute
            if minute_flag[now_min]:
                return 0
            minute_flag[now_min] = True
        return self.helper(minute_flag)

    def helper(self, minute_flag):
        min_diff = 1440
        first = min_diff
        last = -1
        prev = -1
