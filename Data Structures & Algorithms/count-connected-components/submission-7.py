class Sets:
    def __init__(self, n: int) -> None:
        self.__parents = dict()
        self.__rank = dict()
        self.__connected_components = n

        for i in range(n):
            self.__parents[i] = i
            self.__rank[i] = 1
    
    # TC - O(α(N))
    # SC - O(1)
    # α(N) - inverse Ackermann ≈  which is nearly constant time
    # N - Number of node
    def find(self, x: int) -> int:
        p = self.__parents[x]

        while p != self.__parents[p]:
            self.__parents[p] = self.__parents[self.__parents[p]]
            p = self.__parents[p]
        
        return p
    
    # TC - O(α(N))
    # SC - O(1)
    # α(N) - inverse Ackermann ≈  which is nearly constant time
    # N - Number of nodes
    def union(self, u: int, v: int) -> bool:
        p1 = self.find(u)
        p2 = self.find(v)

        if p1 == p2:
            return True
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__parents[p2] = p1
            self.__rank[p1] += self.__rank[p2]
        else:
            self.__parents[p1] = p2
            self.__rank[p2] += self.__rank[p1]
        self.__connected_components -= 1
        return True
    
    # TC - O(1) SC - O(1)
    def get_connected_components(self) -> int:
        return self.__connected_components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # return self.__count_components_dfs(n, edges)
        # return self.__count_components_bfs(n, edges)
        return self.__count_components_union_find(n, edges)

    # TC - O(N + M * α(N)) ~ O(N + M)
    # SC - O(N)
    # α(N) - inverse Ackermann ≈  which is nearly constant time
    # N - Number of nodes 
    # M - len of edges
    def __count_components_union_find(self, n: int, edges: List[List[int]]) -> int:
        sets = Sets(n)

        for u, v in edges:
            sets.union(u, v)
        
        return sets.get_connected_components()

    # TC - O(V + E)
    # SC - O(V + E)
    # V -> # of nodes or n
    # E -> # of edges
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
        return

    # TC - O(V + E)
    # SC - O(V + E)
    # V -> # of nodes or n
    # E -> # of edges
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