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

    def threeSum_update1(self, nums: List[int]) -> List[List[int]]:
        """先排序，固定数字i，然后在排序数组中查找和为-i的两个数字
        移动指针的时候跳过所有相同的值，以便过滤重复的三元组
        """
        result = []
        if len(nums) < 3:
            return []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            self.twoSum(nums, i, result)
            temp = nums[i]
            while i < len(nums) and nums[i] == temp:
                i += 1

        return result

    def twoSum(self, nums, i, result):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                result.append([nums[i], nums[j], nums[k]])
                temp = nums[j]
                while nums[j] == temp and j < k:
                    j += 1
            elif nums[i] + nums[j] + nums[k] < 0:
                # nums[j] + nums[k] < -nums[i]，需要增大nums[j] + nums[k]的和
                # j 向左移动，增大nums[j]
                j += 1
            else:
                k -= 1


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
