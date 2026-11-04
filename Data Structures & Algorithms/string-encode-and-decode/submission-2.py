class Solution:
    def encode(self, strs: List[str]) -> str:
        encodeString = ""
        for string in strs:
            encodeString += str(len(string)) + '#' + string
        return encodeString

    def decode(self, s: str) -> List[str]:

        decodeStrings = []
        i = 0
        while i < len(s):
            delimiter = s.find('#', i)
            length = int(s[i:delimiter])
            decodeStrings.append(s[delimiter + 1:delimiter + 1 + length])
            i = delimiter + 1 + length
        return decodeStrings