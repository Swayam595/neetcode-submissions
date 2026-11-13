class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        return self.__bfs1(beginWord, endWord, wordList)
        # return self.__bfs2_meet_at_end(beginWord, endWord, wordList)

    # TC -> O(N * M ^ 2)
    # Breakdown:
    #   - O(N) to create word_set
    #   - O(N * M^2) for BFS: Process N words, for each word:
    #     * Loop M positions
    #     * Loop 26 characters
    #     * Create new word: O(M)
    #     * Check in word_set: O(M) for string comparison
    #   - Total: N * (M * 26 * M) = N * M^2
    #
    # SC -> O(N * M)
    # Breakdown:
    #   - O(N * M) for word_set: stores N words of length M
    #   - O(N * M) for from_begin dict: max N words as keys
    #   - O(N * M) for from_end dict: max N words as keys
    #   - O(N) for qb and qe queues (negligible compared to dicts)
    #   - Total: O(N * M) dominated space
    #
    # N -> len of word_list
    # M -> len of word in the word_list
    def __bfs2_meet_at_end(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        word_set = set(word_list)  # O(N * M) space
        m = len(word_list[0])
        qb, qe = deque([begin_word]), deque([end_word])  # O(1) initially
        from_begin, from_end = {begin_word: 1}, {end_word: 1}  # O(N * M) space
    
        # Bidirectional BFS: Process smaller queue first for optimization
        while qb and qe:
            # Optimize: always expand from smaller frontier
            if len(qb) > len(qe):
                qb, qe = qe, qb
                from_begin, from_end = from_end, from_begin

            # Process one level of BFS - O(N * M^2) total across all iterations
            for _ in range(len(qb)):
                word = qb.popleft()
                steps = from_begin[word]
                
                # Try changing each position: O(M)
                for i in range(m):
                    # Try each letter a-z: O(26) = O(1)
                    for c in range(ord('a'), ord('z') + 1):
                        if chr(c) == word[i]:
                            continue
                        
                        # Create new word: O(M) for string concatenation
                        new_word = word[:i] + chr(c) + word[i + 1:]
                        
                        # Check if word exists: O(1) dict lookup (word comparison ~O(M))
                        if new_word not in word_set:
                            continue
                        
                        # Found end word from other side - return immediately
                        if new_word in from_end:
                            return steps + from_end[new_word]
                        
                        # Add to visited and queue: O(1) operations
                        if new_word not in from_begin:
                            from_begin[new_word] = steps + 1
                            qb.append(new_word)
        
        return 0

    # TC -> O(N^2 * M)
    # Breakdown:
    #   - O(N) to create word_map: single pass
    #   - O(N^2 * M) to build adj_list: Compare all N^2 pairs, each comparison O(M)
    #   - O(M) to generate neighbors from beginWord
    #   - O(N^2) for BFS: worst case visit all N words with N^2 total edges
    #   - Total: N^2*M dominates
    #
    # SC -> O(N^2)
    # Breakdown:
    #   - O(N) for word_map: N entries
    #   - O(N^2) for adj_list: worst case N^2 edges (when many words differ by 1 char)
    #   - O(N) for visit set: max N words
    #   - O(N) for queue: max N words at once
    #   - Total: O(N^2) from adjacency list
    #
    # N -> len of word_list
    # M -> len of word in the word_list
    def __bfs1(self, begin_word: str, end_word: str, word_list: List[str]) -> int:        
        n, m = len(word_list), len(word_list[0])
        word_map = dict()  # O(N) space
        adj_list = [[] for _ in range(n)]  # O(N) space initially, grows to O(N^2)

        # O(N) to populate word_map
        for i, word in enumerate(word_list):
            word_map[word] = i
        
        # O(N^2 * M) - Compare all pairs of words
        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                # O(M) to compare each word pair
                for k in range(m):
                    if word_list[i][k] != word_list[j][k]:
                        diff += 1
                
                # O(1) to add edge if words differ by exactly 1 character
                if diff == 1:
                    adj_list[i].append(j)  # Can lead to O(N^2) edges total
                    adj_list[j].append(i)
            
        q, res = deque(), 1
        visit = set()  # O(N) space
        
        # O(M) to generate neighbors from beginWord
        for i in range(m):
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) == begin_word[i]:
                    continue
                
                word = begin_word[:i] + chr(c) + begin_word[i + 1:]
                # O(1) dict lookup after word creation
                if word in word_map and word not in visit:
                    q.append(word_map[word])
                    visit.add(word_map[word])
        
        # O(N^2) BFS: Visit N nodes, process up to N^2 edges total
        while len(q) > 0:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if word_list[node] == end_word:
                    return res
                # Process neighbors - total across all iterations is O(N^2) edges
                for neighbor in adj_list[node]:
                    if neighbor not in visit:
                        q.append(neighbor)
                        visit.add(neighbor)

        return 0