class UnionFind:
    def __init__(self, n: int) -> None:
        self.__parent = [i for i in range(n)]
        self.__rank = [0] * n
    
    def find(self, x: int) -> int:
        p = self.__parent[x]

        while p != self.__parent[p]:
            self.__parent[p] = self.__parent[self.__parent[p]]
            p = self.__parent[p]
        
        return p
    
    def union(self, x1: int, x2: int) -> bool:
        p1 = self.find(x1)
        p2 = self.find(x2)

        if p1 == p2:
            return False
        
        if self.__rank[p1] > self.__rank[p2]:
            self.__parent[p2] = p1
            self.__rank[p1] += 1
        else:
            self.__parent[p1] = p2
            self.__rank[p2] += 1
        
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ans = []
        uf = UnionFind(len(accounts))

        email_to_account = dict()

        for curr_user_idx, entry in enumerate(accounts):
            user_name = entry[0]
            emails = entry[1:]
            for email in emails:
                if email in email_to_account:
                    user_last_seen_at = email_to_account[email]
                    uf.union(curr_user_idx, user_last_seen_at)
                else:
                    email_to_account[email] = curr_user_idx
            
        email_group = dict()

        for email, user_idx in email_to_account.items():
            parent_user_idx = uf.find(user_idx)

            if parent_user_idx not in email_group:
                email_group[parent_user_idx] = []

            email_group[parent_user_idx].append(email)
        
        for parent_user_idx, emails in email_group.items():
            username = accounts[parent_user_idx][0]
            ans.append([username] + sorted(emails))
        
        return ans