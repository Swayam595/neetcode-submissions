class Sets:
    def __init__(self, n: int):
        self.__connected_components = n
        self.__parents = dict()
        self.__rank = dict()

        for i in range(n):
            self.__parents[i] = i
            self.__rank[i] = 1
    
    # TC -> O(α(n))
    # SC -> O(1)
    # α(n) -> inverse Ackermann function (essentially constant)
    # n -> # of nodes
    def find(self, x: int) -> int:
        p = self.__parents[x]

        while p != self.__parents[p]:
            self.__parents[p] = self.__parents[self.__parents[p]]
            p = self.__parents[p]
        
        return p

    # TC -> O(α(n))
    # SC -> O(1)
    # α(n) -> inverse Ackermann function (essentially constant)
    # n -> # of nodes
    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 == p2:
            return True
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__parents[p2] = p1
            self.__rank[p1] += self.__rank[p2]
        else:
            self.__parents[p1] = p2
            self.__rank[p2] += self.__rank[p1]

        self.__connected_components -= 1
        return False

    # TC -> O(1) 
    # SC -> O(1)
    def get_connected_components(self) -> int:
        return self.__connected_components


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # return self.__check_by_dfs(n, edges)
        # return self.__check_by_bfs(n, edges)
        return self.__check_by_union_find(n, edges)

    # TC - O(E * α(n))
    # SC - O(n)
    # α(n) -> inverse Ackermann function (essentially constant)
    # E -> # of edges
    # n -> # of nodes
    def __check_by_union_find(self, n: int, edges: List[List[int]]) -> bool:
        sets = Sets(n)

        for u, v in edges:
            if sets.union(u, v):
                return False
        
        return sets.get_connected_components() == 1
    
    # TC - O(V + E)
    # SC - O(V + E)
    # V -> # of nodes or n
    # E -> # of edges
    def __check_by_bfs(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj_dict = self.__adj_dict_builder(n, edges)
        q = deque()
        q.append([0, -1])
        visited = set()

        while len(q) > 0:
            node, parent = q.popleft()

            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adj_dict[node]:
                if neighbor == parent:
                    continue
                
                q.append([neighbor, node])
        
        return len(visited) == n
    
    # TC - O(V + E)
    # SC - O(V + E)
    # V -> # of nodes or n
    # E -> # of edges
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