class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = self.__buildAdjList(words)

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            w1_len = len(w1)
            w2_len = len(w2)

            min_len = min(w1_len, w2_len)

            if w1_len > w2_len and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj_list[w1[j]].add(w2[j])
                    break
        
        visited = dict()
        path = []

        for char in adj_list:
            if self.__dfs(char, adj_list, visited, path):
                return ""
        
        path.reverse()
        return "".join(path)


    
    def __buildAdjList(self, words: List[str]) -> dict:
        adj_list = dict()

        for word in words:
            for char in word:
                adj_list[char] = set()
        
        return adj_list

    def __dfs(self, char:str, adj_list: dict, visited: dict, path: list) -> bool:
        if char in visited:
            return visited[char]
        
        visited[char] = True

        for neighbor in adj_list[char]:
            if self.__dfs(neighbor, adj_list, visited, path):
                return True
        
        path.append(char)
        visited[char] = False

        return False
