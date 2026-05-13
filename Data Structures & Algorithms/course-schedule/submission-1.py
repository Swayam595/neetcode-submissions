class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = self.__createAdjList(numCourses, prerequisites)
        top_sort = []

        current_course_path = set()
        visited = set()

        for i in range(numCourses):
            if not self.__dfs(i, adj_list, top_sort, visited, current_course_path):
                return False
        
        return len(top_sort) == numCourses

    
    def __createAdjList(self, numCourses: int, prerequisites: List[List[int]]) -> dict:
        adj_list = dict()

        for i in range(numCourses):
            adj_list[i] = []
        
        for src, dst in prerequisites:
            adj_list[src].append(dst)
        
        return adj_list
    
    def __dfs(self, src: int, adj_list: List[List[int]], top_sort: List, 
                    visited: set, current_course_path: set) -> bool:
        if src in current_course_path:
            return False
        
        if src in visited:
            return True
        
        visited.add(src)
        current_course_path.add(src)

        for neighbor in adj_list[src]:
            if not self.__dfs(neighbor, adj_list, top_sort, visited, current_course_path):
                return False
            
        current_course_path.remove(src)
        top_sort.append(src)
        return True
    