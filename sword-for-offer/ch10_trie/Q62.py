class TrieOld:

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


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tree = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.tree
        for w in word:
            tree = tree.setdefault(w, {})
        # 是否是一个完整的单词
        tree["is_word"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.tree
        for w in word:
            if w not in tree: return False
            tree = tree[w]
        return tree.get('is_word', False)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.tree
        for ch in prefix:
            if ch not in tree: return False
            tree = tree[ch]
        return True



# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
