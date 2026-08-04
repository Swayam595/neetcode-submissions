class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # return self.__dfs(words)
        return self.__kahns_algorithm(words)

    # TC -> O(N + V + E)
    # SC -> O(V + E)
    # N -> Sum of len of all words
    # V -> # of vertices
    # E -> # of edges
    def __kahns_algorithm(self, words: List[str]) -> str:
        ans = []
        adj_map = self.__build_adj_map(words)
        indegree = self.__build_indegree_map(adj_map)

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                char1 = word1[j]
                char2 = word2[j]

                if char1 != char2:
                    if char2 not in adj_map[char1]:
                        adj_map[char1].add(char2)
                        indegree[char2] += 1
                    break
        
        q = self.__build_and_populate_queue(indegree)

        while len(q) > 0:
            char = q.popleft()
            ans.append(char)

            for neighbor in adj_map[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(ans) != len(indegree):
            return ""
        
        return "".join(ans)

    def __build_adj_map(self, words: List[str]) -> dict:
        adj_map = dict()

        for word in words:
            for char in word:
                adj_map[char] = set()
        
        return adj_map

    def __build_indegree_map(self, adj_map: dict) -> dict:
        indegree = dict()

        for char in adj_map:
            indegree[char] = 0
        
        return indegree
    
    def __build_and_populate_queue(self, indegree: dict) -> deque:
        q = deque()

        for char in indegree:
            if indegree[char] == 0:
                q.append(char)
        
        return q

    # TC -> O(N + V + E)
    # SC -> O(V + E)
    # N -> Sum of len of all words
    # V -> # of vertices
    # E -> # of edges
    def __dfs(self, words: List[str]) -> str:
        ans = []
        visited = dict()
        adj_map = self.__build_adj_map(words)

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                char1 = word1[j]
                char2 = word2[j]
                if char1 != char2:
                    adj_map[char1].add(char2)
                    break
        
        for char in adj_map:
            if self.__dfs_helper(char, adj_map, visited, ans):
                return ""

        ans.reverse()
        return "".join(ans)

    def __dfs_helper(self, char: str, adj_map: dict, visited: dict, ans: List) -> bool:
        if char in visited:
            return visited[char]
        
        visited[char] = True

        for neighbor in adj_map[char]:
            if self.__dfs_helper(neighbor, adj_map, visited, ans):
                return True
        
        visited[char] = False
        ans.append(char)

        return False