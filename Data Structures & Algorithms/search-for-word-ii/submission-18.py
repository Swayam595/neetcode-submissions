class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.__root = TrieNode()
    
    def get_root(self) -> TrieNode:
        return self.__root
    
    def insert(self, word: str) -> None:
        curr = self.__root

        for char in word:
            idx = ord(char) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        
        curr.is_word = True
        curr.word = word

class Solution:
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # TC -> O((N * W) + (R * C * 4 ^ L))
    # SC -> O(N * W)
    # N -> len of words list
    # W -> max len of the word in the words list
    # R -> # of rows in the board
    # C -> # of cols in the board
    # L -> At each position, you can explore up to 4 directions, and the
    #      depth of recursion is limited by the longest word length
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.__build_trie(words)

        ans = []
        self.__ROWS = len(board)
        self.__COLS = len(board[0])


        for r in range(self.__ROWS):
            for c in range(self.__COLS):
                self.__search(r, c, trie.get_root(), ans, board)
        
        return ans

    # TC -> O(R * C * 4 ^ L)
    # SC -> O(W)
    # R -> # of rows in the board
    # C -> # of cols in the board
    # W -> Max word length
    # L -> At each position, you can explore up to 4 directions, and the
    #      depth of recursion is limited by the longest word length
    def __search(self, r: int, c: int, root: 'TrieNode', ans: List[str], board: List[List[str]]) -> None:
        if not self.__is_valid_index(r, c) or board[r][c] == '#':
            return
        
        char = board[r][c]
        idx = ord(char) - ord('a')
        node = root.children[idx]

        if node is None:
            return
        
        board[r][c] = "#"
        self.__add_to_ans(node, ans)

        for r_offset, c_offset in self.DIRECTIONS:
            r_new = r + r_offset
            c_new = c + c_offset
            self.__search(r_new, c_new, node, ans, board)
        
        board[r][c] = char

        # if node.is_word:
        #     node.children[idx] = None
        
        return

    def __add_to_ans(self, node: 'TrieNode', ans: List[str]) -> None:
        if node.is_word:
            ans.append(node.word)
            node.is_word = False

    def __is_valid_index(self, r: int, c: int) -> bool:
        return 0 <= r < self.__ROWS and 0 <= c < self.__COLS

    # TC -> O(N * W)
    # SC -> O(N * W)
    # N -> len of words list
    # W -> max len of the word in the words list
    def __build_trie(self, words: List[str]) -> 'Trie':
        trie = Trie()

        for word in words:
            trie.insert(word)
        return trie
        