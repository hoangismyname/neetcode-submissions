from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Khởi tạo một dictionary với giá trị mặc định là list trống
        anagram_map = {}
        
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = []
            anagram_map[sorted_s].append(s)
        return list(anagram_map.values())