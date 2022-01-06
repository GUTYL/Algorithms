from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1
        while low != high:
            if numbers[low] + numbers[high] < target:
                low += 1
            elif numbers[low] + numbers[high] > target:
                high -= 1
            else:
                break
        return [low + 1, high + 1]


s = Solution()
print(s.twoSum(numbers=[2, 7, 11, 15], target=9))
