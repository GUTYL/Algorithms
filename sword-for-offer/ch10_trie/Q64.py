import string
import string
from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            tree = self.tree

            for w in word:
                tree = tree.setdefault(w, {})
            # 是否是一个完整的单词
            tree["is_word"] = True

    def search(self, searchWord: str) -> bool:
        root = self.tree
        return self.dfs(root, searchWord, 0, 0)

    def dfs(self, root, searchWord, i, edit):
        if root is None:
            return False
        if root.get('is_word') and i == len(searchWord) and edit == 1:
            return True
        if i < len(searchWord) and edit <= 1:
            found = False
            for ch in string.ascii_lowercase:
                if not found:
                    next_exit = edit if ch == searchWord[i] else edit + 1
                    if root.get(ch):
                        found = self.dfs(root.get(ch), searchWord, i + 1, next_exit)
            return found
        return False


s = MagicDictionary()
s.buildDict(["hello", "leetcode"])
print(s.search('hello'))
print(s.search('hhllo'))
print(s.search('hell'))
print(s.search('leetcoded'))
