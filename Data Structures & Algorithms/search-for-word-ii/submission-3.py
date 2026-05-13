class TrieNode:
    def __init__(self, char = None):
        self.char = None
        self.children = dict()
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # TC - O(n) SC - O(n)
    # n - len of the word
    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.word = word
        
class Solution:
    # TC - O((n * m) + (N * M * 4^L)) SC - O(L + t)
    # => TC - O(N * M) SC - (N * M)
    # n - len of the largest word
    # m - len of the words array
    # t - number of nodes in the trie which cannot exceed n * m
    # N - Number of Rows in the board
    # M - Number of columns in the board
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = list()
        root = self.__buildTrie(words)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.__search(i, j, board, root, ans)
            
        return ans

    # TC - O(n * m) SC - O(t)
    # n - len of the largest word
    # m - len of the words array
    # t - number of nodes in the trie which cannot exceed n * m
    def __buildTrie(self, words: List[str]) -> TrieNode:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
        
        return trie.root
    
    # TC - O(4 ^ L) SC - O(L)
    # Recursive stack can reach a depth of L
    # L - len of the largest word 
    def __search(self, x: int, y: int, board: List[List[str]], node: TrieNode, ans: List) -> None:
        if not self.__isValidIndex(x, y, board) or board[x][y] == "#":
            return

        char = board[x][y]

        if char not in node.children:
            return
            
        board[x][y] = '#'

        self.__addToAnsIfWord(ans, node.children[char])        

        offset = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for x_offset, y_offset in offset:
            x_new = x + x_offset
            y_new = y + y_offset
            self.__search(x_new, y_new,  board, node.children[char], ans)
        
        board[x][y] = char
        
        return

    def __isValidIndex(self, x: int, y: int, board: List[List[str]]) -> bool:
        if x == len(board) or y == len(board[0]):
            return False
        
        if x < 0 or y < 0:
            return False

        return True        

    def __addToAnsIfWord(self, ans: List, node: TrieNode) -> None:
        if node.word is not None:
            ans.append(node.word)
            node.word = None

        