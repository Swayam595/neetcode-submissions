class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

# TC -> O(W)
# SC -> O(N * L)
# N -> # of words inserted into the trie
# L -> max len of the word
class PrefixTree:

    def __init__(self):
        self.__root = TrieNode()
        
    # TC -> O(W)
    # SC -> O(W)
    # W -> len of the word
    def insert(self, word: str) -> None:
        curr = self.__root

        for char in word:
            i = ord(char) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.is_word = True

    # TC -> O(W)
    # SC -> O(1)
    # W -> len of the word
    def search(self, word: str) -> bool:
        curr = self.__root

        for char in word:
            i = ord(char) - ord('a')
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        
        return curr.is_word
        
    # TC -> O(W)
    # SC -> O(1)
    # W -> len of the word
    def startsWith(self, prefix: str) -> bool:
        curr = self.__root

        for char in prefix:
            i = ord(char) - ord('a')
            if curr.children[i] is None:
                return False
            curr = curr.children[i]
        
        return True
        
        