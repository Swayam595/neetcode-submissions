class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_array = []
        for word in strs:
            word_len = len(word)
            encoded_array.append(f"{word_len}#{word}")
        
        return "".join(encoded_array)

    def decode(self, s: str) -> List[str]:
        print (s)
        decoded_array = []
        i = 0

        while i < len(s):
            num_array = []

            while i < len(s) and s[i] != '#':
                num_array.append(s[i])
                i += 1
            
            word_len_str = "".join(num_array)
            word_len = int(word_len_str)
            
            i += 1
            
            j = 0
            word_array = []
            while i < len(s) and j < word_len:
                word_array.append(s[i])
                i += 1
                j += 1
            
            word = "".join(word_array)
            decoded_array.append(word)
            
        return decoded_array

