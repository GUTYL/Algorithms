class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        while ans * ans <= x:
            tmp = ans + 1
            if tmp * tmp > x:
                break
            ans = tmp
        return ans

    def mySqrt(self, x: int) -> int:
        """二分优化"""
        low, high = 0, x
        ans = 0
        while low <= high:
            mid = (low + high) >> 1
            tmp = mid * mid
            if tmp <= x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


s = Solution()
print(s.mySqrt(8))
