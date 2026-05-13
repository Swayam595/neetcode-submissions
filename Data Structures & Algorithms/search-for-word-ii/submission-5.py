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
        if not board or not board[0] or not words:
            return []

        ans = list()
        root = self.__buildTrie(words)

        self.R, self.C = len(board), len(board[0])

        for i in range(self.R):
            for j in range(self.C):
                if board[i][j] in root.children:
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
    def __search(self, x: int, y: int, board: List[List[str]], parent: TrieNode, ans: List) -> None:
        if not self.__isValidIndex(x, y) or board[x][y] == "#":
            return

        char = board[x][y]

        node = parent.children.get(char)
        if node is None:
            return

        board[x][y] = '#'

        self.__addToAnsIfWord(ans, node)        

        offset = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for x_offset, y_offset in offset:
            x_new = x + x_offset
            y_new = y + y_offset
            self.__search(x_new, y_new,  board, node, ans)
        
        board[x][y] = char
        if not node.children and node.word is None:
            parent.children.pop(char, None)
        
        return

    def __isValidIndex(self, x: int, y: int) -> bool:
        return 0 <= x < self.R and 0 <= y < self.C

    def __addToAnsIfWord(self, ans: List, node: TrieNode) -> None:
        if node.word is not None:
            ans.append(node.word)
            node.word = None

        