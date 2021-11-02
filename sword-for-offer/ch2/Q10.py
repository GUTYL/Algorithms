from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """两重循环获取全部子数组，求和
        超出时间限制：72/89个通过测试用例
        """
        result = 0
        for left in range(len(nums)):
            sum_ = 0
            for right in range(left, len(nums)):
                sum_ += nums[right]
                if sum_ == k:
                    result += 1
        return result

    def subarraySum_update1(self, nums: List[int], k: int) -> int:
        """使用累加数组数字更新
        """
        sum_to_count = {}
        sum_to_count[0] = 1
        sum_ = 0
        count = 0
        for num in nums:
            sum_ += num
            count += sum_to_count.get(sum_ - k, 0)
            sum_to_count[sum_] = sum_to_count.get(sum_, 0) + 1
        return count


s = Solution()
print(s.subarraySum_update1([1, 2, 3], 3))
