class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.__root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.__root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.is_word = True

    def search(self, word: str) -> bool:
        return self.__searchWord(word, self.__root, 0)
    
    def __searchWord(self, word, node, i):
        if i > len(word):
            return False
        
        while i < len(word):
            c = word[i]
            
            if c == '.':
                return self.__searchWordWithMissingChar(word, node.children, i + 1)
            elif c not in node.children:
                return False
            node = node.children[c]
            i += 1
        return node.is_word
    
    def __searchWordWithMissingChar(self, word, children, i):
        if i > len(word):
            return False

        for child_node in children:
            if self.__searchWord(word, children[child_node], i):
                return True
        return False