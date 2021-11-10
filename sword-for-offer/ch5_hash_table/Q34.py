from typing import List


class Solution:
    def is_order(self, word1, word2, order_value):
        i = 0
        while i < len(word1) and i < len(word2):
            ch1 = word1[i]
            ch2 = word2[i]
            if order_value[ch1] > order_value[ch2]:
                return False
            if order_value[ch1] < order_value[ch2]:
                return True
            i += 1
        # 没找到不相同的字母，短单词应该在前面
        return i == len(word1)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_value = {ch: value for value, ch in enumerate(order)}
        for i in range(0, len(words) - 1):
            if not self.is_order(words[i], words[i + 1], order_value):
                return False
        return True

    def is_order_update(self, word1, word2, order_array):
        i = 0
        while i < len(word1) and i < len(word2):
            ch1 = word1[i]
            ch2 = word2[i]
            if order_array[ord(ch1) - ord('a')] > order_array[ord(ch2) - ord('a')]:
                return False
            if order_array[ord(ch1) - ord('a')] < order_array[ord(ch2) - ord('a')]:
                return True
            i += 1
        # 没找到不相同的字母，短单词应该在前面
        return i == len(word1)

    def isAlienSorted_update(self, words: List[str], order: str) -> bool:
        """数组模拟哈希表"""
        order_array = [0] * len(order)
        for index, ch in enumerate(order):
            order_array[ord(ch) - ord('a')] = index
        for i in range(0, len(words) - 1):
            if not self.is_order_update(words[i], words[i + 1], order_array):
                return False
        return True


s = Solution()
print(s.isAlienSorted_update(["hello", "helloh"], "hlabcdefgijkmnopqrstuvwxyz"))
