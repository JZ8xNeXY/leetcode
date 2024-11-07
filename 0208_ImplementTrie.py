class TrieNode:
    def __init__(self):
        self.children = {}  # 子ノードを辞書で管理
        self.is_end_of_word = False  # 単語の終端を示すフラグなな


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

        # Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # 出力: True
print(trie.search("app"))    # 出力: False
print(trie.startsWith("app"))  # 出力: True
trie.insert("app")
print(trie.search("app"))    # 出力: True
