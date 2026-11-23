class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # return self.__foreign_dictionary_dfs(words)
        return self.__foreign_dictionary_topological_sort(words)

    def __foreign_dictionary_topological_sort(self, words: List[str]) -> str:
        adj_dict = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in adj_dict}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj_dict[w1[j]]:
                        indegree[w2[j]] += 1
                        adj_dict[w1[j]].add(w2[j])
                    break
        
        return self.__topological_sort_helper(adj_dict, indegree)

    def __topological_sort_helper(self, adj_dict: dict[chr, set], indegree: dict[chr, int]) -> str:
        ans = list()
        seen = set()
        q = deque()
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)

        while len(q) > 0:
            front = q.popleft()
            ans.append(front)
            for neighbor in adj_dict[front]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        if len(ans) != len(indegree):
            return ""

        return "".join(ans)



    # TC -> O(N + V + E)
    # SC -> O(V + E)
    # N -> Total chars in the words list
    # V -> 26 chars in the alien dict
    # E -> # of edges
    def __foreign_dictionary_dfs(self, words: List[str]) -> str:
        adj_dict = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_dict[w1[j]].add(w2[j])
                    break
        
        visited = dict()
        ans = list()

        for char in adj_dict:
            if self.__foreign_dictionary_dfs_helper(char, adj_dict, visited, ans):
                return ""
        
        ans.reverse()
        return "".join(ans)
    
    def __foreign_dictionary_dfs_helper(self, char: chr, adj_dict: dict, visited: dict, ans: List[chr]) -> bool:
        if char in visited:
            return visited[char]
        
        visited[char] = True

        for neighbor in adj_dict[char]:
            if self.__foreign_dictionary_dfs_helper(neighbor, adj_dict, visited, ans):
                return True
        
        visited[char] = False
        ans.append(char)
        return False
        