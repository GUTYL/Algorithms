class Solution:
    def totalMoney(self, n: int) -> int:
        day = 1
        money = 0
        while day <= n:
            week = (day-1) // 7
            money += week + day - 7 * week
            day += 1
        return money



s = Solution()
print(s.totalMoney(20))
