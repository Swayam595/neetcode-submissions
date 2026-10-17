class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # return self.__least_interval_brute_force(tasks, n)
        # return self.__least_interval_max_heap(tasks, n)
        return self.__least_interval_greedy(tasks, n)
    
    # TC -> O(M)
    # SC -> O(1) since we have at most 26 different characters.
    # M -> # of tasks
    def __least_interval_greedy(self, tasks: List[str], n: int) -> int:
        task_freq = [0] * 26
        for task in tasks:
            task_freq[ord(task) - ord('A')] += 1
        
        task_freq.sort()
        max_f = task_freq[-1]

        idle = (max_f - 1) * n

        time = 0
        for i in range(24, -1, -1):
            idle -= min(max_f - 1, task_freq[i])
        return max(0, idle) + len(tasks)

    # TC -> O(M)
    # SC -> O(1) since we have at most 26 different characters.
    # M -> # of tasks
    def __least_interval_max_heap(self, tasks: List[str], n: int) -> int:
        freq_dict = dict()
        for task in tasks:
            freq_dict[task] = freq_dict.get(task, 0) + 1
        
        max_heap = [-count for count in freq_dict.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while q or max_heap:
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