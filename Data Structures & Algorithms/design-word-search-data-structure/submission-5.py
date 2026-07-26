class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.__root = TrieNode()

    # TC - O(N)
    # SC - O(N)
    # N -> len of the word
    def addWord(self, word: str) -> None:
        node = self.__root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        
        node.is_word = True

    # TC -> O(N * 26 ^ d)
    # SC -> O(N)
    # N -> len of word
    # d -> # of dots
    def search(self, word: str) -> bool:
        return self.__searchHelper(word, self.__root, 0)

    def __searchHelper(self, word: str, node: TrieNode, i: int) -> bool:
        if i > len(word): 
            return False

        while i < len(word):
            char = word[i]

            if char == ".":
                return self.__searchWordWithMissingChar(word, node, i + 1)
            elif char not in node.children:
                return False
            
            node = node.children[char]
            i += 1
        
        return node.is_word
                    
    def __searchWordWithMissingChar(self, word: str, node: TrieNode, i: int) -> bool:
        if i > len(word):
            return False
        
        for child in node.children.values():
            if self.__searchHelper(word, child, i):
                return True
        
        return False