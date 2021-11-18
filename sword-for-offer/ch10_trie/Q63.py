from typing import List


class Trie:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        tree = self.tree
        for w in word:
            tree = tree.setdefault(w, {})
        # 是否是一个完整的单词
        tree["is_word"] = True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = Trie()
        for i in dictionary:
            root.insert(i)
        self.tree = root.tree
        # 判断是否为前缀
        result = []
        for word in sentence.split():
            result.append(self.findPrefix(word))
        return ' '.join(result)

    def findPrefix(self, word):
        node = self.tree
        prefix = ''
        for w in word:
            if node.get('is_word', False) or node.get(w) is None:
                break
            prefix += w
            node = node[w]
        return prefix if node.get('is_word') else word



s = Solution()
print(s.replaceWords(["catt", "cat", "bat", "rat"], sentence="the cattle was rattled by the battery"))
