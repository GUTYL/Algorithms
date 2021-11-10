from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[str]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        heights = [0] * len(matrix[0])
        max_area = 0
        for row in matrix:
            for i in range(len(row)):
                if row[i] == '0':
                    heights[i] = 0
                else:
                    heights[i] += 1
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area

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
