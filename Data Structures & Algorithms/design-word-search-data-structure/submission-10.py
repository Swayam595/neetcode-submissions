class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

# TC -> O(W)
# SC -> O(L + N)
# W -> len of the word
# L -> Max len of the word
# N -> Number of words inserted
class WordDictionary:

    def __init__(self):
        self.__root = TrieNode()

    # TC -> O(W)
    # SC -> O(W)
    # W -> len of the word
    def addWord(self, word: str) -> None:
        curr = self.__root

        for char in word:
            i = ord(char) - ord('a')
            if curr.children[i] is None:
                curr.children[i] = TrieNode()
            
            curr = curr.children[i]
        
        curr.is_word = True

    # TC -> O(W * 26^D)
    # SC -> O(W * 26^D)
    # W -> len of the word
    # D -> # of dots in the word to search
    def search(self, word: str) -> bool:
        return self.__search_helper(word, self.__root, 0)
    
    def __search_helper(self, word: str, node: 'TrieNode', i: int) -> bool:
        if i > len(word):
            return False

        for char in word[i:]:
            if char == '.':
                return self.__serach_all_possible_strings(word, node, i + 1)
        
            idx = ord(char) - ord('a')
            if node.children[idx] is None:
                return False

            node = node.children[idx]
            i += 1

        return node.is_word

    def __serach_all_possible_strings(self, word: str, node: 'TrieNode', i: int) -> bool:
        if i > len(word):
            return False

        for child in node.children:
            if child is not None and self.__search_helper(word, child, i):
                return True
        
        return False


