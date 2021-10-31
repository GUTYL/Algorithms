from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """超出时间限制：315/318个通过测试用例"""
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = sorted([nums[i], nums[j], nums[k]])
                        if tmp in result:
                            pass
                        else:
                            result.append(tmp)
        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
