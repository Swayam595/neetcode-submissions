class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # return self.__least_interval_brute_force(tasks, n)
        return self.__least_interval_max_heap(tasks, n)

    def __least_interval_max_heap(self, tasks: List[str], n: int) -> int:
        count_dict = dict()
        for task in tasks:
            count_dict[task] = 1 + count_dict.get(task, 0)
        
        max_heap = [-count for count in count_dict.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1
            if not max_heap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append([count, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
            
        return time
        

    def __least_interval_brute_force(self, tasks: List[str], n: int) -> int:
        count = [0] * 26

        for char in tasks:
            count[ord(char) - ord('A')] += 1
        
        arr = []
        for i in range(26):
            if count[i] > 0:
                arr.append([count[i], i])
            
        time = 0
        processed = []

        while len(arr) > 0:
            max_i = -1
            for i in range(len(arr)):
                if all(processed[j] != arr[i][1] for j in range(max(0, time - n), time)):
                    if max_i == -1 or arr[max_i][0] < arr[i][0]:
                        max_i = i
            
            time += 1
            curr = -1

            if max_i != -1:
                curr = arr[max_i][1]
                arr[max_i][0] -= 1
                if arr[max_i][0] == 0:
                    arr.pop(max_i)
            processed.append(curr)
        
        return time