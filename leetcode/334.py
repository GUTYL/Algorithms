from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left_min = [0] * len(nums)
        right_max = [0] * len(nums)

        left_min[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < left_min[i - 1]:
                left_min[i] = nums[i]
            else:
                left_min[i] = left_min[i - 1]

        right_max[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > right_max[i + 1]:
                right_max[i] = nums[i]
            else:
                right_max[i] = right_max[i + 1]

        for i in range(1, len(nums) - 1):
            if left_min[i - 1] < nums[i] < right_max[i + 1]:
                return True
        return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        left_min = [0] * len(nums)
        right_max = [0] * len(nums)

        left_min[0] = nums[0]
        for i in range(1, len(nums)):
            left_min[i] = min(nums[i], left_min[i - 1])

        right_max[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right_max[i] = max(nums[i], right_max[i + 1])

        for i in range(1, len(nums) - 1):
            if left_min[i - 1] < nums[i] < right_max[i + 1]:
                return True
        return False

s = Solution()
print(s.increasingTriplet(nums=[2, 1, 5, 0, 4, 6]))
