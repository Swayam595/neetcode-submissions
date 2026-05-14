class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zerosAndOnesCount = self.__countZerosAndOnes(strs)
        
        # return self.__recursive(0, zerosAndOnesCount, m, n)
        return self.__topDown(zerosAndOnesCount, m, n)        

    # TC - O(N * M) 
    #       -> N Size of the strs array
    #       -> M max len binary string in the array
    # SC - O(N * M) 
    #       -> N Size of the strs array
    #       -> M max len binary string in the array
    def __countZerosAndOnes(self, strs: List[str]) -> List[dict]:
        zerosAndOnesCount = [{'1': 0, '0': 0} for _ in range(len(strs))]

        for i, bin_str in enumerate(strs):
            for char in bin_str:
                if char == '1':
                    zerosAndOnesCount[i]['1'] += 1
                else:
                    zerosAndOnesCount[i]['0'] += 1
        return zerosAndOnesCount

    # TC - O(2 ^ N) 
    #       -> N Size of the strs array
    # SC - O(N) -> max recursion tree depth
    def __recursive(self, i: int, zerosAndOnesCount: List[dict], m: int, n: int) -> int:
        if i == len(zerosAndOnesCount):
            return 0

        total_0s = zerosAndOnesCount[i]['0']
        total_1s = zerosAndOnesCount[i]['1']
        take = 0

        if total_0s <= m and total_1s <= n:
            take = 1 + self.__recursive(i + 1, zerosAndOnesCount, m - total_0s, n - total_1s)

        skip = self.__recursive(i + 1, zerosAndOnesCount, m, n)

        return max(take, skip)
    
    def __topDown(self, zerosAndOnesCount: List[dict], m: int, n: int) -> int:
        N = len(zerosAndOnesCount)
        memo = dict()

        return self.__topDownHelper(0, zerosAndOnesCount, memo, m, n)
    
    def __topDownHelper(self, i: int, zerosAndOnesCount: dict, memo: dict, m: int, n: int) -> int:
        if i == len(zerosAndOnesCount):
            return 0
        
        if (i, m, n) in memo:
            return memo[(i, m, n)]

        total_0s = zerosAndOnesCount[i]['0']
        total_1s = zerosAndOnesCount[i]['1']
        
        take = 0
        if total_0s <= m and total_1s <= n:
            take = 1 + self.__topDownHelper(i + 1, zerosAndOnesCount, memo, m - total_0s, n - total_1s)

        
        skip = self.__topDownHelper(i + 1, zerosAndOnesCount, memo, m, n)

        memo[(i, m, n)] = max(take, skip)

        return memo[(i, m, n)]