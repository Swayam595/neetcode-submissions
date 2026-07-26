class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = dict() 

class PrefixTree:

    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.__root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.__root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.__root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True
        