class SegmentTreeBuilder:
    def __init__(self, total: int, L: int, R: int) -> None:
        self.total = total
        self.left_child = None
        self.right_child = None
        self.L = L
        self.R = R
    
    @staticmethod
    def build(nums: List[int], L: int, R: int) -> SegmentTreeBuilder:
        if L == R:
            return SegmentTreeBuilder(nums[L], L, R)
        
        mid = L + (R -  L) // 2

        root = SegmentTreeBuilder(0, L, R)
        root.left_child = SegmentTreeBuilder.build(nums, L, mid)
        root.right_child = SegmentTreeBuilder.build(nums, mid + 1, R)
        root.total = root.left_child.total + root.right_child.total

        return root
    
    def update(self, index: int, val: int) -> None:
        if self.L == self.R:
            self.total = val
            return
        
        mid = self.L + (self.R - self.L) // 2

        if index > mid:
            self.right_child.update(index, val)
        else:
            self.left_child.update(index, val)
        
        self.total = self.left_child.total + self.right_child.total
    
    def query(self, L: int, R: int) -> int:
        if L == self.L  and R == self.R:
            return self.total
        
        mid = self.L + (self.R - self.L) // 2

        if mid < L:
            return self.right_child.query(L, R)
        elif R <= mid:
            return self.left_child.query(L, R)
        else:
            left_total = self.left_child.query(L, mid)
            right_total = self.right_child.query(mid + 1, R)
            return left_total + right_total


class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.__root = SegmentTreeBuilder.build(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        return self.__root.update(index, val)

    
    def query(self, L: int, R: int) -> int:
        return self.__root.query(L, R)
