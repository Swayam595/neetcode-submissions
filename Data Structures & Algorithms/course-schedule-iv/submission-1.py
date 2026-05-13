class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        result = []
        adjList = self.__createAdjList(numCourses, prerequisites)
        
        preReqMap = dict()

        for crs in range(numCourses):
            self.__dfs(crs, adjList, preReqMap)
        
        for dst, src in queries:
            result.append(dst in preReqMap[src])
        
        return result       
        
    def __createAdjList(self, n: int, edges: List[List[int]]) -> dict:
        adjList = dict()
        for i in range(n):
            adjList[i] = []
        
        for dst, src in edges:
            adjList[src].append(dst)
        
        return adjList
    
    def __dfs(self, src: int, adjList: dict, indirectEdgeMap: dict) -> set:
        if src not in indirectEdgeMap:
            indirectEdgeMap[src] = set()

            for neighbor in adjList[src]:
                indirectEdgeMap[src].update(self.__dfs(neighbor, adjList, indirectEdgeMap))
            
            indirectEdgeMap[src].add(src)
        
        return indirectEdgeMap[src]