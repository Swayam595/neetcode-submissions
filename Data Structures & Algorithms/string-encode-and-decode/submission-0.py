class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []

        for word in strs:
            encoded_word_list = [str(len(word)), "/:", word]
            encoded_word_str = "".join(encoded_word_list)
            encoded_string.append(encoded_word_str)
        
        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        i = 0

        while i < len(s):
            delim = i
            while delim + 1 < len(s) and s[delim:delim+2] != "/:":
                delim += 1

            encoded_word_length = int(s[i:delim])
            encoded_word = s[delim + 2:delim + encoded_word_length + 2] 
            decoded_string.append(encoded_word)
            i = delim + encoded_word_length + 2
        
        return decoded_string