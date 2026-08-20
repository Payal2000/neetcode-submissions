class Solution:

    def encode(self, strs: List[str]) -> str:

        #defined an empty list
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        return res
        
    def decode(self, s: str) -> List[str]:

        res, i = [], 0

        # Keep decoding while i is still inside the string.
        while len(s) > i:
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j]) #[start : stop], start → INCLUDED, stop  → EXCLUDED

            word = s[j + 1 : j + 1 + length]

            res.append(word)

            i = j + 1 + length

        return res






