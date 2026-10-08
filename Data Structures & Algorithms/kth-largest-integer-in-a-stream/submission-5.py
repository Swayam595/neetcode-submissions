class KthLargest:
    # TC -> O(N * log(K))
    # SC -> O(K)
    # N -> len of nums
    # K -> len of the min heap
    def __init__(self, k: int, nums: List[int]):
        self.__k = k
        self.__min_heap = []
        self.__create_heap(nums)

    def add(self, val: int) -> int:
        if len(self.__min_heap) == 0 or len(self.__min_heap) < self.__k:
            heapq.heappush(self.__min_heap, val)
        elif self.__min_heap[0] < val:
            self.__heap_pop_push(val)
        
        return self.__min_heap[0]
    
    def __create_heap(self, nums: List[int]) -> None:
        for num in nums:
            if len(self.__min_heap) < self.__k:
                heapq.heappush(self.__min_heap, num)
            elif self.__min_heap[0] < num:
                self.__heap_pop_push(num)
        print (self.__min_heap)

    def __heap_pop_push(self, val):
        heapq.heappop(self.__min_heap)
        heapq.heappush(self.__min_heap, val)        
