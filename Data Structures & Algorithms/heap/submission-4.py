class MinHeap:
    
    def __init__(self):
        self.__min_heap = [0]

    def push(self, val: int) -> None:
        self.__min_heap.append(val)
        i = len(self.__min_heap) - 1

        while i > 1 and self.__min_heap[i] < self.__min_heap[i // 2]:
            self.__swap(self.__min_heap, i, i // 2)
            i = i // 2

    def pop(self) -> int:
        top = self.__get_top()

        if top == -1:
            return top
        

        if len(self.__min_heap) == 2:
            self.__min_heap.pop()
            return top

        self.__min_heap[1] = self.__min_heap.pop()
        
        i = 1
        self.__percolate_down(self.__min_heap, i)
        return top

    def top(self) -> int:
        return self.__get_top()

    def heapify(self, nums: List[int]) -> None:
        if len(nums) == 0:
            return
            
        nums.append(nums[0])
    
        self.__min_heap = nums

        curr = (len(self.__min_heap) - 1) // 2

        while curr > 0:
            i = curr
            self.__percolate_down(self.__min_heap, i)
            curr = curr - 1
                    
    def __get_top(self):
        top = -1

        if len(self.__min_heap) > 1:
            top = self.__min_heap[1]
            
        return top
    
    def __swap(self, arr, i, j):
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    
    def __percolate_down(self, arr, i):
        while 2 * i < len(arr):
            if (2 * i + 1 < len(arr) and
                arr[2 * i + 1] < arr[2 * i] and
                arr[i] > arr[2 * i + 1]):
                self.__swap(arr, i, 2 * i + 1)
                i = 2 * i + 1
            elif arr[i] > arr[2 * i]:
                self.__swap(arr, i, 2 * i)
                i = 2 * i
            else:
                break