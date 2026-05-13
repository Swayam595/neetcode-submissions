class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = self.__createAdjList(numCourses, prerequisites)
        courses_completed = set()

        for course in range(numCourses):
            if self.__dfs(course, set(), numCourses, adj_list, courses_completed):
                courses_completed.add(course)
            else:
                break
        
        return len(courses_completed) == numCourses
    
    def __createAdjList(self, numCourses: int, prerequisites: List[List[int]]) -> Dict[int, int]:
        adj_list = dict()

        for i in range(numCourses):
            adj_list[i] = []
        
        for u, v in prerequisites:
            adj_list[u].append(v)
        
        return adj_list
    
    def __dfs(self, course, seen, numCourses, adj_list, courses_completed):
        if len(courses_completed) == numCourses:
            return True
        
        if len(adj_list[course]) == 0:
            return True
        
        if course in seen:
            return False
        
        seen.add(course)

        can_be_completed = True
        for pre_req in adj_list[course]:
            can_be_completed = can_be_completed and self.__dfs(pre_req, 
                                                                seen, 
                                                                numCourses, 
                                                                adj_list, 
                                                                courses_completed)
        
        seen.remove(course)
        return can_be_completed
        