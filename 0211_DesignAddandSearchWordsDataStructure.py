class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j, len(word)):
                char = word[i]

                if char == '.':
                    return any(dfs(i + 1, child) for child in node.children.values())

                elif char in node.children:
                    node = node.children[char]
                else:
                    return False
            return node.is_end_of_word

        return dfs(0, self.root)


obj = WordDictionary()
obj.addWord('word')
param_2 = obj.search('.ord')
print(param_2)
