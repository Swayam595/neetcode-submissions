class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = self.__createAdjList(numCourses, prerequisites)
        top_sort = []

        current_course_path = set()
        course_taken = set()

        for i in range(numCourses):
            if not self.__dfs(i, adj_list, top_sort, course_taken, current_course_path):
                return []
        
        return top_sort
    
    def __createAdjList(self, numCourses: int, prerequisites: List[List[int]]) -> dict:
        adj_list = dict()

        for i in range(numCourses):
            adj_list[i] = []
        
        for src, dst in prerequisites:
            adj_list[src].append(dst)
        
        return adj_list
    
    def __dfs(self, src: int, adj_list: dict, top_sort: List[List[int]],
                    visited: set, path: set) -> bool:
        if src in path:
            return False
        
        if src in visited:
            return True
        
        visited.add(src)
        path.add(src)
        
        for neighbor in adj_list[src]:
            if not self.__dfs(neighbor, adj_list, top_sort, visited, path):
                return False
        
        top_sort.append(src)
        path.remove(src)

        return True