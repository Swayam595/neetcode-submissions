class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        return self.__foreign_dictionary_dfs(words)

    # TC -> O(N + V + E)
    # SC -> O(V + E)
    # N -> Total chars in the words list
    # V -> 26 chars in the alien dict
    # E -> # of edges
    def __foreign_dictionary_dfs(self, words: List[str]) -> str:
        adj_dict = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_dict[w1[j]].add(w2[j])
                    break
        
        visited = dict()
        ans = []

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