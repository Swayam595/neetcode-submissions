class Solution:
    # TC - O(E * log V)
    # the size of the min_heap can increase max upto E
    # each operation of adding it to the min_heap will take O(logE)
    # since we will be traversing each edge from the adjacency list to find the shortest path
    # it will take O(E * log E) time
    # we know E = V^2
    # we can make say TC - E * log(V^2)
    #                      = E * 2logV
    #                      TC => O(E * logV)
    # 
    # SC - O(E + V)
    # E is the size of min_heap and V is the len of the shortest_path dict
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjacency_list = dict()
        shortest_path = dict()

        for i in range(n):
            adjacency_list[i] = []

        for s, d, w in edges:
            adjacency_list[s].append((d, w))
        
        min_heap = [(0, src)]

        while len(min_heap) > 0:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in shortest_path:
                continue
            
            shortest_path[n1] = w1

            for n2, w2 in adjacency_list[n1]:
                if n2 not in shortest_path:
                    cost = w1 + w2
                    heapq.heappush(min_heap, (cost, n2))

        for i in range(n):
            if i not in shortest_path:
                shortest_path[i] = -1
        
        return shortest_path