class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        # return self.__bfs1(beginWord, endWord, wordList)
        return self.__bfs2_meet_at_end(beginWord, endWord, wordList)

    # TC -> O(N *  M ^ 2)
    # SC -> O(N * M ^ 2)
    # N -> len of word_list
    # M -> len of word in the word_list
    def __bfs2_meet_at_end(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        word_set = set(word_list)
        m = len(word_list[0])
        qb, qe = deque([begin_word]), deque([end_word])
        from_begin, from_end = {begin_word: 1}, {end_word: 1}
    
        while qb and qe:
            if len(qb) > len(qe):
                qb, qe = qe, qb
                from_begin, from_end = from_end, from_begin

            for _ in range(len(qb)):
                word = qb.popleft()
                steps = from_begin[word]
                for i in range(m):
                    for c in range(ord('a'), ord('z') + 1):
                        if chr(c) == word[i]:
                            continue
                        new_word = word[:i] + chr(c) + word[i + 1:]
                        if new_word not in word_set:
                            continue
                        if new_word in from_end:
                            return steps + from_end[new_word]
                        if new_word not in from_begin:
                            from_begin[new_word] = steps + 1
                            qb.append(new_word)
        return 0

    # TC -> O(N + N ^ 2 * M + N * M + N ^ 2) ~ O(N ^ 2 * M)
    # SC -> O(N ^ 2)
    # N -> len of word_list
    # M -> len of word in the word_list
    def __bfs1(self, begin_word: str, end_word: str, word_list: List[str]) -> int:        
        n, m = len(word_list), len(word_list[0])
        word_map = dict()
        adj_list = [[] for _ in range(n)]

        for i, word in enumerate(word_list):
            word_map[word] = i
        
        for i in range(n):
            for j in range(i + 1, n):
                diff = 0
                for k in range(m):
                    if word_list[i][k] != word_list[j][k]:
                        diff += 1
                    
                if diff == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
            
        q, res = deque(), 1
        visit = set()
        for i in range(m):
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) == begin_word[i]:
                    continue
                
                word = begin_word[:i] + chr(c) + begin_word[i + 1:]
                if word in word_map and word not in visit:
                    q.append(word_map[word])
                    visit.add(word_map[word])
        
        while len(q) > 0:
            res += 1
            for i in range(len(q)):
                node = q.popleft()
                if word_list[node] == end_word:
                    return res
                for neighbor in adj_list[node]:
                    if neighbor not in visit:
                        q.append(neighbor)
                        visit.add(neighbor)

        return 0