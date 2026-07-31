class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.__checkUsingDfs(numCourses, prerequisites)
    
    # TC - O(V + E)
    # SC - O(V + E)
    # V is the number of courses (numCourses)
    # E is the number of prerequisite pairs (len(prerequisites))
    def __checkUsingDfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        top_sort = list()
        current_course_path = set()
        visited = set()

        adj_list = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        for crs in range(numCourses):
            if not self.__dfsHelper(crs, adj_list, current_course_path, top_sort, visited):
                return False
        
        return True
    
    def __dfsHelper(self, src: int, adj_list: dict, current_course_path: set, top_sort: list, visited: set) -> bool:
        if src in current_course_path:
            return False
        
        if src in visited:
            return True
        
        current_course_path.add(src)
        visited.add(src)

        for pre_req in adj_list[src]:
            if not self.__dfsHelper(pre_req, adj_list, current_course_path, top_sort, visited):
                return False
        
        current_course_path.remove(src)
        top_sort.append(src)

        return True