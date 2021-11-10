from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """排序字符串，构成字典。
        键为排序后的字符串（str），值为原始字符串构成的list，1对多关系。"""
        result_dict = defaultdict(list)
        for i in range(len(strs)):
            sort_i = ''.join(sorted(list(strs[i])))
            result_dict[sort_i].append(strs[i])
        result = []
        for i in result_dict.values():
            result.append(i)
        return result
