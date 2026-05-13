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
    # E is the size of min_heap and V is the lenght of adjacency_list
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjacency_list = dict()
        visited = set()
        max_heap = []

        for i in range(n):
            adjacency_list[i] = []
        
        for i in range(len(edges)):
            s = edges[i][0]
            d = edges[i][1]
            prob = succProb[i]

            adjacency_list[s].append((d, prob))
            adjacency_list[d].append((s, prob))
        
        max_heap.append((-1, start_node))

        while len(max_heap) > 0:
            p1, n1 = heapq.heappop(max_heap)

            if n1 in visited:
                continue

            if n1 == end_node:
                return -p1
            
            visited.add(n1)

            for n2, p2 in adjacency_list[n1]:
                if p2 not in visited:
                    p = p1 * p2
                    heapq.heappush(max_heap, (p, n2))
        
        return 0
