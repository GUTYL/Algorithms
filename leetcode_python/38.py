class Solution:
    def countAndSay(self, n: int) -> str:

        say_str = '1'

        def return_str(s):
            count_num = s[0]
            count_times = 0
            result = ''
            for i in s:
                if count_num == i:
                    count_times += 1
                else:
                    result += str(count_times) + str(count_num)
                    count_num = i
                    count_times = 1
            result += str(count_times) + str(count_num)
            return result

        for i in range(n - 1):
            say_str = return_str(say_str)
        return say_str


s = Solution()
print(s.countAndSay(4))
