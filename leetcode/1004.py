from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, num_sum, result = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                num_sum += 1
            if num_sum > k:
                if nums[left] == 0:
                    num_sum -= 1
                left += 1
            result = max(result, right - left + 1)
        return result


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
