class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        return self.__dijkstra(times, n, k)

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
    # E is the size of min_heap and V is the lenght of adjacency_dict
    def __dijkstra(self, times: List[List[int]], n: int, k: int) -> int:
        min_time_to_signal = 0

        adj_dict = self.__create_adj_dict(times, n)
        min_heap = []
        heapq.heappush(min_heap, [0, k])
        visited = set()
        shortest_path = dict()

        while len(min_heap) > 0:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue

            visited.add(n1)
            shortest_path[n1] = w1

            for n2, w2 in adj_dict[n1]:
                heapq.heappush(min_heap, [w1 + w2, n2])
        
        for i in range(1, n + 1):
            if i not in visited:
                return -1 
            min_time_to_signal = max(min_time_to_signal, shortest_path[i])
        return min_time_to_signal

    def __create_adj_dict(self, times: List[List[int]], n: int) -> dict[int, List[List[int, int]]]:
        adj_dict = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj_dict[u].append([v, w])
        return adj_dict