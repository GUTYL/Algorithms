from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        length = len(data)
        while i < length:
            j = 7
            while j >= 0 and (data[i] >> j) & 1 == 1:
                j -= 1
            cnt = 7 - j
            if i + cnt > length:
                return False
            if cnt == 1 or cnt > 4:
                return False
            for k in range(i + 1, i + cnt):
                if (data[k] >> 7) & 1 == 1 and (data[k] >> 6) & 1 == 0:
                    continue
                return False
            if cnt == 0:
                i += 1
            else:
                i += cnt
        return True

    def validUtf8_old(self, data: List[int]) -> bool:
        i = 0
        while i < len(data):
            nums = self.get_bin_num(data[i])
            # 计算字节数
            if nums[0] == '0':
                i += 1
                continue
            if nums[:5] == '11110':
                if self.judge(i + 1, 3, data):
                    i += 4
                    continue
                return False

            if nums[:4] == '1110':
                if self.judge(i + 1, 2, data):
                    i += 3
                    continue
                return False
            if nums[:3] == '110':
                if self.judge(i + 1, 1, data):
                    i += 2
                    continue
            return False
        return True

    def get_bin_num(self, num):
        nums = bin(num)[2:]
        if len(nums) < 8:
            append = '0' * (8 - len(nums))
            return append + nums
        return nums

    def judge(self, start, length, data):
        for i in range(start, start + length):
            if i == len(data):
                return False
            if not self.get_bin_num(data[i]).startswith('10'):
                return False
        return True


s = Solution()
print(s.validUtf8([197, 130, 1]))
print(bin(1 << 7))
