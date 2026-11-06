class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # return self.__find_order_dfs(numCourses, prerequisites)
        return self.__find_order_kahns_algo(numCourses, prerequisites)

    # TC -> O(V + E)
    # SC -> O(V + E)
    # V is the number of courses
    # E is the number of edges or the len of prerequisites
    def __find_order_kahns_algo(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_order = list()
        indegree = [0] * numCourses
        adj_dict = {i: list() for i in range(numCourses)}

        for crs, pre_req in prerequisites:
            adj_dict[crs].append(pre_req)
            indegree[pre_req] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while len(q) > 0:
            crs = q.popleft()
            course_order.append(crs)

            for pre_req in adj_dict[crs]:
                indegree[pre_req] -= 1
                if indegree[pre_req] == 0:
                    q.append(pre_req)

        return course_order[::-1] if len(course_order) == numCourses else []

    # TC -> O(V + E)
    # SC -> O(V + E)
    # V is the number of courses
    # E is the number of edges or the len of prerequisites
    def __find_order_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_order = list()
        current_course_path = set()
        visited = set()
        adj_dict = {i: list() for i in range(numCourses)}

        for crs, pre_req in prerequisites:
            adj_dict[crs].append(pre_req)
        
        for crs in range(numCourses):
            if not self.__dfs_helper(crs, adj_dict, visited, current_course_path, course_order):
                return []
        
        return course_order
    
    def __dfs_helper(
        self,
        src: int, 
        adj_dict: dict[int, list], 
        visited: set[int], 
        current_course_path: set[int],
        course_order: list[int]
    ) -> bool:
        if src in current_course_path:
            return False
        
        if src in visited:
            return True
        
        current_course_path.add(src)
        visited.add(src)

        for neighbor in adj_dict[src]:
            if not self.__dfs_helper(neighbor, adj_dict, visited, current_course_path, course_order):
                return False
        
        course_order.append(src)
        current_course_path.remove(src)
        return True