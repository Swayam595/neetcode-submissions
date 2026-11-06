class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # return self.__check_using_dfs(numCourses, prerequisites)
        return self.__check_using_kahns_algo(numCourses, prerequisites)

    # TC - O(V + E)
    # SC - O(V + E)
    # V is the number of courses (numCourses)
    # E is the number of prerequisite pairs (len(prerequisites))
    def __check_using_kahns_algo(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        indegree = [0] * numCourses
        adj_dict = {i: list() for i in range(numCourses)}

        for crs, pre_req in prerequisites:
            adj_dict[crs].append(pre_req)
            indegree[pre_req] += 1
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while len(q) > 0:
            crs = q.popleft()
            finish += 1
            for pre_req in adj_dict[crs]:
                indegree[pre_req] -= 1
                if indegree[pre_req] == 0:
                    q.append(pre_req)
        return finish == numCourses
    

    # TC - O(V + E)
    # SC - O(V + E)
    # V is the number of courses (numCourses)
    # E is the number of prerequisite pairs (len(prerequisites))
    def __check_using_dfs(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0:
            return True

        visited = set()
        current_course_path = set()
        adj_dict = {i: [] for i in range(numCourses)}

        for crs, pre_req in prerequisites:
            adj_dict[crs].append(pre_req)

        for src in range(numCourses):
            if not self.__dfs_helper(src, adj_dict, current_course_path, visited):
                return False
        return True
    
    def __dfs_helper(
        self,
        src: int, 
        adj_dict: dict[int, List],
        current_course_path: set[int],
        visited: set[int]
    ) -> bool:
        if src in current_course_path:
            return False
        
        if src in visited:
            return True
        
        current_course_path.add(src)
        visited.add(src)

        for pre_req in adj_dict[src]:
            if not self.__dfs_helper(pre_req, adj_dict, current_course_path, visited):
                return False
        
        current_course_path.remove(src)
        return True