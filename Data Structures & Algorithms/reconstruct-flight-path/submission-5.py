class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
            # return self.__find_itinerary_dfs(tickets)
            # return self.__find_itinerary_hierholzer_recursion(tickets)
            return self.__find_itinerary_hierholzer_iterative(tickets)

    def __find_itinerary_hierholzer_iterative(self, tickets: List[List[str]]) -> List[str]:
        adj_dict = dict()

        for src, dst in sorted(tickets)[::-1]:
            if src not in adj_dict:
                adj_dict[src] = list()
            adj_dict[src].append(dst)
        
        ans = []
        stack = ["JFK"]

        while len(stack) > 0:
            curr = stack[-1]
            if curr not in adj_dict or len(adj_dict[curr]) == 0:
                ans.append(stack.pop())
            else:
                stack.append(adj_dict[curr].pop())
        return ans[::-1]

    # TC -> O(E * log(E))
    # SC -> O(2E) ~ O(E) i.e. E for adj_dict and E for recursive stack
    # E -> # of edges/ connecting flights
    def __find_itinerary_hierholzer_recursion(self, tickets: List[List[str]]) -> List[str]:
        adj_dict = dict()
        for src, dst in sorted(tickets)[::-1]:
            if src not in adj_dict:
                adj_dict[src] = list()
            adj_dict[src].append(dst)
        
        ans = []
        self.__find_itinerary_hierholzer_recursion_dfs_helper(adj_dict, "JFK", ans)
        return ans[::-1]
    
    def __find_itinerary_hierholzer_recursion_dfs_helper(self, adj_dict: dict, src: str, ans: List) -> None:
        while src in adj_dict and len(adj_dict[src]) > 0:
            dst = adj_dict[src].pop()
            self.__find_itinerary_hierholzer_recursion_dfs_helper(adj_dict, dst, ans)
        ans.append(src)

    # TLE
    # TC -> O(E * V)
    # SC -> O(E * V)
    # E -> # of edges/ aiports
    # V -> # of vertices/ connecting flights
    def __find_itinerary_dfs(self, tickets: List[List[str]]) -> List[str]:
        adj_dict = {src: list() for src, dst in tickets}
        tickets.sort()

        for src, dst in tickets:
            adj_dict[src].append(dst)

        ans = ["JFK"]
        self.__find_itinerary_dfs_helper(adj_dict, ans, "JFK", len(tickets))
        return ans
    
    def __find_itinerary_dfs_helper(self, adj_dict: dict, ans: List, src: str, n: int) -> bool:
        if len(ans) == n + 1:
            return True
        
        if src not in adj_dict:
            return False
        
        temp = list(adj_dict[src])
        for i, v in enumerate(temp):
            adj_dict[src].pop(i)
            ans.append(v)
            
            if self.__find_itinerary_dfs_helper(adj_dict, ans, v, n):
                return True
            
            adj_dict[src].insert(i, v)
            ans.pop()
        return False