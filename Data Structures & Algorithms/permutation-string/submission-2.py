class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # return self.__check_inclusion_brute_force(s1, s2)
        return self.__check_inclusion_hash_table(s1, s2)

    # TC -> O(N * M)
    # SC -> O(N)
    # N -> len of s1
    # M -> len of s2
    def __check_inclusion_hash_table(self, s1: str, s2: str) -> bool:
        s1_dict = dict()

        for char in s1:
            s1_dict[char] = 1 + s1_dict.get(char, 0)

        needed = len(s1_dict)
        for i in range(len(s2)):
            s2_dict = dict()
            curr = 0
            for j in range(i, len(s2)):
                s2_dict[s2[j]] = 1 + s2_dict.get(s2[j], 0)
                if s1_dict.get(s2[j], 0) < s2_dict[s2[j]]:
                    break
                if s1_dict.get(s2[j], 0) == s2_dict[s2[j]]:
                    curr += 1
                if curr == needed:
                    return True 
        return False

    # TC -> O(log(N) * N ^ 3)
    # SC -> O(N)
    def __check_inclusion_brute_force(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                sub_str = s2[i: j + 1]
                sub_str = sorted(sub_str)
                if sub_str == s1:
                    return True
        
        return False