class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        return self.__kahnsAlgorithm(words)

    # TC -> O(N + V + E)
    # SC -> O(V + E)
    # N -> Sum of len of all words
    # V -> # of vertices
    # E -> # of edges
    def __kahnsAlgorithm(self, words: List[str]) -> str:
        ans = []
        adj_map = {char: set() for word in words for char in word}
        indegree = {char: 0 for char in adj_map}

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
                        indegree[char2] += 1
                        adj_map[char1].add(char2)
                    break
        
        q = deque()

        for char in indegree:
            if indegree[char] == 0:
                q.append(char)

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
