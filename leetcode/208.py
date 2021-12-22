class Trie:

    def __init__(self):
        self.tree = set()

    def insert(self, word: str) -> None:
        self.tree.add(word)

    def search(self, word: str) -> bool:
        return word in self.tree

    def startsWith(self, prefix: str) -> bool:
        index = len(prefix)
        for i in self.tree:
            if prefix == i[:index]:
                return True
        return False


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False



class Trie2:
    # TODO
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True

    def search(self, word) -> 'Trie2':
        pass


word = 'aaa'
obj = Trie2()
obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
