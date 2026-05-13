class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = dict()
        visited = set()
        path = set()
        top_sort = list()


        for i in range(n):
            adj_list[i] = []
        
        for src, dst in edges:
            adj_list[src].append(dst)
        
        for i in range(n):
            if not self.dfs(i, adj_list, visited, top_sort, path):
                return []
        
        top_sort.reverse()
        return top_sort
    
    def dfs(self, src: int, adj_list: dict, visited: set, top_sort: list, path: set) -> bool:
        if src in visited:
            return True
        
        if src in path:
            return False
        
        path.add(src)

        for neighbor in adj_list[src]:
            if not self.dfs(neighbor, adj_list, visited, top_sort, path):
                return False
        
        top_sort.append(src)

        visited.add(src)
        path.remove(src)

        return True