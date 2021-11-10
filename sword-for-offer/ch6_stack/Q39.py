from typing import List


class Solution:
    def largestRectangleArea_old1(self, heights: List[int]) -> int:
        """暴力法，两重循环遍历所有矩形
        超时，87 / 96 个通过测试用例"""
        largest = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                w = j - i + 1
                h = min(heights[i:j + 1])
                largest = max(largest, w * h)
        return largest

    def recursive(self, heights, start, end):
        if start == end:
            return 0
        if start + 1 == end:
            return heights[start]
        min_index = start
        for i in range(start + 1, end):
            if heights[i] < heights[min_index]:
                min_index = i
        now_area = (end - start) * heights[min_index]
        left_area = self.recursive(heights, start, min_index)
        right_area = self.recursive(heights, min_index + 1, end)
        return max(now_area, left_area, right_area)

    def largestRectangleArea_old2(self, heights: List[int]) -> int:
        """分治法，使用递归
        超时，87 / 96 个通过测试用例
        """
        return self.recursive(tuple(heights), 0, len(heights))

    def largestRectangleArea(self, heights: List[int]) -> int:
        """单调栈优化"""
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        while stack[-1] != -1:
            h = heights[stack.pop()]
            w = len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)
        return max_area
