class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mapS, mapT = {}, {}
        for ch in s:
            mapS[ch]=mapS.get(ch, 0)+1
        for ch in t:
            mapT[ch]=mapT.get(ch, 0)+1
        return mapS == mapT