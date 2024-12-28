# Notes:

# Time  Complexity: O(n), where n is the total number of characters in all strings in input
# Space Complexity: O(k), where k is the number of strings

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # length-prefix encoding handles cases where the delimiter is part of the string itself
        encoded = ""
        for word in strs:
            encoded += f"{len(word)}#{word}" 
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i < len(s):
            j = s.find("#", i) # finds the first '#' starting at index i
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))