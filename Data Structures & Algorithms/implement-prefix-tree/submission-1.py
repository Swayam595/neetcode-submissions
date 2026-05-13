class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False

class PrefixTree:
    # TC - O(n) SC - O(m * n)
    # n -> len of largest word inserted into the trie
    # m -> total number of words inserted into the trie
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.__root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True


    def search(self, word: str) -> bool:
        node = self.__getTrie(word)

        if node is None or not node.is_word:
            return False
        
        return True

    def startsWith(self, prefix: str) -> bool:
        return self.__getTrie(prefix) is not None
        
    
    def __getTrie(self, string: str) -> Optional(TrieNode):
        curr = self.__root

        for c in string:
            if c not in curr.children:
                return None
            curr = curr.children[c]
        return curr