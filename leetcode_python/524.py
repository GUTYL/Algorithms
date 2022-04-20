from typing import List


class Solution:
    class Solution:
        def findLongestWord(self, s: str, dictionary: List[str]) -> str:
            # 将 dictionary 依据字符串长度的降序和字典序的升序进行排序
            dictionary.sort(key=lambda x: (-len(x), x))
            for i in dictionary:
                if self.check(s, i):
                    return i
            return ""

        def check(self, s, sub):
            s_p = 0
            sub_p = 0
            while s_p < len(s) and sub_p < len(sub):
                # 1
                # if s[s_p] == sub[sub_p]:
                #     sub_p += 1
                # s_p += 1

                # 2
                if s[s_p] != sub[sub_p]:
                    s_p += 1
                    continue
                sub_p += 1
                s_p += 1

            if sub_p == len(sub):
                return True
            return False

