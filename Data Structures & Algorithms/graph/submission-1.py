class Graph:
    
    def __init__(self):
        self.__adj_list = dict()

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.__adj_list:
            self.__adj_list[src] = set()
        
        if dst not in self.__adj_list:
            self.__adj_list[dst] = set()
        
        self.__adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.__adj_list and dst in self.__adj_list[src]:
            self.__adj_list[src].remove(dst)
            return True
        else:
            return False


    def hasPath(self, src: int, dst: int) -> bool:
        q = deque()
        visited = set()

        q.append(src)

        while len(q) > 0:
            node = q.popleft()

            if node == dst:
                return True
            
            if node in visited:
                continue
            
            visited.add(node)

            for neighbour in self.__adj_list[node]:
                q.append(neighbour)
        
        return False