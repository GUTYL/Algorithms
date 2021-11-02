from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        dict_s1 = defaultdict(int)
        for i in range(len(s1)):
            dict_s1[s1[i]] += 1
            dict_s1[s2[i]] -= 1
        if any(dict_s1.values()) == 0:
            return True
        for i in range(len(s1), len(s2)):
            dict_s1[s2[i]] -= 1
            dict_s1[s2[i - len(s1)]] += 1
            if any(dict_s1.values()) == 0:
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        dict_s1 = defaultdict(int)
        for i in range(len(s1)):
            dict_s1[s1[i]] += 1
            dict_s1[s2[i]] -= 1
        if not any(dict_s1.values()):
            return True
        for i in range(len(s1), len(s2)):
            dict_s1[s2[i]] -= 1
            dict_s1[s2[i - len(s1)]] += 1
            if not any(dict_s1.values()):
                return True
        return False
