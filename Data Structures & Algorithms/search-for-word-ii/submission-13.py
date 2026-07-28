class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_word = False
        self.word= ""

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def buildTrie(self, words: List[str]) -> "Trie":
        for word in words:
            self.insertWord(word)
        
        return self.root
    
    def insertWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_word = True
        curr.word = word

class Solution:
    DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        trie_root = Trie().buildTrie(words)

        self.N = len(board)
        self.M = len(board[0])

        for i in range(self.N):
            for j in range(self.M):
                self.__search(i, j, trie_root, ans, board)

        return ans
    
    def __search(self, x: int, y: int, root: "Trie", ans: List[str], board: List[List[str]]) -> None:
        if not self.__isValidIndex(x, y) or board[x][y] == "#":
            return

        char = board[x][y]
        
        node = root.children.get(char, None)
        if node is None:
            return
        
        board[x][y] = "#"
        self.__addToAns(node, ans)

        for x_offset, y_offset in self.DIRECTIONS:
            x_new = x + x_offset
            y_new = y + y_offset

            self.__search(x_new, y_new, node, ans, board)

        board[x][y] = char

        if node.children is not None and node.word is not None and node.is_word:
            node.children.pop(char, None)

        return

    def __isValidIndex(self, i: int, j: int) -> bool:
        return 0 <= i < self.N and 0 <= j < self.M

    def __addToAns(self, node: "Trie", ans: List[str]) -> None:
        if node.word is not None and node.is_word:
            ans.append(node.word)
            is_word = False
            node.word = None