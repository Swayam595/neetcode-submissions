class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        return self.__check_by_dfs(n, edges)

    def __check_by_dfs(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj_dict = self.__adj_dict_builder(n, edges)

        visited = set()
        return self.__dfs_helper(0, -1, visited, adj_dict) and len(visited) == n
    
    def __dfs_helper(self, node: int, parent: node, visited: set[int], adj_dict: dict[int, List[int]]) -> bool:
        if node in visited:
            return False
        
        visited.add(node)

        for neighbor in adj_dict[node]:
            if neighbor == parent:
                continue
            
            if not self.__dfs_helper(neighbor, node, visited, adj_dict):
                return False
            
        return True
    
    def __adj_dict_builder(self, n: int, edges: List[List[int]]) -> dict[int, List[int]]:
        adj_dict = {i: list() for i in range(n)}

        for src, dst in edges:
            adj_dict[src].append(dst) 
            adj_dict[dst].append(src)
        
        return adj_dict