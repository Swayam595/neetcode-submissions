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

        for i, user_accounts in enumerate(accounts):
            for email in user_accounts[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i
        
        email_group = dict()

        for email, i in email_to_account.items():
            leader = uf.find(i)

            if leader not in email_group:
                email_group[leader] = []
            
            email_group[leader].append(email)
        
        for i, emails in email_group.items():
            name = accounts[i][0]
            ans.append([name] + sorted(emails))
        
        return ans




        