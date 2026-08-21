class Solution:
    # TC -> O(N + M)
    # SC -> O(N + M)
    # N -> # of words
    # M -> total number of chars in all words
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        encoded_list = []

        for word in strs:
            word_len = len(word)
            encoded_list.append(str(word_len))
            encoded_list.append(word)

        return "#".join(encoded_list)

    # TC -> O(N + M)
    # SC -> O(N + M)
    # N -> # of words
    # M -> total number of chars in all words
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        print (s)
        i = 0

        while i < len(s):
            word_len = 0
            while i < len(s) and s[i].isnumeric():
                num = int(s[i])
                word_len = word_len * 10 + num
                i += 1
            i += 1

            word = s[i: i + word_len]
            decoded_list.append("".join(word))

            i = i + word_len + 1
            
        
        return decoded_list
            