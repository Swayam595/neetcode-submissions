class Sets:
    def __init__(self, n: int) -> None:
        self.__parents = dict()
        self.__rank = dict()
        self.__connected_components = n

        for i in range(1, n + 1):
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
    # N - Number of node
    def union(self, u: int, v: int) -> None:
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
        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # return self.__dfs(edges)
        # return self.__bfs(edges)
        return self.__union_find(edges)

    # TC -> O(V + (E  * α(V))) ~ O(V + E)
    # α(N) - inverse Ackermann ≈  which is nearly constant time
    # SC -> O(V)
    # E -> Number of edges
    # V -> # of vertices
    def __union_find(self, edges: List[List[int]]) -> List[int]:
        sets = Sets(len(edges))

        for u, v in edges:
            if sets.union(u, v):
                return [u, v]
        
        return []

    # TC -> O(E  * (V + E))
    # SC -> O(V + E)
    # E -> Number of edges
    # V -> # of vertices
    def __bfs(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_dict = {i: list() for i in range(n + 1)}

        for u, v in edges:
            adj_dict[u].append(v)
            adj_dict[v].append(u)
            if self.__bfs_helper(u, adj_dict):
                return [u, v]
        
        return False
    
    # TC -> O(E  * (V + E))
    # SC -> O(V + E)
    # E -> Number of edges
    # V -> # of vertices
    def __bfs_helper(self, root: int, adj_dict: dict[int, List[int]]) -> bool:
        visited = set()
        q = deque()
        q.append([root, -1])

        while len(q) > 0:
            node, par = q.popleft()
            if node in visited:
                return True
            visited.add(node)

            for neighbor in adj_dict[node]:
                if neighbor == par:
                    continue
                q.append([neighbor, node])
        
        return False

    # TC -> O(E  * (V + E))
    # SC -> O(V + E)
    # E -> Number of edges
    # V -> # of vertices
    def __dfs(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj_dict = {i: list() for i in range(n + 1)}

        for u, v in edges:
            adj_dict[u].append(v)
            adj_dict[v].append(u)

            visit = [False] * (n + 1)

            if self.__dfs_helper(u, -1, adj_dict, visit):
                return [u, v]
        
        return []
    
    def __dfs_helper(self, node: int, par: int, adj_dict: dict[int, List[int]], visit: List[bool]) -> bool:
        if visit[node]:
            return True
        
        visit[node] = True

        for neighbor in adj_dict[node]:
            if neighbor == par:
                continue
            if self.__dfs_helper(neighbor, node, adj_dict, visit):
                return True
        return False