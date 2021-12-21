from typing import List


class Solution:
    def exchange1(self, nums: List[int]) -> List[int]:
        j_list, o_list = [], []
        for n in nums:
            if n % 2 == 0:
                o_list.append(n)
            else:
                j_list.append(n)
        return j_list + o_list

    def exchange2(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] % 2 != 0:
                i += 1
            while i < j and nums[j] % 2 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums

    def exchange(self, nums: List[int]) -> List[int]:
        """与运算（&）。奇数&1为1，偶数&1为0"""
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] & 1 == 1:
                i += 1
            while i < j and nums[j] & 1 == 0:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


s = Solution()
print(s.exchange([1, 2, 3, 4]))