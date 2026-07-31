class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return self.__checkUsingDfs(numCourses, prerequisites)
    
    # TC - O(V + E)
    # SC - O(V + E)
    def __checkUsingDfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        taken = set()
        adj_map = {i: [] for i in range(numCourses)}
        for course, pre_req in prerequisites: 
            adj_map[course].append(pre_req)

        for course in range(numCourses):
            if not self.__dfsHelper(course, adj_map, taken):
                return False

        return True
    
    def __dfsHelper(self, course: int, adj_map: dict, taken: set) -> bool:
        if course in taken:
            return False

        if len(adj_map[course]) == 0:
            return True
        
        taken.add(course)
        for pre_req in adj_map[course]:
            if not self.__dfsHelper(pre_req, adj_map, taken):
                return False

        taken.remove(course)
        adj_map[course] = []
        return True