class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26 

class PrefixTree:

    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.__root
        for char in word:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()

            node = node.children[idx]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.__root
        for char in word:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                return False
            node = node.children[idx]
        
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.__root

        for char in prefix:
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                return False
                
            node = node.children[idx]
        
        return True
        