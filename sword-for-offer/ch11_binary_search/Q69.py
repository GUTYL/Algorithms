from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            tmp = arr[mid]
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid - 1] < arr[mid] < arr[mid + 1]:
                left = mid
            elif arr[mid - 1] > arr[mid] > arr[mid + 1]:
                right = mid
