class TrieNode:
    def __init__(self, char = None):
        self.char = None
        self.children = dict()
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.is_word = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.__ans = set()
        self.__root = self.__buildTrie(words)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.__search(i, j, board, set(), self.__root, [])
            
        return list(self.__ans)

    
    def __buildTrie(self, words: List[str]) -> Optional(TrieNode):
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        return trie.root
    
    def __search(self, x: int, y: int, board: List[List[str]], 
                seen: set, node: Optional(TrieNode), acc: List) -> None:
        if not self.__isValidIndex(x, y, board, seen):
            return

        char = board[x][y]
        if self.__isVisited(x, y, seen):
            return
        
        if char not in node.children:
            return

        seen.add((x, y))
        acc.append(char)

        self.__addToAnsIfWord(acc, node.children[char])        

        offset = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for x_offset, y_offset in offset:
            x_new = x + x_offset
            y_new = y + y_offset
            self.__search(x_new, y_new,  board, seen, node.children[char], acc)
        
        acc.pop()
        seen.remove((x, y))
        
        return



    def __isValidIndex(self, x: int, y: int, board: List[List[str]], seen: set) -> bool:
        if x == len(board) or y == len(board[0]):
            return False
        
        if x < 0 or y < 0:
            return False

        return True        

    def __isVisited(self, x: int, y: int, seen: set) -> bool:
        return (x, y) in seen

    def __addToAnsIfWord(self, acc: List, node: Optional(TrieNode)) -> None:
        if node.is_word:
            self.__ans.add("".join(acc))

        