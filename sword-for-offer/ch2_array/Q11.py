from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        sum_ = 0
        max_len = 0
        sum_to_index = {0: -1}
        for i in range(len(nums)):
            sum_ += 1 if nums[i] else -1
            if sum_to_index.get(sum_) is not None:
                max_len = max(max_len, i - sum_to_index.get(sum_))
            else:
                sum_to_index[sum_] = i
        return max_len


s = Solution()
nums = [0, 0, 1]
print(s.findMaxLength(nums))
