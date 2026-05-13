from typing import List, Dict


class UnionFind:
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    # N = number of nodes
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    # Time Complexity: O(α(N)) amortized
    # Space Complexity: O(1)
    # α(N) = inverse Ackermann function (grows extremely slowly, ~ constant)
    def find(self, x: int) -> int:
        p = self.parent[x]

        # Path compression
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        return p

    # Time Complexity: O(α(N)) amortized
    # Space Complexity: O(1)
    def union(self, x1: int, x2: int) -> bool:
        p1 = self.find(x1)
        p2 = self.find(x2)

        if p1 == p2:
            return False

        # Union by rank
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1

        return True


class Solution:
    # Time Complexity:
    # O(E · α(N) + E log E)
    #
    # E = total number of emails
    # N = number of accounts
    # α(N) = inverse Ackermann function (≈ constant)
    #
    # Explanation:
    # - Each email causes at most one union/find → O(E · α(N))
    # - Sorting emails within each merged account → O(E log E)
    #
    # Space Complexity:
    # O(N + E)
    #
    # Explanation:
    # - UnionFind parent & rank arrays → O(N)
    # - Email-to-account mapping → O(E)
    # - Grouped email storage + output → O(E)
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_account: Dict[str, int] = {}

        # Step 1: Union accounts that share the same email
        for account_idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(account_idx, email_to_account[email])
                else:
                    email_to_account[email] = account_idx

        # Step 2: Group emails by their root account
        email_group: Dict[int, List[str]] = {}

        for email, account_idx in email_to_account.items():
            root = uf.find(account_idx)
            if root not in email_group:
                email_group[root] = []
            email_group[root].append(email)

        # Step 3: Build the result
        result = []
        for root, emails in email_group.items():
            username = accounts[root][0]
            result.append([username] + sorted(emails))

        return result
