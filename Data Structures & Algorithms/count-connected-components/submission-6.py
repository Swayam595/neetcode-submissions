class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # return self.__count_components_dfs(n, edges)
        return self.__count_components_bfs(n, edges)
    
    def __count_components_bfs(self, n: int, edges: List[List[int]]) -> int:
        adj_dict = self.__create_adj_dict(n, edges)
        visited = set()
        connected_components = 0

        for i in range(n):
            if i in visited:
                continue
            self.__bfs_helper(i, adj_dict, visited)
            connected_components += 1
        return connected_components

    def __bfs_helper(self, root: int, adj_dict: dict[int, List[int]], visited: set[int]) -> None:
        q = deque()
        q.append(root)

        while len(q) > 0:
            node = q.popleft()

            if node in visited:
                continue
            visited.add(node)

            for neighbor in adj_dict[node]:
                q.append(neighbor)

    def __count_components_dfs(self, n: int, edges: List[List[int]]) -> int:
        adj_dict = self.__create_adj_dict(n, edges)
        visited = set()
        connected_components = 0
        for node in range(n):
            if node in visited:
                continue
            self.__dfs_helper(node, visited, adj_dict)
            connected_components += 1
        
        return connected_components
    
    def __dfs_helper(self, node: int, visited: set[int], adj_dict: dict[int, List[int]]) -> None:
        if node in visited:
            return
        
        visited.add(node)
        for neighbor in adj_dict[node]:
            self.__dfs_helper(neighbor, visited, adj_dict)
        
        return
    
    def __create_adj_dict(self, n: int, edges: List[List[int]]) -> int:
        adj_dict = {i: list() for i in range(n)}

        for u, v in edges:
            adj_dict[u].append(v)
            adj_dict[v].append(u)
        
        return adj_dict